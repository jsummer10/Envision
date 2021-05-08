'''
Application : Envision
File name   : validate.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : This file is for input validation
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

def VerifyPose(pose):
    """ 
    Summary    : This functions tests the pose input to verify all values
                 are integers
    Parameters : scene to verify
    Return     : Boolean
    """

    for value in pose.split():
        try: 
            float(value)
        except: 
            print('Something other than a number detected: ' + pose)
            logging.error('Something other than a number detected: ' + pose)
            return False
    
    return True

def VerifyModel(model):
    """ 
    Summary    : This functions tests the model input to verify that it 
                 is supported by Envision
    Parameters : scene to verify
    Return     : Boolean
    """
    
    if model in settings.SupportedModels():
        return True
    else:
        print(model + ' is not supported')
        logging.error(model + ' is not supported')
        return False

def VerifyScene(scene):
    """ 
    Summary    : This functions tests the scene input to verify that it 
                 is supported by Envision
    Parameters : scene to verify
    Return     : Boolean
    """
    
    if scene.lower() in settings.SupportedScenes():
        return True
    else:
        print(scene + ' is not supported')
        logging.error(scene + ' is not supported')
        return False

def ModelMatch(comp):
    """ 
    Summary    : This functions compares a list to model with
                 typo handling
    Parameters : comparison list
    Return     : Boolean
    """

    for item in comp:
        try:
            item = item.lower()
        except:
            continue

        if item == 'model':
            return True, item

        if item == 'pose' or item == 'name':
            continue

        char_match = 0

        if 'm' in item: char_match += 1
        if 'o' in item: char_match += 1
        if 'd' in item: char_match += 1
        if 'e' in item: char_match += 1
        if 'l' in item: char_match += 1

        if char_match >= 4:
            return True, item
        else:
            continue

    return False, None

def PoseMatch(comp):
    """ 
    Summary    : This functions compares a list to pose with
                 typo handling
    Parameters : comparison list
    Return     : Boolean
    """

    for item in comp:
        try:
            item = item.lower()
        except:
            continue

        if item == 'pose':
            return True, item

        if item == 'model' or item == 'name':
            continue

        char_match = 0

        if 'p' in item: char_match += 1
        if 'o' in item: char_match += 1
        if 's' in item: char_match += 1
        if 'e' in item: char_match += 1

        if char_match >= 3:
            return True, item
        else: 
            continue

    return False, None

def NameMatch(comp):
    """ 
    Summary    : This functions compares a list to name with
                 typo handling
    Parameters : comparison list
    Return     : Boolean
    """

    for item in comp:
        try:
            item = item.lower()
        except:
            continue

        if item == 'name':
            return True, item

        if item == 'model' or item == 'pose':
            continue

        char_match = 0

        if 'n' in item: char_match += 1
        if 'a' in item: char_match += 1
        if 'm' in item: char_match += 1
        if 'e' in item: char_match += 1

        if char_match >= 3:
            return True, item
        else: 
            continue

    return False, None

def SceneMatch(comp):
    """ 
    Summary    : This functions compares a list to scene with
                 typo handling
    Parameters : comparison list
    Return     : Boolean
    """

    for item in comp:
        try:
            item = item.lower()
        except:
            continue

        if item == 'scene':
            return True, item

        char_match = 0

        if 's' in item: char_match += 1
        if 'c' in item: char_match += 1
        if 'e' in item: char_match += 1
        if 'n' in item: char_match += 1
        if 'e' in item: char_match += 1

        if char_match >= 4:
            return True, item
        else: 
            continue

    return False, None

def LineModel(line):
    """ 
    Summary    : This functions compares a string to model with
                 typo handling
    Parameters : comparison string
    Return     : Boolean
    """

    try:
        line = line.lower()
    except:
        return False

    if 'default:' in line:
        return False

    if 'model' in line:
        return True

    char_match = 0

    if 'm' in line: char_match += 1
    if 'o' in line: char_match += 1
    if 'd' in line: char_match += 1
    if 'e' in line: char_match += 1
    if 'l' in line: char_match += 1

    if char_match >= 4:
        return True

    return False