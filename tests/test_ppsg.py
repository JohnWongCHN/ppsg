import click
from click.testing import CliRunner
from ppsg.ppsg import main

def test_main():
    print('run test main')
    runner = CliRunner()
    result = runner.invoke(main, ['--name=demo'])
    print('Exit Code: ' + str(result.exit_code))
    print('Output: ' + result.output)
    assert result.exit_code == 0