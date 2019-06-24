# Copyright 2019 The Sonnet Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or  implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""Utils for Sonnet optimizers."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from sonnet.src import replicator
import tensorflow as tf


def check_strategy():
  if tf.distribute.has_strategy():
    strategy = tf.distribute.get_strategy()
    if not isinstance(strategy, replicator.Replicator):
      raise ValueError("Sonnet optimizers are not compatible with {}. Please"
                       "use `sonnet.distribute.Replicator` instead.".format(
                           strategy.__class__.__name__))


def check_updates_parameters(updates, parameters):
  if len(updates) != len(parameters):
    raise ValueError("`updates` and `parameters` must be the same length.")
  if not parameters:
    raise ValueError("`parameters` cannot be empty.")


def check_same_dtype(update, parameter):
  # TODO(petebu): Consider casting inconsistent dtypes.
  if update.dtype != parameter.dtype:
    raise ValueError(
        "DType of update {!r} is not equal to that of parameter {!r}".format(
            update, parameter))