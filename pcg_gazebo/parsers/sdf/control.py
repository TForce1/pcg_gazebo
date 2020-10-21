# Copyright (c) 2019 - The Procedural Generation for Gazebo authors
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
from ...utils import is_string
from .type import Type
from .offset import offset
from .p_gain import p_gain
from .i_gain import i_gain
from .d_gain import d_gain
from .i_max import i_max
from .i_min import i_min
from .cmd_max import cmd_max
from .cmd_min import cmd_min
from .joint_name import joint_name
from .multiplier import multiplier
from .controlVelocitySlowdownSim import controlVelocitySlowdownSim


class Control(XMLBase):
    _NAME = 'control'
    _TYPE = 'sdf'

    _ATTRIBUTES = dict(
        channel='',
    )

    _CHILDREN_CREATORS = dict(
        type=dict(creator=Type, optional=True),
        offset=dict(creator=offset, optional=True),
        p_gain=dict(creator=p_gain, optional=True),
        i_gain=dict(creator=i_gain, optional=True),
        d_gain=dict(creator=d_gain, optional=True),
        i_max=dict(creator=i_max, optional=True),
        i_min=dict(creator=i_min, optional=True),
        cmd_max=dict(creator=cmd_max, optional=True),
        cmd_min=dict(creator=cmd_min, optional=True),
        jointName=dict(creator=joint_name, optional=True),
        multiplier=dict(creator=multiplier, optional=True),
        controlVelocitySlowdownSim=dict(creator=controlVelocitySlowdownSim,
                                        optional=True),
    )

    def __init__(self):
        super(Control, self).__init__()
        self.reset()
        self._value = None
        self._has_custom_elements = True

    @property
    def channel(self):
        return self.attributes['channel']

    @channel.setter
    def channel(self, value):
        assert isinstance(value, int), 'control channel must be an integer'
        self.attributes['channel'] = value

    @property
    def type(self):
        return self._get_child_element('type')

    @type.setter
    def type(self, value):
        self._add_child_element('type', value)

    @property
    def offset(self):
        return self._get_child_element('offset')

    @offset.setter
    def offset(self, value):
        self._add_child_element('offset', value)

    @property
    def p_gain(self):
        return self._get_child_element('p_gain')

    @p_gain.setter
    def p_gain(self, value):
        self._add_child_element('p_gain', value)

    @property
    def i_gain(self):
        return self._get_child_element('i_gain')

    @i_gain.setter
    def i_gain(self, value):
        self._add_child_element('i_gain', value)

    @property
    def d_gain(self):
        return self._get_child_element('d_gain')

    @d_gain.setter
    def d_gain(self, value):
        self._add_child_element('d_gain', value)

    @property
    def i_max(self):
        return self._get_child_element('i_max')

    @i_max.setter
    def i_max(self, value):
        self._add_child_element('i_max', value)

    @property
    def i_min(self):
        return self._get_child_element('i_min')

    @i_min.setter
    def i_min(self, value):
        self._add_child_element('i_min', value)

    @property
    def cmd_max(self):
        return self._get_child_element('cmd_max')

    @cmd_max.setter
    def cmd_max(self, value):
        self._add_child_element('cmd_max', value)

    @property
    def cmd_min(self):
        return self._get_child_element('cmd_min')

    @cmd_min.setter
    def cmd_min(self, value):
        self._add_child_element('cmd_min', value)

    @property
    def jointName(self):
        return self._get_child_element('jointName')

    @jointName.setter
    def jointName(self, value):
        self._add_child_element('jointName', value)

    @property
    def multiplier(self):
        return self._get_child_element('multiplier')

    @multiplier.setter
    def multiplier(self, value):
        self._add_child_element('multiplier', value)

    @property
    def controlVelocitySlowdownSim(self):
        return self._get_child_element('controlVelocitySlowdownSim')

    @controlVelocitySlowdownSim.setter
    def controlVelocitySlowdownSim(self, value):
        self._add_child_element('controlVelocitySlowdownSim', value)

