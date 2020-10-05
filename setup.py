#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:00:48 2020

@author: Miles
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = "reading-frame-MilesHorne",
    version = "0.0.1",
    author = "Miles Horne",
    author_email = "lmhorne@miners.utep.edu",
    description = "reading frame package for Bioinfo class",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https:github.com/MilesHorne/Reading_Frames",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming language :: Python :: 3"
    ],
    python_requires = '>=3.6')
    