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
from .control import Control
from .always_On import AlwaysOn
from .update_rate import UpdateRate
from .topic import Topic
from .noise import Noise
from .xyzOffset import xyzOffset
from .xyzOffsets import XyzOffsets
from .rpyOffset import RpyOffset
from .rpyOffsets import RpyOffsets
from .name import Name
from .frame_name import FrameName
from .body_name import BodyName
from .link_name import LinkName
from .fdm_addr import FdmAddr
from .imu_name import ImuName
from .prefix import Prefix
from .color_optical_frame_name import ColorOpticalFrameName
from .depth_optical_frame_name import DepthOpticalFrameName
from .infrared1_optical_frame_name import Infrared1OpticalFrameName
from .infrared2_optical_frame_name import Infrared2OpticalFrameName
from .a0 import a0
from .alpha_stall import alpha_stall
from .cla import cla
from .cda import cda
from .cma import cma
from .cla_stall import cla_stall
from .cda_stall import cda_stall
from .cma_stall import cma_stall
from .area import area
from .air_density import air_density
from .range_min_depth import rangeMinDepth
from .range_max_depth import rangeMaxDepth
from .point_cloud import pointCloud
from .pointCloudTopicName import pointCloudTopicName
from .point_cloud_cutoff import pointCloudCutoff
from .initialOrientationAsReference import initialOrientationAsReference
from .fdm_port_in import fdm_port_in
from .fdm_port_out import fdm_port_out
from .connectionTimeoutMaxCount import connectionTimeoutMaxCount
from .cp import cp
from .forward import forward
from .upward import upward
from .topicName import topicName
from .gaussian_noise import gaussianNoise
from .depthTopicName import depthTopicName
from .depthCameraInfoTopicName import depthCameraInfoTopicName
from .colorTopicName import colorTopicName
from .colorCameraInfoTopicName import colorCameraInfoTopicName
from .infrared1TopicName import infrared1TopicName
from .infrared1CameraInfoTopicName import infrared1CameraInfoTopicName
from .infrared2TopicName import infrared2TopicName
from .infrared2CameraInfoTopicName import infrared2CameraInfoTopicName
from .updateRate import updateRate
from .updateRateHZ import updateRateHZ
from .depthUpdateRate import depthUpdateRate
from .colorUpdateRate import colorUpdateRate
from .infraredUpdateRate import infraredUpdateRate
from .modelXYZToAirplaneXForwardZDown import modelXYZToAirplaneXForwardZDown
from .gazeboXYZToNED import gazeboXYZToNED


class Plugin(XMLBase):
    _NAME = 'plugin'
    _TYPE = 'sdf'

    _ATTRIBUTES = dict(
        name='',
        filename=''
    )

    _CHILDREN_CREATORS = dict(
        control=dict(creator=Control, n_elems='+', optional=True),
        alwaysOn=dict(creator=AlwaysOn, optional=True),
        updateRate=dict(creator=updateRate, optional=True),
        updateRateHZ=dict(creator=updateRateHZ, optional=True),
        bodyName=dict(creator=BodyName, optional=True),
        topicName=dict(creator=topicName, optional=True),
        gaussianNoise=dict(creator=gaussianNoise, optional=True),
        frameName=dict(creator=FrameName, optional=True),
        xyzOffsets=dict(creator=XyzOffsets, optional=True),
        xyzOffset=dict(creator=xyzOffset, optional=True),
        rpyOffsets=dict(creator=RpyOffsets, optional=True),
        rpyOffset=dict(creator=RpyOffset, optional=True),
        a0=dict(creator=a0, optional=True),
        alpha_stall=dict(creator=alpha_stall, optional=True),
        cla=dict(creator=cla, optional=True),
        cda=dict(creator=cda, optional=True),
        cma=dict(creator=cma, optional=True),
        cla_stall=dict(creator=cla_stall, optional=True),
        cda_stall=dict(creator=cda_stall, optional=True),
        cma_stall=dict(creator=cma_stall, optional=True),
        area=dict(creator=area, optional=True),
        air_density=dict(creator=air_density, optional=True),
        cp=dict(creator=cp, optional=True),
        forward=dict(creator=forward, optional=True),
        upward=dict(creator=upward, optional=True),
        link_name=dict(creator=LinkName, optional=True),
        fdm_addr=dict(creator=FdmAddr, optional=True),
        fdm_port_in=dict(creator=fdm_port_in, optional=True),
        fdm_port_out=dict(creator=fdm_port_out, optional=True),
        modelXYZToAirplaneXForwardZDown=dict(creator=modelXYZToAirplaneXForwardZDown, optional=True),
        gazeboXYZToNED=dict(creator=gazeboXYZToNED, optional=True),
        imuName=dict(creator=ImuName, optional=True),
        connectionTimeoutMaxCount=dict(creator=connectionTimeoutMaxCount, optional=True),
        initialOrientationAsReference=dict(creator=initialOrientationAsReference, optional=True),
        prefix=dict(creator=Prefix, optional=True),
        depthUpdateRate=dict(creator=depthUpdateRate, optional=True),
        colorUpdateRate=dict(creator=colorUpdateRate, optional=True),
        infraredUpdateRate=dict(creator=infraredUpdateRate, optional=True),
        depthTopicName=dict(creator=depthTopicName, optional=True),
        depthCameraInfoTopicName=dict(creator=depthCameraInfoTopicName, optional=True),
        colorTopicName=dict(creator=colorTopicName, optional=True),
        colorCameraInfoTopicName=dict(creator=colorCameraInfoTopicName, optional=True),
        infrared1TopicName=dict(creator=infrared1TopicName, optional=True),
        infrared1CameraInfoTopicName=dict(creator=infrared1CameraInfoTopicName, optional=True),
        infrared2TopicName=dict(creator=infrared2TopicName, optional=True),
        infrared2CameraInfoTopicName=dict(creator=infrared2CameraInfoTopicName, optional=True),
        colorOpticalframeName=dict(creator=ColorOpticalFrameName, optional=True),
        depthOpticalframeName=dict(creator=DepthOpticalFrameName, optional=True),
        infrared1OpticalframeName=dict(creator=Infrared1OpticalFrameName, optional=True),
        infrared2OpticalframeName=dict(creator=Infrared2OpticalFrameName, optional=True),
        rangeMinDepth=dict(creator=rangeMinDepth, optional=True),
        rangeMaxDepth=dict(creator=rangeMaxDepth, optional=True),
        pointCloud=dict(creator=pointCloud, optional=True),
        pointCloudTopicName=dict(creator=pointCloudTopicName, optional=True),
        pointCloudCutoff=dict(creator=pointCloudCutoff, optional=True),
    )

    def __init__(self, default=dict()):
        XMLBase.__init__(self)
        self._has_custom_elements = True
        self.reset()
        self._value = None

    @property
    def name(self):
        return self.attributes['name']

    @name.setter
    def name(self, value):
        assert isinstance(value, str), 'Plugin name must be a string'
        assert len(value) > 0, 'Plugin name cannot be empty'
        self.attributes['name'] = value

    @property
    def filename(self):
        return self.attributes['filename']

    @filename.setter
    def filename(self, value):
        assert isinstance(value, str), 'Plugin filename must be a string'
        assert len(value) > 0, 'Plugin filename cannot be empty'
        assert '.so' in value, 'Invalid plugin filename'
        self.attributes['filename'] = value

    @property
    def control(self):
        return self._get_child_element('control')

    @control.setter
    def control(self, value):
        self._add_child_element('control', value)

    @property
    def alwaysOn(self):
        return self._get_child_element('alwaysOn')
    
    @alwaysOn.setter
    def alwaysOn(self, value):
        self._add_child_element('alwaysOn', value) 
    
    @property
    def updateRate(self):
        return self._get_child_element('updateRate')
    
    @updateRate.setter
    def updateRate(self, value):
        self._add_child_element('updateRate', value) 
        
    @property
    def updateRateHZ(self):
        return self._get_child_element('updateRateHZ')
    
    @updateRateHZ.setter
    def updateRateHZ(self, value):
        self._add_child_element('updateRateHZ', value) 
        
    @property
    def bodyName(self):
        return self._get_child_element('bodyName')
    
    @bodyName.setter
    def bodyName(self, value):
        self._add_child_element('bodyName', value) 
        
    @property
    def topicName(self):
        return self._get_child_element('topicName')
    
    @topicName.setter
    def topicName(self, value):
        self._add_child_element('topicName', value)  
        
    @property
    def gaussianNoise(self):
        return self._get_child_element('gaussianNoise')

    @gaussianNoise.setter
    def gaussianNoise(self, value):
        self._add_child_element('gaussianNoise', value) 

    @property
    def frameName(self):
        return self._get_child_element('frameName')

    @frameName.setter
    def frameName(self, value):
        self._add_child_element('frameName', value)
        
    @property
    def xyzOffsets(self):
        return self._get_child_element('xyzOffsets')

    @xyzOffsets.setter
    def xyzOffsets(self, value):
        self._add_child_element('xyzOffsets', value)

    @property
    def xyzOffset(self):
        return self._get_child_element('xyzOffset')

    @xyzOffset.setter
    def xyzOffset(self, value):
        self._add_child_element('xyzOffset', value)

    @property
    def rpyOffsets(self):
        return self._get_child_element('rpyOffsets')

    @rpyOffsets.setter
    def rpyOffsets(self, value):
        self._add_child_element('rpyOffsets', value)

    @property
    def rpyOffset(self):
        return self._get_child_element('rpyOffset')

    @rpyOffset.setter
    def rpyOffset(self, value):
        self._add_child_element('rpyOffset', value)
        
    @property
    def a0(self):
        return self._get_child_element('a0')
    
    @a0.setter
    def a0(self, value):
        self._add_child_element('a0', value) 
        
    @property
    def alpha_stall(self):
        return self._get_child_element('alpha_stall')

    @alpha_stall.setter
    def alpha_stall(self, value):
        self._add_child_element('alpha_stall', value) 
        
    @property
    def cla(self):
        return self._get_child_element('cla')
    
    @cla.setter
    def cla(self, value):
        self._add_child_element('cla', value) 
        
    @property
    def cda(self):
        return self._get_child_element('cda')
    
    @cda.setter
    def cda(self, value):
        self._add_child_element('cda', value) 
        
    @property
    def cma(self):
        return self._get_child_element('cma')
    
    @cma.setter
    def cma(self, value):
        self._add_child_element('cma', value) 
        
    @property
    def cla_install(self):
        return self._get_child_element('cla_install')
        
    @cla_install.setter
    def cla_install(self, value):
        self._add_child_element('cla_install', value) 
        
    @property
    def cda_install(self):
        return self._get_child_element('cda_install')
        
    
    @cda_install.setter
    def cda_install(self, value):
        self._add_child_element('cda_install', value) 
        
    @property
    def cma_install(self):
        return self._get_child_element('cma_install')
    
    @cma_install.setter
    def cma_install(self, value):
        self._add_child_element('cma_install', value) 
        
    @property
    def area(self):
        return self._get_child_element('area')
    
    @area.setter
    def area(self, value):
        self._add_child_element('area', value)  
        
    @property
    def air_density(self):
        return self._get_child_element('air_density')
    
    @air_density.setter
    def air_density(self, value):
        self._add_child_element('air_density', value) 
        
    @property
    def cp(self):
        return self._get_child_element('cp')
    
    @cp.setter
    def cp(self, value):
        self._add_child_element('cp', value) 
        
    @property
    def forward(self):
        return self._get_child_element('forward')
        
    @forward.setter
    def forward(self, value):
        self._add_child_element('forward', value) 
        
    @property
    def upward(self):
        return self._get_child_element('upward')
        
    @upward.setter
    def upward(self, value):
        self._add_child_element('upward', value) 
        
    @property
    def link_name(self):
        return self._get_child_element('link_name')
        
    @link_name.setter
    def link_name(self, value):
        self._add_child_element('link_name', value) 
        
    @property
    def fdm_addr(self):
        return self._get_child_element('fdm_addr')
    
    @fdm_addr.setter
    def fdm_addr(self, value):
        self._add_child_element('fdm_addr', value) 
        
    @property
    def fdm_port_in(self):
        return self._get_child_element('fdm_port_in')
        
    @fdm_port_in.setter
    def fdm_port_in(self, value):
        self._add_child_element('fdm_port_in', value) 
        
    @property
    def fdm_port_out(self):
        return self._get_child_element('fdm_port_out')
        
    @fdm_port_out.setter
    def fdm_port_out(self, value):
        self._add_child_element('fdm_port_out', value) 
        
    @property
    def modelXYZToAirplaneXForwardZDown(self):
        return self._get_child_element('modelXYZToAirplaneXForwardZDown')

    @modelXYZToAirplaneXForwardZDown.setter
    def modelXYZToAirplaneXForwardZDown(self, value):
        self._add_child_element('modelXYZToAirplaneXForwardZDown', value) 
        
    @property
    def gazeboXYZToNED(self):
        return self._get_child_element('gazeboXYZToNED')

    @gazeboXYZToNED.setter
    def gazeboXYZToNED(self, value):
        self._add_child_element('gazeboXYZToNED', value) 

    @property
    def imuName(self):
        return self._get_child_element('imuName')

    @imuName.setter
    def imuName(self, value):
        self._add_child_element('imuName', value)

    @property
    def connectionTimeoutMaxCount(self):
        return self._get_child_element('connectionTimeoutMaxCount')

    @connectionTimeoutMaxCount.setter
    def connectionTimeoutMaxCount(self, value):
        self._add_child_element('connectionTimeoutMaxCount', value)

    @property
    def initialOrientationAsReference(self):
        return self._get_child_element('initialOrientationAsReference')


    @initialOrientationAsReference.setter
    def initialOrientationAsReference(self, value):
        self._add_child_element('initialOrientationAsReference', value)

    @property
    def prefix(self):
        return self._get_child_element('prefix')

    @prefix.setter
    def prefix(self, value):
        self._add_child_element('prefix', value)

    @property
    def depthUpdateRate(self):
        return self._get_child_element('depthUpdateRate')

    @depthUpdateRate.setter
    def depthUpdateRate(self, value):
        self._add_child_element('depthUpdateRate', value)

    @property
    def colorUpdateRate(self):
        return self._get_child_element('colorUpdateRate')

    @colorUpdateRate.setter
    def colorUpdateRate(self, value):
        self._add_child_element('colorUpdateRate', value)

    @property
    def infraredUpdateRate(self):
        return self._get_child_element('infraredUpdateRate')
        
    
    @infraredUpdateRate.setter
    def infraredUpdateRate(self, value):
        self._add_child_element('infraredUpdateRate', value) 

    @property
    def depthTopicName(self):
        return self._get_child_element('depthTopicName')


    @depthTopicName.setter
    def depthTopicName(self, value):
        self._add_child_element('depthTopicName', value)

    @property
    def depthCameraInfoTopicName(self):
        return self._get_child_element('depthCameraInfoTopicName')


    @depthCameraInfoTopicName.setter
    def depthCameraInfoTopicName(self, value):
        self._add_child_element('depthCameraInfoTopicName', value)

    @property
    def colorTopicName(self):
        return self._get_child_element('colorTopicName')
        
    
    @colorTopicName.setter
    def colorTopicName(self, value):
        self._add_child_element('colorTopicName', value) 

    @property
    def colorCameraInfoTopicName(self):
        return self._get_child_element('colorCameraInfoTopicName')
        
    
    @colorCameraInfoTopicName.setter
    def colorCameraInfoTopicName(self, value):
        self._add_child_element('colorCameraInfoTopicName', value) 

    @property
    def infrared1TopicName(self):
        return self._get_child_element('infrared1TopicName')


    @infrared1TopicName.setter
    def infrared1TopicName(self, value):
        self._add_child_element('infrared1TopicName', value)

    @property
    def infrared1CameraInfoTopicName(self):
        return self._get_child_element('infrared1CameraInfoTopicName')

    @infrared1CameraInfoTopicName.setter
    def infrared1CameraInfoTopicName(self, value):
        self._add_child_element('infrared1CameraInfoTopicName', value)

    @property
    def infrared2TopicName(self):
        return self._get_child_element('infrared2TopicName')

    @infrared2TopicName.setter
    def infrared2TopicName(self, value):
        self._add_child_element('infrared2TopicName', value)

    @property
    def infrared2CameraInfoTopicName(self):
        return self._get_child_element('infrared2CameraInfoTopicName')

    @infrared2CameraInfoTopicName.setter
    def infrared2CameraInfoTopicName(self, value):
        self._add_child_element('infrared2CameraInfoTopicName', value)

    @property
    def colorOpticalframeName(self):
        return self._get_child_element('colorOpticalframeName')
        
    @colorOpticalframeName.setter
    def colorOpticalframeName(self, value):
        self._add_child_element('colorOpticalframeName', value) 

    @property
    def depthOpticalframeName(self):
        return self._get_child_element('depthOpticalframeName')
    
    @depthOpticalframeName.setter
    def depthOpticalframeName(self, value):
        self._add_child_element('depthOpticalframeName', value) 

    @property
    def infrared1OpticalframeName(self):
        return self._get_child_element('infrared1OpticalframeName')
        
    @infrared1OpticalframeName.setter
    def infrared1OpticalframeName(self, value):
        self._add_child_element('infrared1OpticalframeName', value) 

    @property
    def infrared2OpticalframeName(self):
        return self._get_child_element('infrared2OpticalframeName')
        
    @infrared2OpticalframeName.setter
    def infrared2OpticalframeName(self, value):
        self._add_child_element('infrared2OpticalframeName', value) 

    @property
    def rangeMinDepth(self):
        return self._get_child_element('rangeMinDepth')

    @rangeMinDepth.setter
    def rangeMinDepth(self, value):
        self._add_child_element('rangeMinDepth', value)

    @property
    def rangeMaxDepth(self):
        return self._get_child_element('rangeMaxDepth')

    @rangeMaxDepth.setter
    def rangeMaxDepth(self, value):
        self._add_child_element('rangeMaxDepth', value)

    @property
    def pointCloud(self):
        return self._get_child_element('pointCloud')

    @pointCloud.setter
    def pointCloud(self, value):
        self._add_child_element('pointCloud', value)

    @property
    def pointCloudTopicName(self):
        return self._get_child_element('pointCloudTopicName')

    @pointCloudTopicName.setter
    def pointCloudTopicName(self, value):
        self._add_child_element('pointCloudTopicName', value)

    @property
    def pointCloudCutoff(self):
        return self._get_child_element('pointCloudCutoff')

    @pointCloudCutoff.setter
    def pointCloudCutoff(self, value):
        self._add_child_element('pointCloudCutoff', value)

    @staticmethod
    def gazebo_ros_control(name='gazebo_ros_control', robot_namespace='',
                           control_period=None,
                           robot_param='/robot_description',
                           robot_sim_type=None):
        obj = Plugin()
        obj.name = name
        obj.filename = 'libgazebo_ros_control.so'

        params = dict()
        params['robotNamespace'] = robot_namespace
        if control_period is not None:
            assert isinstance(control_period, float) or isinstance(
                control_period, int), 'Control period must be numeric'
            assert control_period > 0, \
                'Control period must be a positive number'
            params['controlPeriod'] = control_period
        params['robotParam'] = robot_param
        if robot_sim_type is not None:
            params['robotSimType'] = robot_sim_type
        obj.value = params
        return obj

    @staticmethod
    def gazebo_ros_bumper(name='gazebo_ros_bumper', robot_namespace='',
                          bumper_topic_name='bumper_states',
                          frame_name='world'):
        obj = Plugin()
        obj.name = name
        obj.filename = 'libgazebo_ros_bumper.so'

        params = dict()
        params['robotNamespace'] = robot_namespace
        params['bumperTopicName'] = bumper_topic_name
        params['frameName'] = frame_name
        obj.value = params
        return obj

    @staticmethod
    def gazebo_ros_ft_sensor(name='gazebo_ros_ft_sensor', robot_namespace='',
                             joint_name=None, topic_name=None,
                             gaussian_noise=0, update_rate=0):
        assert topic_name is not None, 'Topic name is missing'
        assert joint_name is not None, 'Joint name is missing'
        obj = Plugin()
        obj.name = name
        obj.filename = 'libgazebo_ros_ft_sensor.so'

        params = dict()
        params['robotNamespace'] = robot_namespace
        params['topicName'] = topic_name
        params['jointName'] = joint_name
        params['gaussianNoise'] = gaussian_noise
        params['updateRate'] = update_rate
        obj.value = params
        return obj

    @staticmethod
    def gazebo_ros_p3d(name='gazebo_ros_p3d', robot_namespace='',
                       body_name=None, topic_name=None, frame_name='world',
                       xyz_offset=[0, 0, 0], rpy_offset=[0, 0, 0],
                       gaussian_noise=0, update_rate=0):
        assert topic_name is not None, 'Topic name is missing'
        assert body_name is not None, 'Body name is missing'

        obj = Plugin()
        obj.name = name
        obj.filename = 'libgazebo_ros_p3d.so'

        params = dict()
        params['robotNamespace'] = robot_namespace
        params['topicName'] = topic_name
        params['bodyName'] = body_name
        params['frameName'] = frame_name
        params['xyzOffset'] = xyz_offset
        params['rpyOffset'] = rpy_offset
        params['gaussianNoise'] = gaussian_noise
        params['updateRate'] = update_rate
        obj.value = params
        return obj
