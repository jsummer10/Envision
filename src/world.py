'''
Application : Envision
File name   : world.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : This file contains the main node of the .world file
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
from pathlib import Path
import os, sys, logging

from src.config.settings import settings, config

from src.nodehandler    import node_handler
from src.model          import Model
from src.defaultscene   import DefaultScene
  
class World:
    """ This class is the top level for the world file creation """ 

    def __init__(self, world_name):
        self.world_name = world_name
        self.CreateXML()
        self.Nodes()
        self.Scene()
        self.Models()
        self.FormatXML()
        self.SaveWorld()
        
    def CreateXML(self):
        """ Creates the world (XML) file """

        logging.info('Creating World File')

        self.root = minidom.Document() 
        sdf = self.root.createElement('sdf') 
        sdf.setAttribute('version', '1.7')
        self.root.appendChild(sdf) 
          
        self.world = self.root.createElement('world') 
        self.world.setAttribute('name', 'default')
        sdf.appendChild(self.world) 

        # Set the global variables
        config.root  = self.root
        config.world = self.world

    def Nodes(self):
        """ Add the top level nodes """

        logging.info('')
        logging.info('')
        logging.info('--- Adding Top Level Nodes ---')

        #node_handler.Light()
        node_handler.Gui()
        node_handler.Physics()
        node_handler.Scene()
        node_handler.Coordinates()

    def Scene(self):
        """ Setup the user requested default scene """

        logging.info('')
        logging.info('')
        logging.info('--- Setting Default Scene ---')

        DefaultScene()

    def Models(self):
        """ Add the user requested models """

        logging.info('')
        logging.info('')
        logging.info('--- Adding Requested Models ---')

        model = Model()

        for user_model in settings['Models']:
            if 'pose' in user_model.keys() and 'name' in user_model.keys():
                model.AddModel(model=user_model['model'], pose=user_model['pose'], name=user_model['name'])
            elif 'pose' in user_model.keys():
                model.AddModel(model=user_model['model'], pose=user_model['pose'])
            elif 'name' in user_model.keys():
                model.AddModel(model=user_model['model'], name=user_model['name'])
            else:
                model.AddModel(model=user_model['model'])

    def FormatXML(self):
        """ Format the world file output """
        self.xml_str = self.root.toprettyxml(indent ="\t", newl="\n")  
  
    def SaveWorld(self):
        """ Save the world file """

        logging.info('')
        logging.info('')
        logging.info('Saving World file')

        absPath = Path(__file__).parent.parent
        with open(str(absPath) +'/worlds/' + self.world_name, "w") as f: 
            f.write(self.xml_str)  


if __name__ == '__main__':

    env_world = World('test.world')