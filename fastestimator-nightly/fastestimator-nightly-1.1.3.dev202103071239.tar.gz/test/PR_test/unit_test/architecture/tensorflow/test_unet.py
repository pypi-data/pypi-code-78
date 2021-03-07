# Copyright 2020 The FastEstimator Authors. All Rights Reserved.
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
# ==============================================================================
import unittest

import numpy as np
import tensorflow as tf

from fastestimator.architecture.tensorflow import UNet


class TestUNet(unittest.TestCase):
    def test_unet(self):
        data = np.ones((1, 128, 128, 1))
        input_data = tf.constant(data)
        unet = UNet()
        output_shape = unet(input_data).numpy().shape
        self.assertEqual(output_shape, (1, 128, 128, 1))
