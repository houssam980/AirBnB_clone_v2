

from fabric.api import local
from os.path import isdir
from datetime import datetime


def do_pack():

    dt = datetime.utcnow()
    fl= "versions/web_static_{}.tgz".format(dt)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(fl)).failed is True:
        return None
    return fl
