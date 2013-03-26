from setuptools import setup
from toooml import __version__

setup(
    name="toooml",
    version=__version__,
    author="hit9",
    author_email="nz2324@126.com",
    description=(
        """
        Python implementation for toml.
        Support both unicode string and raw string.
        An improved version of marksteve/toml-ply
        """
    ),
    license="MIT",
    keywords="toml, parser",
    url="https://github.com/hit9/toooml",
    py_modules=["toooml"],
    install_requires=["ply"]
)
