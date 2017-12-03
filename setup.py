# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="toxic_proxy",
    version="0.0.3",
    description="An asyncio tcp proxy for network resiliency testing",
    license="MIT",
    author="Alex Myasoedov (Miasoiedov)",
    author_email="msoedov+github@gmail.com",
    packages=['toxic_proxy'],
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ]
)
