#!/usr/bin/python3
"""

"""
from os.path import exists
from fabric.api import put, run, env

env.hosts = ['100.26.49.131', '54.197.89.103']


def do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    try:
        f_name = archive_path.split("/")[-1]
        not_exct = f_name.split(".")[0]
        pth = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(pth, not_exct))
        run('tar -xzf /tmp/{} -C {}{}/'.format(f_name, pth, not_exct))
        run('rm /tmp/{}'.format(f_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(pth, not_exct))
        run('rm -rf {}{}/web_static'.format(pth, not_exct))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(pth, not_exct))
        return True
    except:
        return False
