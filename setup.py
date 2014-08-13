import os
from setuptools import setup

setup(
    name = 'cidrchk',
    version = '1.0.0',
    author = 'Joseph Hunkeler',
    author_email = 'jhunkeler@gmail.com',
    description = ('A simple "Is my computer on this subnet?" detection script.'),
    license = 'BSD',
    keywords = 'cidrchk detect network interface ethernet',
    zip_safe = True,
    scripts = [
        'cidrchk',
    ],
    install_requires = [
        'netaddr',
        'netifaces',
        'argparse',
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ]
)
