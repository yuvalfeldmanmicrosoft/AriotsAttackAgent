import setuptools
import os
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Ariots-Attack-Agent",
    version="0.0.2",
    author="Yuval Feldman",
    author_email="yufeldma@microsoft.com",
    description="Microsoft ArIoTS Attack Agent",
    long_description="Micorosft ArIoTS Attack Agent",
    long_description_content_type="text/markdown",
    url="",
    entry_points={
        'console_scripts': ['ariotsaa = AttackAgent.AttackAgent:display_quote']
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)