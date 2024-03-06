#!/usr/bin/python3
"""
generate a .tgz archive from the contents of the web_static 
"""


from fabric.api import local
from os.path import isdir
from datetime import datetime

def do_pack():
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        fl_name = "versions/web_static_{}.tgz".format(dt)
        local("tar -cvzf {} web_static".format(fl_name))
        return fl_name
    except:
        return None
