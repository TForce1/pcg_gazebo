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

from ...parsers.sdf import create_sdf_element
from ...parsers.sdf.format import Format


class Image(object):
    def __init__(self, image_width=100, image_height=100, image_format="R8G8B8"):
        assert image_format in Format._VALUE_OPTIONS, \
            f'Invalid image format type: {image_format}, options=' + str(Format._VALUE_OPTIONS)
        assert isinstance(image_height, int), 'Image height must be an integer'
        assert image_height > 0, 'Image height must be greater than zero'
        assert isinstance(image_width, int), 'Image width must be an integer'
        assert image_width > 0, 'Image width must be greater than zero'

        self._width = image_width
        self._height = image_height
        self._format = image_format

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, float):
            value = int(value)
        assert isinstance(value, int), 'Image height must be an integer'
        assert value > 0, 'Image height must be greater than zero'
        self._height = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, float):
            value = int(value)
        assert isinstance(value, int), 'Image width must be an integer'
        assert value > 0, 'Image width must be greater than zero'
        self._width = value

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        assert value in Format._VALUE_OPTIONS, \
            f'Invalid image format type: {image_format}, options=' + str(Format._VALUE_OPTIONS)
        self._format = value

    def to_sdf(self):
        sdf = create_sdf_element('image')
        sdf.width = self._width
        sdf.height = self._height
        sdf.format = self._format
        return sdf

    @staticmethod
    def from_sdf(sdf):
        image = Image()
        if sdf.height is not None:
            image.height = sdf.height.value
        if sdf.width is not None:
            image.width = sdf.width.value
        if sdf.format is not None:
            image.format = sdf.format.value
        return image
