from setuptools import setup, find_packages

setup(
    name='rev',
    version='0.1',
    author='hhro',
    description='reversing',
    packages = [],
    entry_points = {
        'console_scripts':[
            'rev=rev.commandline.main:main'
        ]
    }
)
