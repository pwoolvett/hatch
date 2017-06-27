import os
import subprocess
from contextlib import contextmanager

from appdirs import user_data_dir

from hatch.utils import NEED_SUBPROCESS_SHELL

ENV_DIR = os.path.join(user_data_dir('hatch', ''), 'envs')


def create_venv(d, pypath=None):
    command = ['virtualenv', d]
    if pypath:
        command.extend(['-p', pypath])
    subprocess.call(command, shell=NEED_SUBPROCESS_SHELL)


@contextmanager
def venv(d):
    if os.path.exists(os.path.join(d, 'bin')):  # no cov
        venv_exe_dir = os.path.join(d, 'bin')
    elif os.path.exists(os.path.join(d, 'Scripts')):  # no cov
        venv_exe_dir = os.path.join(d, 'Scripts')
    else:
        raise OSError('Unable to locate executables directory.')

    old_path = os.environ['PATH']
    os.environ['PATH'] = '{}{}{}'.format(venv_exe_dir, os.pathsep, old_path)

    try:
        yield
    finally:
        os.environ['PATH'] = old_path

















