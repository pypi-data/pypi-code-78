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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import torch
import torch.nn as nn
import torch.nn.functional as F

__all__ = ["ResNet_SAST"]


class ConvBNLayer(nn.Module):
    def __init__(
            self,
            in_channels,
            out_channels,
            kernel_size,
            stride=1,
            groups=1,
            is_vd_mode=False,
            act=None):
        super(ConvBNLayer, self).__init__()
        
        self.act = act
        self.is_vd_mode = is_vd_mode
        self._pool2d_avg = nn.AvgPool2d(
            kernel_size=2, stride=2, padding=0, ceil_mode=True)
        self._conv = nn.Conv2d(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            stride=stride,
            padding=(kernel_size - 1) // 2,
            groups=groups,
            bias=False)

        self._batch_norm = nn.BatchNorm2d(
            out_channels)
        if act=='relu':
            self.relu=nn.ReLU(inplace=True)
            
    def forward(self, inputs):
        if self.is_vd_mode:
            inputs = self._pool2d_avg(inputs)
        y = self._conv(inputs)
        y = self._batch_norm(y)
        
        if self.act=='relu':
            y = self.relu(y)
        return y



class BottleneckBlock(nn.Module):
    def __init__(self,
                 in_channels,
                 out_channels,
                 stride,
                 shortcut=True,
                 if_first=False):
        super(BottleneckBlock, self).__init__()

        self.conv0 = ConvBNLayer(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=1,
            act='relu')
        self.conv1 = ConvBNLayer(
            in_channels=out_channels,
            out_channels=out_channels,
            kernel_size=3,
            stride=stride,
            act='relu')
        self.conv2 = ConvBNLayer(
            in_channels=out_channels,
            out_channels=out_channels * 4,
            kernel_size=1,
            act=None)

        if not shortcut:
            self.short = ConvBNLayer(
                in_channels=in_channels,
                out_channels=out_channels * 4,
                kernel_size=1,
                stride=1,
                is_vd_mode=False if if_first else True)

        self.shortcut = shortcut
        
        self.relu1 = nn.ReLU(inplace=True)
        self.relu2 = nn.ReLU(inplace=True)
        self.relu3 = nn.ReLU(inplace=True)

    def forward(self, inputs):
        y = self.conv0(inputs)
        y = self.relu1(y)
        conv1 = self.conv1(y)
        conv1 = self.relu2(conv1)
        conv2 = self.conv2(conv1)

        if self.shortcut:
            short = inputs
        else:
            short = self.short(inputs)
        y = torch.add(short, conv2)
        y = self.relu3(y)
        return y


class BasicBlock(nn.Module):
    def __init__(self,
                 in_channels,
                 out_channels,
                 stride,
                 shortcut=True,
                 if_first=False):
        super(BasicBlock, self).__init__()
        self.stride = stride
        self.conv0 = ConvBNLayer(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=3,
            stride=stride,
            act='relu')
        self.conv1 = ConvBNLayer(
            in_channels=out_channels,
            out_channels=out_channels,
            kernel_size=3,
            act=None)

        if not shortcut:
            self.short = ConvBNLayer(
                in_channels=in_channels,
                out_channels=out_channels,
                kernel_size=1,
                stride=1,
                is_vd_mode=False if if_first else True,)

        self.shortcut = shortcut
        
        self.relu1 = nn.ReLU(inplace=True)
        self.relu2 = nn.ReLU(inplace=True)

    def forward(self, inputs):
        y = self.conv0(inputs)
        y = self.relu1(y)
        conv1 = self.conv1(y)

        if self.shortcut:
            short = inputs
        else:
            short = self.short(inputs)
        y = torch.add(short, conv1)
        y = self.relu2(y)
        return y


class ResNet_SAST(nn.Module):
    def __init__(self, in_channels=3, layers=50, **kwargs):
        super(ResNet_SAST, self).__init__()

        self.layers = layers
        supported_layers = [18, 34, 50, 101, 152, 200]
        assert layers in supported_layers, \
            "supported layers are {} but input layer is {}".format(
                supported_layers, layers)

        if layers == 18:
            depth = [2, 2, 2, 2]
        elif layers == 34 or layers == 50:
            # depth = [3, 4, 6, 3]
            depth = [3, 4, 6, 3, 3]
        elif layers == 101:
            depth = [3, 4, 23, 3]
        elif layers == 152:
            depth = [3, 8, 36, 3]
        elif layers == 200:
            depth = [3, 12, 48, 3]
        # num_channels = [64, 256, 512,
        #                 1024] if layers >= 50 else [64, 64, 128, 256]
        # num_filters = [64, 128, 256, 512]
        num_channels = [64, 256, 512,
                        1024, 2048] if layers >= 50 else [64, 64, 128, 256]
        num_filters = [64, 128, 256, 512, 512]

        self.conv1_1 = ConvBNLayer(
            in_channels=in_channels,
            out_channels=32,
            kernel_size=3,
            stride=2,
            act='relu')
        self.conv1_2 = ConvBNLayer(
            in_channels=32,
            out_channels=32,
            kernel_size=3,
            stride=1,
            act='relu')
        self.conv1_3 = ConvBNLayer(
            in_channels=32,
            out_channels=64,
            kernel_size=3,
            stride=1,
            act='relu')
        self.pool2d_max = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

        self.stages = []
        self.out_channels = [3, 64]
        if layers >= 50:
            for block in range(len(depth)):
                block_list = []
                shortcut = False
                for i in range(depth[block]):
                    bottleneck_block = BottleneckBlock(
                            in_channels=num_channels[block]
                            if i == 0 else num_filters[block] * 4,
                            out_channels=num_filters[block],
                            stride=2 if i == 0 and block != 0 else 1,
                            shortcut=shortcut,
                            if_first=block == i == 0)
                    self.add_module(
                        'bb_%d_%d' % (block, i), bottleneck_block)
                    shortcut = True
                    block_list.append(bottleneck_block)
                self.out_channels.append(num_filters[block] * 4)
                self.stages.append(nn.Sequential(*block_list))
        else:
            for block in range(len(depth)):
                block_list = []
                shortcut = False
                for i in range(depth[block]):
                    basic_block = BasicBlock(
                            in_channels=num_channels[block]
                            if i == 0 else num_filters[block],
                            out_channels=num_filters[block],
                            stride=2 if i == 0 and block != 0 else 1,
                            shortcut=shortcut,
                            if_first=block == i == 0)
                    self.add_module(
                        'bb_%d_%d' % (block, i),
                         basic_block)
                    shortcut = True
                    block_list.append(basic_block)
                self.out_channels.append(num_filters[block])
                self.stages.append(nn.Sequential(*block_list))

    def forward(self, inputs):
        out = [inputs]
        y = self.conv1_1(inputs)
        y = self.conv1_2(y)
        y = self.conv1_3(y)
        out.append(y)
        y = self.pool2d_max(y)
        for block in self.stages:
            y = block(y)
            out.append(y)
        return out