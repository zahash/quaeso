# bumpversion --current-version <__version__> (major|minor|patch) setup.py

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

with (HERE / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

setup(
    name="yeet",
    version="0.0.2",
    description="Yeet DEM Requests",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zahash/yeet",
    author="zahash",
    author_email="zahash.z@gmail.com",
    license="MIT",
    entry_points={
        'console_scripts': [
            'yeet = yeet.__main__:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["yeet"],
    include_package_data=True,
    install_requires=requirements,
)
