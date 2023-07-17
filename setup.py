# pip3 install setuptools twine
# python3 setup.py sdist bdist_wheel
# twine upload dist/*


import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

with (HERE / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

setup(
    name="quaeso",
    version="0.1.1",
    description="python cli program to send requests",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zahash/quaeso",
    author="zahash",
    author_email="zahash.z@gmail.com",
    license="MIT",
    entry_points={
        'console_scripts': [
            'quaeso = quaeso.__main__:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["quaeso"],
    include_package_data=True,
    install_requires=requirements,
)
