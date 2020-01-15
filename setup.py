from setuptools import setup

setup(
    name='rev',
    version='0.1',
    author='hhro',
    description='reversing',
    packages = [],
    install_requires = [
        "colorlog",
        "gplaycli"
    ],
    entry_points = {
        'console_scripts':[
            'rev=rev.commandline.main:main'
        ]
    }
)
