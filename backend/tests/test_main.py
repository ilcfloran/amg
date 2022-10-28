from backend.main import app
from typer.testing import CliRunner

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["1"])
    assert result.exit_code == 0
    assert "1" in result.stdout

    result = runner.invoke(app, ["3"])
    assert result.exit_code == 0
    assert "foo" in result.stdout

    result = runner.invoke(app, ["5"])
    assert result.exit_code == 0
    assert "bar" in result.stdout


def test_app_capitalize():
    result = runner.invoke(app, ["3", "--capitalize"])
    assert result.exit_code == 0
    assert "Foo" in result.stdout
