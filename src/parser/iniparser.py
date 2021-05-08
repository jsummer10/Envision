'''
Application : Envision
File name   : iniparser.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : This file parses the ini input file
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

import logging, configparser
from src.config.settings import settings
from src.parser import validate

def ReadFile(filename):
    """ 
    Summary     : This functions reads in the ini file that will be 
                  used to generate the scenario
    Parameters  : input filename
    Return      : None
    """

    logging.info('')
    logging.info('')
    logging.info('Opening ' + filename)

    print('\nParsing input file (ini)')

    model_data = []

    config = configparser.ConfigParser()
    config.read(filename)

    sections = config.sections()

    for header in sections:

        data = {}

        # Parse default scene
        if 'defaults' in header.lower():
            if 'scene' in config[header]:
                scene_desc = config[header]['scene'].strip()
                if not validate.VerifyScene(scene_desc): continue
                
                settings['DefaultScene'] = scene_desc
                logging.info('Default scene: ' + settings['DefaultScene'])

        # Parse models for model, pose, name
        if 'model' in header.lower(): 

            model_present, model = validate.ModelMatch(config[header])
            pose_present,  pose  = validate.PoseMatch(config[header])
            name_present,  name  = validate.NameMatch(config[header])

            # Model
            if model_present:
                model_desc = config[header][model].strip()
                if not validate.VerifyModel(model_desc): continue
                data['model'] = config[header][model]

            else:
                logging.error('No model specified: ' + header) 
                continue

            # Pose
            if pose_present:
                pose_desc = config[header][pose].strip().replace(', ', ' ')
                if not validate.VerifyPose(pose_desc): continue
                data['pose'] = pose_desc

            # Name
            if name_present:
                name_desc = config[header][name].strip()
                data['name'] = name_desc

        if data == {}:
            continue

        model_data.append(data.copy())

        logging.info(data)

    settings['Models'] = model_data   

    logging.info('Closing ' + filename)
    logging.info('')
    logging.info('')

   
