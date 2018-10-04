import os
import sys

import click

from hatch.commands.utils import CONTEXT_SETTINGS, echo_success, echo_warning, echo_info

HATCHRC_FILE = os.path.expanduser('~/.hatchrc')
BASHRC_FILE = os.path.expanduser('~/.bashrc')


def add_script_to_bashrc():
    try:
        os.system('echo "\n. ~/.hatchrc # enables hatch tab completion\n" >> ~/.bashrc')
        with open(BASHRC_FILE, 'r') as fin:
            bashrc = fin.read()
        if '.hatchrc' in bashrc:
            return True
        else:
            return False
    except BaseException:
        return False


def install_script():
    try:
        os.system('_HATCH_COMPLETE=source hatch > ~/.hatchrc')
        with open(HATCHRC_FILE, 'r') as fin:
            hatchrc = fin.read()
        if '_hatch_completion' in hatchrc:
            return True
        else:
            return False
    except BaseException:
        return False


@click.command(context_settings=CONTEXT_SETTINGS,
               short_help='Install tab-autocomplete for bash terminals.')
def autocomplete():
    """Install tab-autcoomplete for bash terminals.

    \b
    $ hatch autocomplete
    Script installed in ~/.hatchrc and sourced in ~/.bashrc
    """

    if not install_script():
        echo_warning(f"Something went wrong: script not installed")
        sys.exit(1)

    if not add_script_to_bashrc():
        echo_warning(f"Something went wrong: script installed but not added to ~/.bashrc")
        sys.exit(1)

    echo_success(f'Script installed in {HATCHRC_FILE} and sourced in {BASHRC_FILE}.')
    echo_info(f' To activate now, run:\nsource ~/.bashrc\n')
