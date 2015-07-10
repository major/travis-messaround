#!/usr/bin/python
#
# Copyright 2015 Major Hayden
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from setuptools import setup


required_packages = [
    "click",
    "easydict",
    "psutil",
    "PyMySQL",
    "termcolor",
]

setup(
    name='mysqltuner',
    version='0.0.1',
    author='Major Hayden',
    author_email='major@mhtx.net',
    description="High-performance MySQL tuning script",
    install_requires=required_packages,
    packages=['mysqltuner'],
    url='https://github.com/rackerhacker/python-mysqltuner',
    entry_points={
        'console_scripts': [
            'mysqltuner = mysqltuner.executable:run_mysqltuner',
            ],
        },
    )
