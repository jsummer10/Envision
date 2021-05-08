<p align="center">
  <img src="docs/Logo.png" width="300"> 
</p>

# Envision
Envision is a scenario generation language for Gazebo. Envision is designed to make creating world files in Gazebo simple and painless. Instead of trying to manually create worlds in Gazebo, Envision will allow you to choose a premade scene and add models to it using an input file. 

# Table of Contents
* [Software Requirements](#Software-Requirements)  
* [Installation](#Installation)  
    1. [Gazebo](#1-Gazebo)
    2. [Envision](#2-Envision)
    3. [Model Library](#3-Model-Library)
* [Dependencies](#Dependencies)  
* [Directories](#Directories)  
* [How To Run (Example)](#How-To-Run)  
* [After Running](#After-Running)
* [Documentation](#Documentation)
* [Authors](#Authors)


## Software Requirements
* Ubuntu 18.04 or 20.04
* Python >= 3.8 (not tested on older versions)

## Installation

### 1. Gazebo

Installing Gazebo

``` $ curl -sSL http://get.gazebosim.org | sh ```

<br/>

### 2. Envision
Download Envision from GitHub...

``` $ git clone https://github.com/Vikings1028/envision.git ```

<br/>

## Dependencies

`  pip3 install html-testRunner argparse `

<br/>

## Directories

| Name         | Contents                                            |
| ------------ | --------------------------------------------------- |
| docs         | Class and project documentation                     |
| inputfiles   | Input files that will be analyzed by envision       |
| logs         | Log files created at runtime                        |
| src          | Source files                                        |
| test         | Test code and unit tests                            |
| worlds       | Created .world files                            |

## How To Run

To run Envision, you will create an input file and place it in the inputfiles directory. By default, a sample file will be included called [sample1.txt](inputfiles/sample1.txt) that will guide you through the process of entering data. The [InputReadMe](inputfiles/InputReadMe.md) file includes all of the possible models and scenes. 

Following the creation of the input file, the run.py file will be used. The follwing switches are available:

``` -h ``` or ``` --help ```: Display possible switches

``` -f ``` or ``` --file ```: Indicates the text file to be used

``` -t ``` or ``` --test ```: Testing mode

``` -w ``` or ``` --world ```: Output .world file name

``` -o ``` or ``` --open ```: Open .world file in Gazebo after running

<br/>

Change directory to envision...

``` $ cd PATH_TO_ENVISION/ ```

<br/>

Run Envision with just a file...

``` $ python3 run.py -f sample1.txt ```

Run Envision with a file and world name...

``` $ python3 run.py -f sample1.txt -w newWorld ```

Run Envision with a file and open in Gazebo...

``` $ python3 run.py -f sample1.txt -o ```

Run Envision in test mode...

``` $ python3 run.py -t ```

## After Running

Envision will output a .world file inside of the worlds directory. If the world name was specified, the world file will be named that. If the world name was not specified, the world file will be called user_defined.world.

The world file can then be opened in gazebo by calling Gazebo along with the world file. 

If trying to output user_defined.world in Gazebo, you would type 

``` $ gazebo user_defined.world ```

# Authors

- Jake Summerville
- Safwan Elmadani
