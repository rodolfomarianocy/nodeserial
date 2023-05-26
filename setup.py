#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages
import os

meta = {}
here = os.path.abspath(os.path.dirname(__file__))

with open(f"{here}/nodeserial/__meta__.py",encoding="utf-8") as arquivo:
    exec(arquivo.read(), meta)

with open("README.md", "r",encoding="utf-8") as arq:
    readme = arq.read()

setup(name=meta["__title__"],
    version=meta["__version__"],
    author=meta["__author__"],
    url=meta["__url__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email=meta["__author_email__"],
    keywords='Deserialization node security',
    description=meta["__description__"],
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.6, <4",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Topic :: System :: Operating System",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities"
    ],
    entry_points={'console_scripts': [
        'nodeserial=nodeserial.nodeserial:argumentos',
        ]
    })