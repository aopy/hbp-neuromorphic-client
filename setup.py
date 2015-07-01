#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

long_description = open("README.txt").read()

setup(
    name="hbp_neuromorphic_platform",
    version='0.1.1',
    packages=['nmpi'],
    install_requires=['requests',],
    author="Andrew P. Davison and Domenico Guarino",
    author_email="andrew.davison@unic.cnrs-gif.fr",
    description="Client software for the Human Brain Project Neuromorphic Computing Platform",
    long_description=long_description,
    license="Proprietary License",
    url='http://www.humanbrainproject.eu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering']
)
