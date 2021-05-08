'''
Application : Envision
File name   : helper.py
Authors     : Jacob Summerville and Safwan Elmadani
Description : This file contains the functions called directly from 
              run.py to guide Envision
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

import argparse, os, sys, subprocess, logging, datetime

from src.parser import txtparser, iniparser
from src.world  import World
from src        import info

def Header():
    """
    Summary     : Print Envisions header message
    Parameters  : None
    Return      : None
    """

    print('\n--- Envision ---')

    print('\nDirectories...')
    print('Current Directory : ' + os.getcwd())

def InitializeLogger():
    """
    Summary     : Initializes the logger that will be used for log messages.
    Parameters  : None
    Return      : None
    """

    today = datetime.datetime.now()

    if not os.path.isdir('logs/'):
        os.mkdir('logs/')

    log_file = 'logs/' + today.strftime("%Y%m%d_%H%M%S") + '.log'

    logging.basicConfig(filename=log_file, 
                        format='%(asctime)s - %(levelname)s: %(message)s', 
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)

    logging.info('Starting Envision')

    print('Log File          : ' + log_file) 

def ParseArguments():
    """
    Summary     : Parses the command line arguments and returns the parser.
    Parameters  : None
    Return      : argument values
    """

    parser = argparse.ArgumentParser(description=info.__doc__)

    parser.add_argument('-f', '--file', help='Text file to be used (e.g. sample1.txt)')
    parser.add_argument('-w', '--world', help='World Name (Optional)')
    parser.add_argument('-t', '--test', help='Testing mode enabled', action="store_true")
    parser.add_argument('-o', '--open', help='Open world in Gazebo', action="store_true")

    return parser.parse_args()

def CheckTestMode(args):
    """
    Summary     : Check if user specified test mode and run 
                  envisiontests if test mode is enabled.
    Parameters  : command line arguments from the user (args)
    Return      : None
    """

    # Check if in testing mode
    if args.test:   
        print('\n--- Testing mode enabled ---\n')
        
        # Remove all arguments
        while len(sys.argv) > 1:
            sys.argv.pop()

        subprocess.run(['python3', 'test/envisiontests.py', '-v'])
        print('')
        sys.exit()

def ParseInputFile(args):
    """
    Summary     : Parse the user provided input file for data.
    Parameters  : command line arguments from the user (args)
    Return      : None
    """

    if args.file: 
        filepath = os.path.join(os.getcwd(), 'inputfiles/', args.file)

        if not os.path.isfile(filepath):
            print(args.file, 'is not a file in the directory', os.path.join(os.getcwd(), 'inputfiles/'))
            logging.critical(filepath + ' does not exist')
            sys.exit() 

        if filepath.endswith('.txt'):
            txtparser.ReadFile(filepath) 
        elif filepath.endswith('.ini'):
            iniparser.ReadFile(filepath) 
        else:
            print('Unexpected file type in input file: ' + filepath)
            logging.critical('Unexpected file type in input file: ' + filepath)

    else:
        print("Please enter an input file to be interpreted (e.g. -f sample1.txt or -f sample2.ini)")
        logging.critical('No input file specified')
        sys.exit()

def WorldName(args):
    """
    Summary     : Get and format the world name to be used
    Parameters  : command line arguments from the user (args)
    Return      : None
    """

    if not os.path.isdir(os.path.join(os.getcwd(), 'worlds/')):
        os.mkdir('worlds')

    if args.world: 
        if not args.world.endswith('.world'):  # if .world wasn't added, add it
            world_name = args.world + '.world'
        else:
            world_name = args.world
    else:
        world_name = 'user_defined.world'

    print('World File        : ' + 'worlds/' + world_name)

    return world_name

def Launch(world_name):
    """
    Summary     : Initiates the creation of the world file.
    Parameters  : The world name to be used
    Return      : None
    """

    print('Creating ' + world_name)

    World(world_name)

    if os.path.isfile((os.path.join(os.getcwd(), 'worlds/', world_name))):
        print('World successfully created\n')
    else:
        print('Error creating world -> Check the logs for further information\n')

def RunGazebo(args, world_name):
    """
    Summary     : Run the world file in gazebo.
    Parameters  : command line arguments from the user (args);
                  created world name
    Return      : None
    """

    if args.open:

        world_file = os.path.join(os.getcwd(), 'worlds/', world_name)

        if os.path.isfile(world_file):
            logging.info('Opening world file in Gazebo: ' + world_file)
            subprocess.Popen(['gazebo', world_file])
        else:
            logging.info('Unable to open world file in Gazebo: ' + world_file)
            print('Unable to open world file in Gazebo')

    logging.info('Envision Exiting Successfully')
