import os

from click.testing import CliRunner

from hatch.cli import hatch
from .utils import matching_file, temp_chdir


def test_invalid_name():
    with temp_chdir() as d:
        runner = CliRunner()
        runner.invoke(hatch, ['new', 'invalid-name', '--basic'])

        assert os.path.exists(os.path.join(d, 'invalid-name', 'invalid_name', '__init__.py'))


def test_output():
    with temp_chdir() as d:
        runner = CliRunner()
        result = runner.invoke(hatch, ['new', 'new-project', '--basic'])

        assert result.exit_code == 0
        assert 'Created project `new-project`' in result.output


def test_already_exists():
    with temp_chdir() as d:
        d = os.path.join(d, 'ok')
        os.makedirs(d)
        runner = CliRunner()
        result = runner.invoke(hatch, ['new', 'ok', '--basic'])

        assert result.exit_code == 1
        assert 'Directory `{}` already exists.'.format(d) in result.output


def test_basic():
    with temp_chdir() as d:
        runner = CliRunner()
        runner.invoke(hatch, ['new', 'ok', '--basic'])
        d = os.path.join(d, 'ok')

        assert os.path.exists(os.path.join(d, 'ok', '__init__.py'))
        assert os.path.exists(os.path.join(d, 'tests', '__init__.py'))
        assert os.path.exists(os.path.join(d, 'setup.py'))
        assert os.path.exists(os.path.join(d, 'requirements.txt'))
        assert os.path.exists(os.path.join(d, '.coveragerc'))
        assert os.path.exists(os.path.join(d, 'tox.ini'))
        assert matching_file(r'^LICENSE.*', os.listdir(d))
        assert matching_file(r'^README.*', os.listdir(d))


def test_cli():
    with temp_chdir() as d:
        runner = CliRunner()
        runner.invoke(hatch, ['new', 'ok', '--cli'])
        d = os.path.join(d, 'ok')

        assert os.path.exists(os.path.join(d, 'ok', 'cli.py'))
