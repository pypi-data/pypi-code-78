# copyright (c) 2020 PaddlePaddle Authors. All Rights Reserve.
#
# Modifications copyright (c) 2021 DocYard Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__all__ = ['build_backbone']


def build_backbone(config, model_type):
    if model_type == 'det':
        from .det_mobilenet_v3 import MobileNetV3
        from .det_vgg16_bn import VGG16_BN
        from .det_resnet_vd import ResNet
        from .det_resnet_vd_sast import ResNet_SAST
        support_dict = ['VGG16_BN', 'MobileNetV3', 'ResNet', 'ResNet_SAST']
    elif model_type == 'rec' or model_type == 'cls':
        from .rec_mobilenet_v3 import MobileNetV3
        from .rec_resnet_vd import ResNet
        from .rec_resnet_fpn import ResNetFPN
        support_dict = ['MobileNetV3', 'ResNet', 'ResNetFPN']
    else:
        raise NotImplementedError

    module_name = config.pop('name')
    assert module_name in support_dict, Exception(
        'when model typs is {}, backbone only support {}'.format(model_type,
                                                                 support_dict))
    module_class = eval(module_name)(**config)
    return module_class
