'''
Application : Envision
File name   : settings.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : The settings class is a dictionary that will contain 
              the user specified settings from the input file
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

class Settings(dict):
    """ This class contains user specified settings from the input file """ 
    def __init__(self):
        self.settings = { 'DefaultScene' : str(), 
                          'Models'       : str(), 
                        }

    def __getitem__(self, key):
        return self.settings[key]

    def __setitem__(self, key, value):
        if key not in self.settings.keys():
            print("\nKeyError: '{}' does not exist in settings".format(key))
            print('The following keys exist:')
            print('\tDefaultScene')
            print('\tModels')

            sys.exit()

        self.settings[key] = value

    def SupportedModels(self):
        
        vehicles = ['ambulance', 'bus', 'fire_truck', 'hatchback', 'hatchback_blue', 'hatchback_red', 
                    'pickup', 'polaris_ranger_ev', 'prius_hybrid', 'prius_hybrid_sensors', 'suv']

        pedestrians = ['person_standing', 'person_walking']

        buildings = ['apartment', 'fast_food', 'fire_station', 'gas_station', 'grocery_store',
                     'house_1', 'house_2', 'house_3', 'law_office', 'osrf_first_office',
                     'parking_garage', 'police_station', 'post_office', 'powerplant', 'salon', 
                     'school', 'thrift_shop']

        tcs = ['stop_light', 'stop_light_post', 'stop_sign', 'speed_limit_sign']

        vegetation = ['oak_tree', 'pine_tree']

        planes = ['asphalt_plane', 'robocup_3Dsim_field', 'ground_plane']

        misc = ['cafe_table', 'cardboard_box', 'cinder_block', 'cinder_block_2', 'construction_barrel', 
                'construction_cone', 'dumpster', 'fire_hydrant', 'fountain', 'jersey_barrier', 
                'lamp_post', 'playground', 'postbox', 'radio_tower', 'reactor', 'simple_arm', 
                'telephone_pole', 'tower_crane']

        drc = ['drc_practice_angled_barrier_45', 'drc_practice_blue_cylinder', 
               'drc_practice_orange_jersey_barrier', 'drc_practice_white_jersey_barrier']

        other = ['collapsed_industrial', 'pier', 'submarine', 'sun', 'truss_bridge']

        models = []
        models += vehicles
        models += pedestrians
        models += buildings
        models += tcs
        models += vegetation
        models += planes
        models += misc
        models += drc
        models += other

        return models
    
    def SupportedScenes(self):
        scenes = ['interchange_empty', 'interchange_vehicles', 'mcity']

        return scenes

    # def KeyWords (self):
    #     words = ['model', 'pose', 'ref']
    #     return words

settings = Settings()

class GlobalConfig():
    """ This class contains global variables """
    def __init__(self):
        self.root  = None
        self.world = None

config = GlobalConfig()