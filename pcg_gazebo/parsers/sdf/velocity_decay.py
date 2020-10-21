# Copyright (c) 2020 - The Procedural Generation for Gazebo authors
# For information on the respective copyright owner see the NOTICE file
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
from ..types import XMLBase
from .linear import Linear
from .angular import Angular


class velocity_decay(XMLBase):
    _NAME = 'velocity_decay'
    _TYPE = 'sdf'

    _CHILDREN_CREATORS = dict(
        linear=dict(creator=Linear, optional=True),
        angular=dict(creator=Angular, optional=True),
    )

    def __init__(self):
        super().__init__()
        self.reset()

    @property
    def linear(self):
        return self._get_child_element('linear')

    @linear.setter
    def linear(self, value):
        self._add_child_element('linear', value)

    @property
    def angular(self):
        return self._get_child_element('angular')

    @angular.setter
    def angular(self, value):
        self._add_child_element('angular', value)
