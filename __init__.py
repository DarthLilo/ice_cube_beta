bl_info ={
    "name": "Ice Cube Beta",
    "author": "DarhtLilo",
    "version": (1, 4, 3),
    "blender": (3, 0, 0),
    "location": "View3D > Tool",
    "description": "Beta Version of Ice Cube",
    "tracker_url": "https://discord.gg/3G44QQM",
    "category": "Lilo's Rigs",
}

import bpy
import importlib
import sys
import os

#File Variables
root_folder = os.path.dirname(os.path.abspath(__file__))
github_url = "https://api.github.com/repos/DarthLilo/ice_cube_beta/releases/latest"
latest_dlc = "https://raw.githubusercontent.com/DarthLilo/ice_cube_beta/master/ice_cube_data/dlc_list.json"
dlc_id = []
dlc_type = []
dlc_author = []
dlc_date = []
dlc_enum_data = []
update_available = False

#Folder Creation
required_dirsmain = ["backups","downloads"]

for dir in required_dirsmain:
    dir_path = os.path.normpath(f"{root_folder}/{dir}")
    if os.path.exists(dir_path):
        print(f"Found path {dir_path}")
    else:
        os.mkdir(dir_path)
        print(f"Made directory {dir_path}")


required_dirs = ["skins","user_packs", "user_packs/rigs", "user_packs/inventory"]
for dir in required_dirs:
    dir_path = os.path.normpath(f"{root_folder}/ice_cube_data/internal_files/{dir}")
    if os.path.exists(dir_path):
        print(f"Found path {dir_path}")
    else:
        os.mkdir(dir_path)
        print(f"Made directory {dir_path}")


#Path Appending
sys.path.append(os.path.dirname(os.path.abspath(__file__)))



#Import Files
from . import main
from . import ice_cube_data

#Reload
importlib.reload(main)
importlib.reload(ice_cube_data)


def register():
    main.register()
    ice_cube_data.register()

def unregister():
    main.unregister()
    ice_cube_data.unregister()
