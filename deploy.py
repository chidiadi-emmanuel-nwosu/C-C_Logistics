#!/usr/bin/python3
"""deploy module
"""
import os
from datetime import datetime
from fabric.api import run, local, env, put

env.hosts = ['128.199.12.180']
env.user = 'logistics'


def do_pack():
    """function that generates a .tgz archive from the
       the contents of webstatic folder
    """
    try:
        print("in here")
        created_at = datetime.now().strftime('%Y%m%d%H%M%S')
        local('mkdir -p versions')
        archive_name = f"app_{created_at}.tgz"
        local(f'tar -cvzf versions/{archive_name} --exclude=node_modules app')
        return f"versions/{archive_name}"
    except Exception as e:
        return None


def do_deploy(archive_path):
    """function that distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        arc_name = archive_path.split('/')[-1]
        release_folder = f'/data/cc_logistics/releases/{arc_name.split(".")[0]}'

        put(archive_path, '/tmp/')
        run(f'mkdir -p {release_folder}')
        run(f'tar -xzf /tmp/{arc_name} -C {release_folder}')
        run(f'rm /tmp/{arc_name}')
        # run(f'mv {release_folder}/app/* {release_folder}/')
        # run(f'rm -rf {release_folder}/app/')
        run(f'ln -sf {release_folder} /data/cc_logistics/current')
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_name = do_pack()
    if not archive_name:
        return False

    return do_deploy(archive_name)

if __name__ == "__main__":
    deploy()
