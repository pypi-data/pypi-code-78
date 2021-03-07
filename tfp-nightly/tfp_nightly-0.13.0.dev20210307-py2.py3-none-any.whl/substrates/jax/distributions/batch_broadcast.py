# Copyright 2021 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Batch broadcasting meta-distribuion."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Dependency imports
from tensorflow_probability.python.internal.backend.jax.compat import v2 as tf

from tensorflow_probability.substrates.jax.bijectors import bijector as bijector_lib
from tensorflow_probability.substrates.jax.distributions import distribution as distribution_lib
from tensorflow_probability.substrates.jax.internal import assert_util
from tensorflow_probability.substrates.jax.internal import prefer_static as ps
from tensorflow_probability.substrates.jax.internal import tensor_util
from tensorflow_probability.substrates.jax.internal import tensorshape_util


__all__ = ['BatchBroadcast']


def _make_bcast_fn(fn_name, n_event_shapes):
  """Implements functions like mean, variance, etc."""
  def fn(self, *args, **kwargs):
    val = getattr(self.distribution, fn_name)(*args, **kwargs)
    single_val_shape = self.batch_shape_tensor()
    if n_event_shapes:
      single_val_shape = ps.concat(
          [single_val_shape] + [self.event_shape_tensor()] * n_event_shapes,
          axis=0)
    return tf.broadcast_to(
        val, ps.broadcast_shape(ps.shape(val), single_val_shape))
  fn.__name__ = f'_{fn_name}'
  return fn


class BatchBroadcast(distribution_lib.Distribution):
  """A distribution that broadcasts an underlying distribution's batch shape.

  This meta-distribution can be useful when we desire to implicitly broadcast
  an underlying distribution's batch shape with, or to, another shape, typically
  to parameterize a larger batch of distributions.

  This distribution supports two flavors of broadcasting. The
  `with_shape` argument broadcasts the underlying distribution's batch
  shape _with_ a compatible shape `with_shape`, obtaining a batch shape that
  results from the broadcast of these two shapes together. Alternatively,
  the `to_shape` argument broadcasts the underlying distribution's
  batch shape _to_ the exact shape specified. With an unnamed argument, the more
  permissive `with_shape` behavior is used.

  #### Examples

  ```python
  d = tfd.BatchBroadcast(tfd.Normal(tf.range(3.), 1.), with_shape=[2, 3])
  d.batch_shape  # => [2, 3]
  d.distribution.batch_shape  # => [3]
  d.event_shape  # => []

  d = tfd.BatchBroadcast(tfd.Normal(tf.range(3.), 1.), to_shape=[2, 3])
  d.batch_shape  # => [2, 3]

  df = tfd.Uniform(4., 5.).sample([10, 1])
  d = tfd.BatchBroadcast(
      tfd.WishartTriL(df=df, scale_tril=tf.eye(3)), with_shape=[2])
  d.batch_shape  # => [10, 2]
  d.distribution.batch_shape  # => [10, 1]
  d.event_shape  # => [3, 3]

  d = tfd.BatchBroadcast(
      tfd.WishartTriL(df=df, scale_tril=tf.eye(3)), to_shape=[2])
  # => Exception: to_shape is too small

  d = tfd.BatchBroadcast(tfd.WishartTriL(df=df, scale_tril=tf.eye(3)),
                         to_shape=[10, 2])
  d.batch_shape  # => [10, 2]
  ```

  #### Example: Spatially distributed samples

  In some cases a particular batch shape may be required, but the underlying
  parameterization has a smaller representation.

  Suppose data is sampled in 10 different vicinities on a globe. We might write:

  ```python
  loc = tfp.random.spherical_uniform([10], 3)
  components_dist = tfd.VonMisesFisher(mean_direction=loc, concentration=50.)
  ```

  Now suppose we are operating 500 different experiments, each of which samples
  these different vicinities in different proportions. We might hope to write:

  ```python
  mixture_dist = tfd.Categorical(logits=tf.random.stateless_uniform([500, 10]))
  obs_dist = tfd.MixtureSameFamily(mixture_dist, components_dist)
  ```

  But this currently (Feb. 2021) causes an exception `ValueError:
  mixture_distribution.batch_shape ([500]) is not compatible with
  components_distribution.batch_shape ([])`.

  A naive fix would be to broadcast the parameters of `components_dist` to
  ensure the component distribution has batch shape `[500, 10]`. But this is
  wasteful in that it replicates a `[10, 3]`-shaped tensor 500 times, and will
  cause unnecessary computation, memory motion, etc. Using `BatchBroadcast` we
  may write:

  ```python
  obs_dist = tfd.MixtureSameFamily(
      mixture_dist, tfd.BatchBroadcast(components_dist, [500, 10]))
  ```

  This allows us to avoid avoid replicating any parameters, but achieve the
  requisite batch shape. If we would like to evaluate the likelihood of 20 given
  observation locations under each different experiment, we might write:

  ```python
  test_sites = tfp.random.spherical_uniform([20], 3)
  lp = tfd.Sample(obs_dist, 20).log_prob(test_sites)  # shape [500]
  ```
  """

  def __init__(self, distribution, with_shape=None, *, to_shape=None,
               validate_args=False, name=None):
    """Constructs a new BatchBroadcast distribution.

    Args:
      distribution: The underlying distribution. Must have batch shape
        compatible with `broadcast_shape`.
      with_shape: The shape _with which_ the underlying distribution's batch
        shape is to be broadcast. The resulting batch shape may be different
        from either input. Mutually exclusive with `to_shape`.
      to_shape: The shape _to which_ the underlying distribution's batch
        shape is to be broadcast. This provides a stricter contract than
        `with_shape`, in that the resulting batch shape will be exactly the
        one provided in `to_shape`. Mutually exclusive with
        `with_shape`.
      validate_args: Indicates whether additional assertions should be used; may
        impose a performance penalty.
      name: Optional name for the distribution.
    """
    parameters = dict(locals())
    self._distribution = distribution
    if (to_shape is None) == (with_shape is None):
      raise ValueError(
          'Exactly one of `with_shape` or `to_shape` must be given.')
    self._with_shape = tensor_util.convert_nonref_to_tensor(
        with_shape, dtype_hint=tf.int32, as_shape_tensor=True,
        name='with_shape')
    self._to_shape = tensor_util.convert_nonref_to_tensor(
        to_shape, dtype_hint=tf.int32, as_shape_tensor=True,
        name='to_shape')
    with tf.name_scope(name or f'BatchBroadcast{distribution.name}') as name:
      super(BatchBroadcast, self).__init__(
          dtype=distribution.dtype,
          reparameterization_type=distribution.reparameterization_type,
          validate_args=validate_args,
          allow_nan_stats=distribution.allow_nan_stats,
          parameters=parameters,
          name=name)

  @property
  def distribution(self):
    return self._distribution

  @property
  def with_shape(self):
    return self._with_shape

  @property
  def to_shape(self):
    return self._to_shape

  def __getitem__(self, slices):
    # Implementing this method would require logic similar to
    # slicing._slice_single_param, but mapped to distribution instances instead
    # of Tensors.
    raise NotImplementedError(
        'Slices of `BatchBroadcast` are not implemented. Email '
        'tfprobability@tensorflow.org if this would be helpful.')

  def _batch_shape(self):
    if self.to_shape is None:
      return tf.broadcast_static_shape(
          self.distribution.batch_shape,
          tf.TensorShape(tf.get_static_value(self.with_shape)))
    return tf.TensorShape(tf.get_static_value(self.to_shape))

  def _batch_shape_tensor(self):
    if self.to_shape is None:
      return ps.broadcast_shape(self.distribution.batch_shape_tensor(),
                                self.with_shape)
    return self.to_shape

  def _event_shape(self):
    return self.distribution.event_shape

  def _event_shape_tensor(self):
    return self.distribution.event_shape_tensor()

  def _sample_n(self, n, seed=None):
    batch_shape = self.batch_shape_tensor()
    batch_rank = ps.rank_from_shape(batch_shape)
    n_batch = ps.reduce_prod(batch_shape)

    underlying_batch_shape = self.distribution.batch_shape_tensor()
    underlying_batch_rank = ps.rank_from_shape(underlying_batch_shape)
    underlying_n_batch = ps.reduce_prod(underlying_batch_shape)

    # Left pad underlying shape with any necessary ones.
    underlying_bcast_shp = ps.concat(
        [ps.ones([ps.maximum(batch_rank - underlying_batch_rank, 0)],
                 dtype=underlying_batch_shape.dtype),
         underlying_batch_shape],
        axis=0)

    # Determine how many underlying samples to produce.
    n_bcast_samples = ps.maximum(0, n_batch // underlying_n_batch)
    samps = self.distribution.sample([n, n_bcast_samples], seed=seed)

    is_dim_bcast = ps.not_equal(batch_shape, underlying_bcast_shp)

    event_shape = self.event_shape_tensor()
    event_rank = ps.rank_from_shape(event_shape)
    shp = ps.concat([[n], ps.where(is_dim_bcast, batch_shape, 1),
                     underlying_bcast_shp,
                     event_shape], axis=0)
    # Reshape to expand n_bcast_samples and ones-padded underlying_bcast_shp.
    samps = tf.reshape(samps, shp)
    # Interleave broadcast and underlying axis indices for transpose.
    interleaved_batch_axes = ps.reshape(
        ps.stack([ps.range(batch_rank),
                  ps.range(batch_rank) + batch_rank],
                 axis=-1),
        [-1]) + 1

    event_axes = ps.range(event_rank) + (1 + 2 * batch_rank)
    perm = ps.concat([[0], interleaved_batch_axes, event_axes], axis=0)
    samps = tf.transpose(samps, perm=perm)
    # Finally, reshape to the fully-broadcast batch shape.
    return tf.reshape(samps, ps.concat([[n], batch_shape, event_shape], axis=0))

  _log_prob = _make_bcast_fn('log_prob', n_event_shapes=0)
  _prob = _make_bcast_fn('prob', n_event_shapes=0)
  _log_cdf = _make_bcast_fn('log_cdf', n_event_shapes=0)
  _cdf = _make_bcast_fn('cdf', n_event_shapes=0)
  _log_survival_function = _make_bcast_fn(
      'log_survival_function', n_event_shapes=0)
  _survival_function = _make_bcast_fn(
      'survival_function', n_event_shapes=0)

  _entropy = _make_bcast_fn('entropy', n_event_shapes=0)
  _mode = _make_bcast_fn('mode', n_event_shapes=1)
  _mean = _make_bcast_fn('mean', n_event_shapes=1)
  _variance = _make_bcast_fn('variance', n_event_shapes=1)
  _stddev = _make_bcast_fn('stddev', n_event_shapes=1)
  _covariance = _make_bcast_fn('covariance', n_event_shapes=2)
  _quantile = _make_bcast_fn('quantile', n_event_shapes=1)

  def _default_event_space_bijector(self):
    bijector = self.distribution.experimental_default_event_space_bijector()
    if bijector is None:
      return None
    return _BroadcastingBijector(self, bijector)

  def _parameter_control_dependencies(self, is_init):
    if tensorshape_util.is_fully_defined(self.distribution.batch_shape):
      if self.to_shape is not None:
        static_to_shape = tf.get_static_value(self.to_shape)
        if static_to_shape is not None:
          bcast_shp = tf.broadcast_static_shape(
              tf.TensorShape(static_to_shape),
              self.distribution.batch_shape)
          if bcast_shp != static_to_shape:
            raise ValueError(f'Argument `to_shape` ({static_to_shape}) '
                             'is incompatible with underlying distribution '
                             f'batch shape ({self.distribution.batch_shape}).')

      else:
        static_with_shape = tf.get_static_value(self.with_shape)
        if static_with_shape is not None:
          tf.broadcast_static_shape(  # Ensure compatible.
              tf.TensorShape(static_with_shape),
              self.distribution.batch_shape)

    underlying = self.distribution._parameter_control_dependencies(is_init)  # pylint: disable=protected-access
    if not self.validate_args:
      return underlying

    checks = []
    if self.to_shape is not None:
      if tensor_util.is_ref(self.to_shape) != is_init:
        checks += [assert_util.assert_equal(
            self.to_shape,
            ps.broadcast_shape(self.distribution.batch_shape_tensor(),
                               self.to_shape),
            message='Argument `to_shape` is incompatible with underlying '
                    'distribution batch shape.')]
    else:
      if tensor_util.is_ref(self.with_shape) != is_init:
        checks += [tf.broadcast_dynamic_shape(
            self.distribution.batch_shape_tensor(),
            self.with_shape)]

    return tuple(checks) + tuple(underlying)

  def _sample_control_dependencies(self, value, **kwargs):
    return self.distribution._sample_control_dependencies(value, **kwargs)  # pylint: disable=protected-access

  _composite_tensor_nonshape_params = ('distribution',)
  _composite_tensor_shape_params = ('with_shape', 'to_shape')


class _BroadcastingBijector(bijector_lib.Bijector):
  """Event space bijector for BatchBroadcast."""

  def __init__(self, bcast_dist, bijector):
    parameters = dict(locals())
    self.bcast_dist = bcast_dist
    self.bijector = bijector
    super(_BroadcastingBijector, self).__init__(
        validate_args=bcast_dist.validate_args,
        dtype=bijector.dtype,
        forward_min_event_ndims=bijector.forward_min_event_ndims,
        inverse_min_event_ndims=bijector.inverse_min_event_ndims,
        parameters=parameters)

  def _single_event_shape(self):
    return tensorshape_util.concatenate(self.bcast_dist.batch_shape,
                                        self.bcast_dist.event_shape)

  def _single_event_shape_tensor(self):
    return ps.concat([self.bcast_dist.batch_shape_tensor(),
                      self.bcast_dist.event_shape_tensor()], axis=0)

  def _forward_event_shape(self, x):
    return self.bijector.forward_event_shape(x)

  def _forward_event_shape_tensor(self, x):
    return self.bijector.forward_event_shape_tensor(x)

  def _inverse_event_shape(self, y):
    return self.bijector.inverse_event_shape(y)

  def _inverse_event_shape_tensor(self, y):
    return self.bijector.inverse_event_shape_tensor(y)

  def _bcast_x(self, x):
    shp = self.bijector.inverse_event_shape(self._single_event_shape())
    if not tensorshape_util.is_fully_defined(shp):
      shp = self.bijector.inverse_event_shape_tensor(
          self._single_event_shape_tensor())
    return tf.broadcast_to(x, ps.broadcast_shape(ps.shape(x), shp))

  def _forward(self, x):
    return self.bijector.forward(self._bcast_x(x))

  def _forward_log_det_jacobian(self, x):
    return self.bijector.forward_log_det_jacobian(self._bcast_x(x))

  def _bcast_y(self, y):
    return tf.broadcast_to(
        y, ps.broadcast_shape(ps.shape(y), self._single_event_shape_tensor()))

  def _inverse(self, y):
    return self.bijector.inverse(self._bcast_y(y))

  def _inverse_log_det_jacobian(self, y):
    return self.bijector.inverse_log_det_jacobian(self._bcast_y(y))

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# This file is auto-generated by substrates/meta/rewrite.py
# It will be surfaced by the build system as a symlink at:
#   `tensorflow_probability/substrates/jax/distributions/batch_broadcast.py`
# For more info, see substrate_runfiles_symlinks in build_defs.bzl
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# (This notice adds 10 to line numbering.)


