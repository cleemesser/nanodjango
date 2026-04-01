"""
Test that ``nanodjango convert`` conditionally includes NinjaAPI scaffolding
in the generated ``api.py`` based on whether ``@app.api`` routes are present.
"""

from pathlib import Path
from textwrap import dedent

from nanodjango.testing.utils import cmd

# ---- helpers ----

EXAMPLES_DIR = Path(__file__).resolve().parent / "fixtures"


def _write_app(tmp_path: Path, source: str) -> Path:
    """Write a single-file nanodjango app and return its path."""
    app_file = tmp_path / "testapp.py"
    app_file.write_text(dedent(source))
    return app_file


def _convert(app_file: Path, out_dir: Path) -> Path:
    """Run ``nanodjango convert`` and return the project root."""
    cmd("convert", str(app_file), str(out_dir), "--name=converted")
    return out_dir


# ---- tests ----


def test_convert_with_api_routes_includes_ninja(tmp_path):
    """When the app uses @app.api, api.py should contain NinjaAPI."""
    app_file = _write_app(
        tmp_path,
        """\
        from nanodjango import Django

        app = Django()

        @app.route("/")
        def home(request):
            return "hello"

        @app.api.get("/items")
        def list_items(request):
            return [{"id": 1}]
        """,
    )

    out_dir = tmp_path / "out"
    _convert(app_file, out_dir)

    api_py = out_dir / "converted" / "testapp" / "api.py"
    assert api_py.exists(), "api.py should be generated when @app.api routes exist"
    content = api_py.read_text()
    assert "from ninja import NinjaAPI" in content
    assert "api = NinjaAPI()" in content


def test_convert_without_api_routes_excludes_ninja(tmp_path):
    """When the app has no @app.api routes, api.py should not be generated."""
    app_file = _write_app(
        tmp_path,
        """\
        from nanodjango import Django

        app = Django()

        @app.route("/")
        def home(request):
            return "hello"
        """,
    )

    out_dir = tmp_path / "out"
    _convert(app_file, out_dir)

    api_py = out_dir / "converted" / "testapp" / "api.py"
    assert not api_py.exists(), "api.py should not be generated without @app.api routes"
