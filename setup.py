#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='rtmbot',
    version='0.4.1',
    description='A Slack bot written in python that connects via the RTM API.',
    author='Ryan Huber and Jeff Ammons',
    author_email='developers@slack.com',
    url='https://github.com/djedi/python-rtmbot',
    packages=find_packages(),
    entry_points={'console_scripts': ['rtmbot=rtmbot.bin.run_rtmbot:main']},
    install_requires=[
        'pyyaml>=3, <4',
        'slackclient>=1, <2'
    ]
 )
