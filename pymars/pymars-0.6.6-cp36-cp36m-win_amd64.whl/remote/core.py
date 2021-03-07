# Copyright 1999-2020 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections.abc import Iterable
from functools import partial

import numpy as np

from .. import opcodes
from ..core import Entity, Base, ChunkData
from ..custom_log import redirect_custom_log
from ..dataframe.core import DATAFRAME_TYPE, SERIES_TYPE, INDEX_TYPE
from ..serialize import FunctionField, ListField, DictField, \
    BoolField, Int32Field, StringField
from ..operands import ObjectOperand
from ..tensor.core import TENSOR_TYPE
from ..utils import build_fetch_tileable, calc_nsplits, enter_current_session
from .operands import RemoteOperandMixin
from .utils import replace_inputs, find_objects


class _TileablePlaceholder:
    def __init__(self, tileable):
        self.tileable = build_fetch_tileable(tileable)

    def __getstate__(self):
        fetch_op = self.tileable.op
        fetch_tileable = self.tileable
        chunk_infos = [(type(c.op), c.op.output_types, c.key, c.id, c.params)
                       for c in fetch_tileable.chunks]
        return type(fetch_op), fetch_op.id, fetch_op.output_types, \
               fetch_tileable.params, fetch_tileable.nsplits, chunk_infos

    def __setstate__(self, state):
        fetch_op_type, fetch_op_id, output_types, params, nsplits, chunk_infos = state
        params['nsplits'] = nsplits
        chunks = []
        for ci in chunk_infos:
            chunk_op_type, chunk_op_output_types, chunk_key, chunk_id, chunk_params = ci
            chunk = chunk_op_type(output_types=chunk_op_output_types).new_chunk(
                None, _key=chunk_key, _id=chunk_id, kws=[chunk_params])
            chunks.append(chunk)
        params['chunks'] = chunks
        self.tileable = fetch_op_type(
            _id=fetch_op_id, output_types=output_types).new_tileable(None, kws=[params])

    def __mars_tokenize__(self):
        return self.__getstate__()

    def __call__(self):  # pragma: no cover
        # make itself serializable
        pass


class RemoteFunction(RemoteOperandMixin, ObjectOperand):
    _op_type_ = opcodes.REMOTE_FUNCATION
    _op_module_ = 'remote'

    _function = FunctionField('function')
    _function_args = ListField('function_args')
    _function_kwargs = DictField('function_kwargs')
    _retry_when_fail = BoolField('retry_when_fail')
    _n_output = Int32Field('n_output')
    # for chunk
    _tileable_op_key = StringField('tileable_op_key')

    def __init__(self, function=None, function_args=None,
                 function_kwargs=None, retry_when_fail=None,
                 n_output=None, tileable_op_key=None, **kw):
        super().__init__(_function=function, _function_args=function_args,
                         _function_kwargs=function_kwargs,
                         _retry_when_fail=retry_when_fail,
                         _n_output=n_output, _tileable_op_key=tileable_op_key, **kw)

    @property
    def function(self):
        return self._function

    @property
    def function_args(self):
        return self._function_args

    @property
    def function_kwargs(self):
        return self._function_kwargs

    @property
    def retry_when_fail(self):
        return self._retry_when_fail

    @property
    def n_output(self):
        return self._n_output

    @property
    def tileable_op_key(self):
        return self._tileable_op_key

    @property
    def output_limit(self):
        return self._n_output or 1

    @property
    def retryable(self) -> bool:
        return self._retry_when_fail

    @classmethod
    def _no_prepare(cls, tileable):
        return isinstance(tileable, (TENSOR_TYPE, DATAFRAME_TYPE,
                                     SERIES_TYPE, INDEX_TYPE))

    def _set_inputs(self, inputs):
        raw_inputs = getattr(self, '_inputs', None)
        super()._set_inputs(inputs)

        function_inputs = iter(inp for inp in self._inputs)
        mapping = {inp: new_inp for inp, new_inp in zip(inputs, self._inputs)}
        if raw_inputs is not None:
            for raw_inp in raw_inputs:
                if self._no_prepare(raw_inp):
                    if not isinstance(self._inputs[0], ChunkData):
                        # not in tile, set_inputs from tileable
                        mapping[raw_inp] = next(function_inputs)
                    else:
                        # in tile, set_inputs from chunk
                        mapping[raw_inp] = _TileablePlaceholder(raw_inp)
                else:
                    mapping[raw_inp] = next(function_inputs)
        self._function_args = replace_inputs(self._function_args, mapping)
        self._function_kwargs = replace_inputs(self._function_kwargs, mapping)

    def __call__(self):
        find_inputs = partial(find_objects, types=(Entity, Base))
        inputs = find_inputs(self._function_args) + find_inputs(self._function_kwargs)
        if self.n_output is None:
            return self.new_tileable(inputs)
        else:
            return self.new_tileables(
                inputs, kws=[dict(i=i) for i in range(self.n_output)])

    @classmethod
    def tile(cls, op):
        outs = op.outputs
        chunk_op = op.copy().reset_key()

        chunk_inputs = []
        pure_depends = []
        for inp in op.inputs:
            if cls._no_prepare(inp):  # pragma: no cover
                # if input is tensor, DataFrame etc,
                # do not prepare data, because the data may be to huge,
                # and users can choose to fetch slice of the data themselves
                pure_depends.extend([True] * len(inp.chunks))
            else:
                pure_depends.extend([False] * len(inp.chunks))
            chunk_inputs.extend(inp.chunks)
        chunk_op._pure_depends = pure_depends
        # record tileable op key for chunk op
        chunk_op._tileable_op_key = op.key

        out_chunks = [list() for _ in range(len(outs))]
        chunk_kws = []
        for i, out in enumerate(outs):
            chunk_params = out.params
            chunk_params['index'] = ()
            chunk_params['i'] = i
            chunk_kws.append(chunk_params)
        chunks = chunk_op.new_chunks(chunk_inputs, kws=chunk_kws)
        for i, c in enumerate(chunks):
            out_chunks[i].append(c)

        kws = []
        for i, out in enumerate(outs):
            params = out.params
            params['chunks'] = out_chunks[i]
            params['nsplits'] = ()
            kws.append(params)
        new_op = op.copy()
        return new_op.new_tileables(op.inputs, kws=kws)

    @classmethod
    @redirect_custom_log
    @enter_current_session
    def execute(cls, ctx, op: "RemoteFunction"):
        mapping = {inp: ctx[inp.key] for inp, is_pure_dep
                   in zip(op.inputs, op.pure_depends) if not is_pure_dep}
        for to_search in [op.function_args, op.function_kwargs]:
            tileable_placeholders = find_objects(to_search, _TileablePlaceholder)
            for ph in tileable_placeholders:
                tileable = ph.tileable
                chunk_index_to_shape = dict()
                for chunk in tileable.chunks:
                    if any(np.isnan(s) for s in chunk.shape):
                        shape = ctx.get_chunk_metas([chunk.key], filter_fields=['chunk_shape'])[0][0]
                        chunk._shape = shape
                    chunk_index_to_shape[chunk.index] = chunk.shape
                if any(any(np.isnan(s) for s in ns) for ns in tileable._nsplits):
                    nsplits = calc_nsplits(chunk_index_to_shape)
                    tileable._nsplits = nsplits
                    tileable._shape = tuple(sum(ns) for ns in nsplits)
                mapping[ph] = tileable

        function = op.function
        function_args = replace_inputs(op.function_args, mapping)
        function_kwargs = replace_inputs(op.function_kwargs, mapping)

        result = function(*function_args, **function_kwargs)

        if op.n_output is None:
            ctx[op.outputs[0].key] = result
        else:
            if not isinstance(result, Iterable):
                raise TypeError(f'Specifying n_output={op.n_output}, '
                                f'but result is not iterable, got {result}')
            result = list(result)
            if len(result) != op.n_output:
                raise ValueError(f'Length of return value should be {op.n_output}, '
                                 f'got {len(result)}')
            for out, r in zip(op.outputs, result):
                ctx[out.key] = r


def spawn(func, args=(), kwargs=None, retry_when_fail=False, n_output=None):
    """
    Spawn a function and return a Mars Object which can be executed later.

    Parameters
    ----------
    func : function
        Function to spawn.
    args: tuple
       Args to pass to function
    kwargs: dict
       Kwargs to pass to function
    retry_when_fail: bool, default False
       If True, retry when function failed.
    n_output: int
       Count of outputs for the function

    Returns
    -------
    Object
        Mars Object.

    Examples
    --------
    >>> import mars.remote as mr
    >>> def inc(x):
    >>>     return x + 1
    >>>
    >>> result = mr.spawn(inc, args=(0,))
    >>> result
    Object <op=RemoteFunction, key=e0b31261d70dd9b1e00da469666d72d9>
    >>> result.execute().fetch()
    1

    List of spawned functions can be converted to :class:`mars.remote.ExecutableTuple`,
    and `.execute()` can be called to run together.

    >>> results = [mr.spawn(inc, args=(i,)) for i in range(10)]
    >>> mr.ExecutableTuple(results).execute().fetch()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Mars Object returned by :meth:`mars.remote.spawn` can be treated
    as arguments for other spawn functions.

    >>> results = [mr.spawn(inc, args=(i,)) for i in range(10)]   # list of spawned functions
    >>> def sum_all(xs):
            return sum(xs)
    >>> mr.spawn(sum_all, args=(results,)).execute().fetch()
    55

    inside a spawned function, new functions can be spawned.

    >>> def driver():
    >>>     results = [mr.spawn(inc, args=(i,)) for i in range(10)]
    >>>     return mr.ExecutableTuple(results).execute().fetch()
    >>>
    >>> mr.spawn(driver).execute().fetch()
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Mars tensor, DataFrame and so forth is available in spawned functions as well.

    >>> import mars.tensor as mt
    >>> def driver2():
    >>>     t = mt.random.rand(10, 10)
    >>>     return t.sum().to_numpy()
    >>>
    >>> mr.spawn(driver2).execute().fetch()
    52.47844223908132

    Argument of `n_output` can indicate that the spawned function will return multiple outputs.
    This is important when some of the outputs may be passed to different functions.

    >>> def triage(alist):
    >>>     ret = [], []
    >>>     for i in alist:
    >>>         if i < 0.5:
    >>>             ret[0].append(i)
    >>>         else:
    >>>             ret[1].append(i)
    >>>     return ret
    >>>
    >>> def sum_all(xs):
    >>>     return sum(xs)
    >>>
    >>> l = [0.4, 0.7, 0.2, 0.8]
    >>> la, lb = mr.spawn(triage, args=(l,), n_output=2)
    >>>
    >>> sa = mr.spawn(sum_all, args=(la,))
    >>> sb = mr.spawn(sum_all, args=(lb,))
    >>> mr.ExecutableTuple([sa, sb]).execute().fetch()
    >>> [0.6000000000000001, 1.5]
    """
    if not isinstance(args, tuple):
        args = [args]
    else:
        args = list(args)
    if kwargs is None:
        kwargs = dict()
    if not isinstance(kwargs, dict):
        raise TypeError('kwargs has to be a dict')

    op = RemoteFunction(function=func, function_args=args,
                        function_kwargs=kwargs,
                        retry_when_fail=retry_when_fail,
                        n_output=n_output)
    return op()
