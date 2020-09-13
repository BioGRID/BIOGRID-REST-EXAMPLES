# BIOGRID-REST-EXAMPLES
Sample code for accessing the BioGRID Rest Service and working with the resulting datasets.

## Development Status
+ **Status**: Stable
+ **Version**: 1.0

## Requirements
+ Python 3.6.9+
+ Pipenv
+ Requirements are located in the Pipfile, simply execute `pipenv shell` inside this directory to activate the virtual environment and install required dependencies.
+ If dependencies are not installed, run `pipenv install` when inside your virtual environment

## Configuration
+ All configuration options are located in the config/config.sample.yml file in YAML format. Simply rename the file to config.yml and update the options contained within to reflect your own environment.
+ All access to the BioGRID ORCS Webservice requires an individual access key. It's free to signup to use it. You will need to register at **https://webservice.thebiogrid.org/** to obtain one, and enter it in your config file for it to be accessible from all example code in this repository.
+ For a listing of all configurable search parameters when making requests, visit our wiki: **https://wiki.thebiogrid.org/doku.php/biogridrest**

## How to Run
+ After completing the configuration steps above. Simply run: **python \<script name\>** at the command prompt. Example: **python get_organisms.py**

## Examples
+ [**get_organisms.py**](https://github.com/BioGRID/BIOGRID-REST-EXAMPLES/blob/master/get_organisms.py) - Obtain currently supported organism names and ids
