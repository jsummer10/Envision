'''
Application : Envision
File name   : defaultscene.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : This file is used to create default scenes
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

from xml.dom import minidom 
import os, logging

from src.config.settings import config, settings
from src.model import Model

class DefaultScene:
    """ This class is used to create default scenes """

    def __init__(self):
        self.root  = config.root
        self.world = config.world

        self.model = Model()

        self.SelectScene()

    def SelectScene(self):
        """ This is the controller for which scene will be used """

        scene = settings['DefaultScene']

        if scene == 'interchange_empty':
            self.model.AddModel(model='cloverleaf_interchange')
        elif scene == 'interchange_vehicles':
            self.InterchangeVehicles()
        elif scene == 'mcity':
            self.McityModels()
            
        else:
            pass

    def InterchangeVehicles(self):
        """ A scene containing cars on the interchange """ 

        self.model.AddModel(model='sun')
        self.model.AddModel(model='cloverleaf_interchange')
        self.model.AddModel(model='ambulance', name='default_ambulance1', pose='8.52 -35.51 6 0 0 3.1', static='false')
        self.model.AddModel(model='bus', name='default_bus1', pose='7.85 -13.17 5.50 0 0 3.13', static='false')
        self.model.AddModel(model='suv', name='default_suv1', pose='-8.04 -10.92 6 0 0 -1.523', static='false')
        self.model.AddModel(model='prius_hybrid', name='default_prius1', pose='4.99 7.01 6 0 0 3.12', static='false')
        self.model.AddModel(model='prius_hybrid', name='default_prius2', pose='-4.7 -27.82 6 0 0 0.0513', static='false')
        self.model.AddModel(model='hatchback_red', name='default_hatchback_red1', pose='-4.66 9.37 6 0 0 -1.523', static='false')


    def McityModels(self):
        """ A scene containing mcity """ 
        self.model.AddModel(model='sun')
        self.model.AddModel(model='mcity')


