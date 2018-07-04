"""
                                                 
                                       _         
 ____  _____  ___   ____  ____ _____ _| |_ _____ 
|  _ \| ___ |/ _ \ / _  |/ ___|____ (_   _) ___ |
| | | | ____| |_| ( (_| | |   / ___ | | |_| ____|
|_| |_|_____)\___/ \___ |_|   \_____|  \__)_____)
                  (_____|                        
"""
from setuptools import setup

version = '0.1.0dev'

setup(
  name='neograte',
  version=version,
  description='Django South-inspired migrations for Neo4j',
  author='Martin Ronquillo',
  packages=['neograte'],
  # https://pypi.org/pypi?%3Aaction=list_classifiers
  classifiers=[
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Topic :: Database',
    ''
  ],
  entry_points={
    'console_scripts': ['neograte=neograte.cli:main'],
  },
  install_requires=[
    'setuptools',
    'py2neo>=4.0.0',
  ],
  url='https://github.com/PapayaHealth/neograte',
  keywords='neo4j migrations database',
  license='MIT',
)