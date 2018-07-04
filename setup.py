from setuptools import setup

version = '0.1.0dev'

setup(
  name='neograte',
  version=version,
  description='Django South-inspired migrations for Neo4j',
  author='Martin Ronquillo',
  # https://pypi.org/pypi?%3Aaction=list_classifiers
  classifiers=[
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Topic :: Database',
    ''
  ],
  install_requires=[
    'setuptools',
  ],
  url='https://github.com/PapayaHealth/neograte',
  keywords='neo4j migrations database',
  license='MIT',
)