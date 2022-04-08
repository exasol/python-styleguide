from shutil import rmtree
from textwrap import dedent
from pathlib import Path
import nox

ROOT = Path(__file__).parent
STYLEGUIDE = ROOT / "styleguide"
SRC_DIRECTORY = STYLEGUIDE
BUILD_DIRECTORY = STYLEGUIDE / "_build"

nox.options.sessions = ['build', 'open']


@nox.session(python=None)
def build(session):
    """Build the styleguide."""
    session.run(
        "sphinx-build",
        f"{SRC_DIRECTORY.resolve()}",
        f"{(BUILD_DIRECTORY / 'html').resolve()}",
        external=True
    )


@nox.session(python=None)
def clean(session):
    """Remove the build directory."""
    if BUILD_DIRECTORY.exists():
        rmtree(BUILD_DIRECTORY.resolve())
        session.log(f"Removed {BUILD_DIRECTORY}")


@nox.session(python=None)
def open(session):
    """Open the styleguide in the browser."""
    index_page = BUILD_DIRECTORY / "html" / "index.html"
    if not index_page.exists():
        session.error(
            dedent(
            f"""
            File {index_page} does not exist.
            Please run `nox -s build` first
            """
            )
        )
    session.run(
        "python",
        "-m",
        "webbrowser",
        "-t",
        f"{index_page.resolve()}",
        external=True
    )


@nox.session(python=None)
def verify(session):
    """Checks if the styleguide builds successfully."""
    if BUILD_DIRECTORY.exists():
        rmtree(BUILD_DIRECTORY.resolve())
        session.log(f"Removed {BUILD_DIRECTORY}")
    session.run(
        "sphinx-build",
        "-W",
        "--keep-going",
        f"{SRC_DIRECTORY.resolve()}",
        f"{(BUILD_DIRECTORY / 'html').resolve()}",
        external=True
    )
