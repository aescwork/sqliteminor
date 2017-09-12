# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='sqliteminor',
    version='1.1.1',
    description='Python class for working with sqlite databases.',
    long_description=long_description,
    url='https://github.com/aescwork/sqliteminor',
    author='aescwork',
    author_email='aescwork@protonmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Database',
		'Topic :: Database :: Front-Ends',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='sqliteminor setuptools development sqlite database python',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
	python_requires='>=2.7, ~=3.5',
    entry_points={
        'console_scripts': [
            'sqliteminor=sqliteminor:main',
        ],
    },
)
