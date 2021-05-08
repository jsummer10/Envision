'''
Application : Envision
File name   : light.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : This file contains the light node
'''

# Copyright (c) April 26, 2021 Jacob Summerville and Safwan Elmadani
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os, logging  
from xml.dom import minidom 
from src.node.node import Node
  
class Light(Node):
    def __init__(self):
        Node.__init__(self)

        logging.info('Top Level Node Creation -> Light')

        self.light = self.root.createElement('light') 
        self.light.setAttribute('name', 'sun') 
        self.light.setAttribute('type', 'directional') 

        self.CastShadows()
        self.Pose()
        self.Diffuse()
        self.Specular()
        self.Attenuation()
        self.Direction()
        self.Spot()

        self.world.appendChild(self.light) 

    def CastShadows(self):
        self.TextTag(self.light, 'cast_shadows', '1') 

    def Pose(self):
        self.TextTag(self.light, 'pose', '0 0 10 0 -0 0') 

    def Diffuse(self):
        self.TextTag(self.light, 'diffuse', '0.8 0.8 0.8 1') 

    def Specular(self):
        self.TextTag(self.light, 'specular', '0.2 0.2 0.2 1') 

    def Attenuation(self):
        attenuation = self.root.createElement('attenuation')
        self.TextTag(attenuation, 'range', '1000')
        self.TextTag(attenuation, 'constant', '0.9')
        self.TextTag(attenuation, 'linear', '0.01')
        self.TextTag(attenuation, 'quadratic', '0.001')
        self.light.appendChild(attenuation) 

    def Direction(self):
        self.TextTag(self.light, 'direction', '-0.5 0.1 -0.9') 

    def Spot(self):
        spot = self.root.createElement('spot')
        self.TextTag(spot, 'inner_angle', '0')
        self.TextTag(spot, 'outer_angle', '0')
        self.TextTag(spot, 'falloff', '0')
        self.light.appendChild(spot) 

