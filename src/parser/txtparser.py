'''
Application : Envision
File name   : txtparser.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : This file parses the txt input file
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

import logging
from src.config.settings import settings
from src.parser          import validate

def ReadFile(filename):
    """ 
    Summary     : This functions reads in the text file that will be 
                  used to generate the scenario
    Parameters  : input filename
    Return      : None
    """

    logging.info('')
    logging.info('')
    logging.info('Opening ' + filename)

    print('\nParsing input file (txt)')

    model_data = []
    data = {}

    try:
        file = open(filename, "r")
    except Exception as e:
        print("Unable to open " + filename)
        logging.critical(e)
        sys.exit()

    file_data = file.readlines()

    for line in file_data:
        if (line == '\n' or line[0:2] == '//'):
            continue
        line = line.strip()
        line = line.replace(', ', ' ')
        # Parse default scene
        if 'default:' in line:
            scene = line.split(':')[1].strip().lower()
            if not validate.VerifyScene(scene): continue
            settings['DefaultScene'] = scene
            logging.info('Default scene: ' + settings['DefaultScene'])

        # Parse models for model, pose, name

        elif validate.LineModel(line):

            data_cur = {}
            
            for item in line.split(';'):
                (key, val) = item.split(':')
                data[key.strip()] = val.strip()
           
            model_present, model = validate.ModelMatch(data.keys())
            pose_present,  pose  = validate.PoseMatch(data.keys())
            name_present,  name  = validate.NameMatch(data.keys())

            # Model
            if model_present:
                if not validate.VerifyModel(data[model]): continue
                data_cur['model'] = data[model]
            else:
                logging.error('No model specified: ' + line) 
                continue
            
            # Pose
            if pose_present:
                if not validate.VerifyPose(data[pose]): continue
                data_cur['pose'] = data[pose]

            # Name
            if name_present:
                data_cur['name'] = data[name]

            model_data.append(data_cur.copy())

            logging.info(data)

        



    settings['Models'] = model_data     

    #----------------------
    #   Close Input File   
    #----------------------

    logging.info('Closing ' + filename)
    logging.info('')
    logging.info('')
    file.close()
