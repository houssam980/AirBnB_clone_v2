#!/usr/bin/python3
"""
generate a .tgz archive from the contents of the web_static 
"""


from datetime import datetime
from os.path import isdir
from fabric.api import local



def do_pack():
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file = "versions/web_static_{}.tgz".format(dt)
        local("tar -cvzf {} web_static".format(file))
        return file
    except:
        return None
