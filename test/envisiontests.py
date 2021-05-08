'''
Application : Envision
File name   : envisiontests.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : This file tests performs unit tests on evision
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

import unittest, sys, os, time, subprocess, HtmlTestRunner

sys.path.append(os.getcwd())

from src.config.settings    import settings
from src.world              import World
from src.parser             import txtparser, iniparser
from inputfile              import InputFile

class EnvisionTests(unittest.TestCase): 
   
    def test_1_world_output(self): 
        """ Description: Verification of .world file """

        settings['DefaultScene'] = 'Scene 1'

        env_world = World('test_world_output.world')

        if os.path.isfile('worlds/test_world_output.world'):
            os.remove("worlds/test_world_output.world")
        else:
            self.fail('.world file was not created') 

    def test_2_input_parser_txt(self):
        """ Description: Input file (txt) parser validation """

        input_file = InputFile('txt')

        input_file.AddLine('default: interchange_empty')
        input_file.AddLine('model: ambulance; pose: 10, 5, 0, 0, 0, 0')
        input_file.AddLine('model: ambulance; pose: 20, 5, 0, 1, 2, 0; name: amb2')

        txtparser.ReadFile(input_file.test_file)


        # Test default scene
        if not settings['DefaultScene'] == 'interchange_empty':
            self.fail("Incorrect default scene: " + settings['DefaultScene'][0] + " == interchange_empty")

        # Test model 1
        if not settings['Models'][0]['model'] == 'ambulance':
            self.fail("Incorrect model: " + settings['Models'][0]['model'] + " == ambulance")

        if not settings['Models'][0]['pose'] == '10 5 0 0 0 0':
            self.fail("Incorrect model: " + settings['Models'][0]['pose'] + " == 10 5 0 0 0 0")

        # Test model 2
        if not settings['Models'][1]['model'] == 'ambulance':
            self.fail("Incorrect model: " + settings['Models'][1]['model'] + " == ambulance")

        if not settings['Models'][1]['pose'] == '20 5 0 1 2 0':
            self.fail("Incorrect model: " + settings['Models'][1]['pose'] + " == 20 5 0 1 2 0")

        if not settings['Models'][1]['name'] == 'amb2':
            self.fail("Incorrect model: " + settings['Models'][1]['name'] + " == amb2")

        input_file.Remove()

        self.assertTrue(True)

    def test_3_input_parser_ini(self):
        """ Description: Input file (ini) parser validation """

        input_file = InputFile('ini')

        input_file.AddLine('[Defaults]')
        input_file.AddLine('scene = interchange_empty')
        input_file.AddLine('[Model_1]')
        input_file.AddLine('model = ambulance')
        input_file.AddLine('pose = 10, 5, 0, 0, 0, 0')
        input_file.AddLine('[Model_2]')
        input_file.AddLine('model = ambulance')
        input_file.AddLine('pose = 20, 5, 0, 1, 2, 0')
        input_file.AddLine('name = amb2')

        iniparser.ReadFile(input_file.test_file)

        # Test default scene
        if not settings['DefaultScene'] == 'interchange_empty':
            self.fail("Incorrect default scene: " + settings['DefaultScene'][0] + " == interchange_empty")

        # Test model 1
        if not settings['Models'][0]['model'] == 'ambulance':
            self.fail("Incorrect model: " + settings['Models'][0]['model'] + " == ambulance")

        if not settings['Models'][0]['pose'] == '10 5 0 0 0 0':
            self.fail("Incorrect model: " + settings['Models'][0]['pose'] + " == 10 5 0 0 0 0")

        # Test model 2
        if not settings['Models'][1]['model'] == 'ambulance':
            self.fail("Incorrect model: " + settings['Models'][1]['model'] + " == ambulance")

        if not settings['Models'][1]['pose'] == '20 5 0 1 2 0':
            self.fail("Incorrect model: " + settings['Models'][1]['pose'] + " == 20 5 0 1 2 0")

        if not settings['Models'][1]['name'] == 'amb2':
            self.fail("Incorrect model: " + settings['Models'][1]['name'] + " == amb2")

        input_file.Remove()

        self.assertTrue(True)

    def test_4_thorough(self):
        """ Description: End-to-end test """

        #---------------------------
        # Test fully with text file
        #---------------------------

        try:
            subprocess.run(['python3', 'run.py', '-f', 'sample1.txt'], capture_output=True)

            if os.path.isfile('worlds/user_defined.world'):
                os.remove("worlds/user_defined.world")
            else:
                self.fail('UserDefined.world file was not created') 
        except:
            self.fail("Could not run 'python3 run.py -f sample1.txt'")

        #------------------------------------------
        # Test fully with text file and world name
        #------------------------------------------
        
        try:
            subprocess.run(['python3', 'run.py', '-f', 'sample1.txt', '-w', 'TestWorld'], capture_output=True)

            if os.path.isfile('worlds/TestWorld.world'):
                os.remove("worlds/TestWorld.world")
            else:
                self.fail('TestWorld.world file was not created') 
        except:
            self.fail("Could not run 'python3 run.py -f sample1.txt -w TestWorld'")

    def test_5_run_gazebo(self):
        """Description: Start gazebo and make sure it's runing and then kill it"""
        
        if sys.platform == 'darwin':
            """" Skip this test if running on MacOS """
            return

        try:
            print("Starting gazebo -->")
            subprocess.Popen(['python3', 'run.py', '-f', 'sample1.txt', '-o'],stdout=subprocess.PIPE)
            time.sleep(2) # wait for gazebo to start

            #check if gazebo is running
            output = subprocess.check_output("pgrep -l gazebo", shell=True).decode('utf-8')

            if output.split()[1] == 'gazebo':
                print("gazebo is running -->")
            else:
                self.fail('gazebo is not running') 

            print("killing gazebo")

            time.sleep(20)  # wait for 20 seconds

            subprocess.run(['killall', '-9 ', 'gzclient'], capture_output=True)
    
        except:
            self.fail("Could not run 'python3 run.py -f sample1.txt -o'")




def RunUnitTests():

    if not os.path.isdir(os.path.join(os.getcwd(), 'worlds/')):
        os.mkdir('worlds')

    if not os.path.isdir(os.path.join(os.getcwd(), 'test/results')):
        os.mkdir('test/results')

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test/results'))

if __name__ == '__main__':
    RunUnitTests()
