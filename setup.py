# ##################################################################################### #
# ISIS File Polling Repository : https://github.com/ISISSoftwareServices/ISISFilePolling
#
# Copyright &copy; 2020 ISIS Rutherford Appleton Laboratory UKRI
# ##################################################################################### #
# pylint:skip-file
"""
Setup for the project
"""

from setuptools import setup

setup_requires = [
    'autoreduce_utils',
    'filelock',
    'requests',
]

setup(
    name='autoreduce-run-detection',
    version='22.0.0.dev0',
    description='A service to discover and ingest new files produced by the ISIS neutron and muon facility',
    author='ISIS Autoreduction Team',
    url='https://github.com/ISISScientificComputing/autoreduce-run-detection',
    install_requires=setup_requires,
)
