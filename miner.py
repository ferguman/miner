import json
from os.path import exists, join

# TODO: This is the entry routine for your monero miner.
# NOTE: If you are creating a new GIT repo and you are going to put the data_location_json and/or settings.json file in your repo directory then be sure
#       to add these to the your .gitignore file.

# The first thing you need is a way to read configuration file to load the 

miner_settings = []

# Load the settings file 
if exists('data_location.json'):
   with open('data_location.json') as f:
      dl = json.load(f)
      if 'settings_file_path' in dl.keys():
         if exists(join(dl['settings_file_path'])):
            #TODO Add code to look for the required settings such as pool address and pool logon
            # with open(join(dl['settings_file_path'])) as s
            #    load_miner_settings(s)
         else:
            print('You must create a settings file')
            print('I will prompt you for answers but feel free to quit and create the file manually.')
      else:
         print('The file named data_location.json must have an attribute named settings.file_path')
else:
   print('You must create a data_location.json file')
