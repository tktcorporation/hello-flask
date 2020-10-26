from setuptools import setup
from setuptools import find_packages

__version__ = "0.0.1"

setup(
    name="hello_flask",
    version=__version__,
    description="test flask package",
    long_description="""
    This is test flask package.
    """,
    author="tktcorporation",
    url="https://github.com/tktcorporation/hello-flask",
    license="MIT",
    package_dir={"": "src", "resource": "resource"},
    packages=find_packages(where="src", exclude=("tests")),
)
