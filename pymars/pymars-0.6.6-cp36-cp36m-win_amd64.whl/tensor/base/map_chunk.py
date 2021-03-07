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

import numpy as np

from ... import opcodes
from ...custom_log import redirect_custom_log
from ...serialize import FunctionField, BoolField, TupleField, \
    DictField, StringField
from ...utils import enter_current_session, quiet_stdio
from ..operands import TensorOperand, TensorOperandMixin


class TensorMapChunk(TensorOperand, TensorOperandMixin):
    _op_type_ = opcodes.MAP_CHUNK

    _func = FunctionField('func')
    _elementwise = BoolField('elementwise')
    _args = TupleField('args')
    _kwargs = DictField('kwargs')
    _with_chunk_index = BoolField('with_chunk_index')
    # for chunk
    _tileable_op_key = StringField('tileable_op_key')

    def __init__(self, func=None, args=None, kwargs=None, tileable_op_key=None,
                 elementwise=None, with_chunk_index=None, **kw):
        super().__init__(_func=func, _args=args, _kwargs=kwargs, _elementwise=elementwise,
                         _with_chunk_index=with_chunk_index,
                         _tileable_op_key=tileable_op_key, **kw)

    @property
    def func(self):
        return self._func

    @property
    def elementwise(self):
        return self._elementwise

    @property
    def args(self):
        return self._args

    @property
    def kwargs(self):
        return self._kwargs

    @property
    def tileable_op_key(self):
        return self._tileable_op_key

    @property
    def with_chunk_index(self):
        return self._with_chunk_index

    def __call__(self, t, dtype=None):
        if dtype is None:
            try:
                kwargs = self.kwargs or dict()
                if self.with_chunk_index:
                    kwargs['chunk_index'] = (0,) * t.ndim
                with np.errstate(all='ignore'), quiet_stdio():
                    mock_result = self.func(np.random.rand(2, 2).astype(t.dtype),
                                            *(self.args or ()), **kwargs)
            except:
                raise TypeError('Cannot estimate output type of map_chunk call')
            dtype = mock_result.dtype

        new_shape = t.shape if self.elementwise else (np.nan,) * t.ndim
        return self.new_tensor([t], dtype=dtype, shape=new_shape)

    @classmethod
    def tile(cls, op: 'TensorMapChunk'):
        inp = op.inputs[0]
        out = op.outputs[0]

        chunks = []
        for c in inp.chunks:
            params = c.params
            params['dtype'] = inp.dtype
            if not op.elementwise:
                params['shape'] = (np.nan,) * c.ndim

            new_op = op.copy().reset_key()
            new_op._tileable_op_key = out.key
            chunks.append(new_op.new_chunk([c], **params))

        new_op = op.copy().reset_key()
        params = out.params
        nsplits = inp.nsplits
        if not op.elementwise:
            nsplits = tuple((np.nan,) * len(sp) for sp in nsplits)
        return new_op.new_tileables([inp], chunks=chunks, nsplits=nsplits, **params)

    @classmethod
    @redirect_custom_log
    @enter_current_session
    def execute(cls, ctx, op: 'TensorMapChunk'):
        in_data = ctx[op.inputs[0].key]
        out_chunk = op.outputs[0]

        kwargs = op.kwargs or dict()
        if op.with_chunk_index:
            kwargs['chunk_index'] = out_chunk.index
        ctx[op.outputs[0].key] = op.func(in_data, *(op.args or ()), **kwargs)


def map_chunk(t, func, args=(), **kwargs):
    """
    Apply function to each chunk.

    Parameters
    ----------
    func : function
        Function to apply to each chunk.
    args : tuple
        Positional arguments to pass to func in addition to the array.
    **kwargs
        Additional keyword arguments to pass as keywords arguments to func.

    Returns
    -------
    Tensor
        Result of applying ``func`` to each chunk of the Tensor.

    Examples
    --------
    >>> import mars.tensor as mt
    >>> a = mt.array([[4, 9]] * 3)
    >>> a.execute()
    array([[4, 9],
           [4, 9],
           [4, 9]])

    Output dtype will be auto inferred.

    >>> a.map_chunk(lambda c: c * 0.5).execute()
    array([[2. , 4.5],
           [2. , 4.5],
           [2. , 4.5]])

    You can specify ``dtype`` by yourself if auto infer failed.
    """
    elementwise = kwargs.pop('elementwise', None)
    dtype = np.dtype(kwargs.pop('dtype')) if 'dtype' in kwargs else None
    with_chunk_index = kwargs.pop('with_chunk_index', False)

    op = TensorMapChunk(func=func, args=args, kwargs=kwargs, elementwise=elementwise,
                        with_chunk_index=with_chunk_index)
    return op(t, dtype=dtype)
