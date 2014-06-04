from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'pycity',
  packages = ['pycity'], # this must be the same as the name above
  include_package_data=True,
  version = '0.1.2',
  description = 'Provides programmatic access to a list of the largest US Cities',
  author = 'Jean-Marc Skopek',
  author_email = 'jskopek@gmail.com',
  url = 'https://github.com/jskopek/pycity', # use the URL to the github repo
  download_url = 'https://github.com/jskopek/pycity/archive/0.1.2.tar.gz',
  keywords = [],
  classifiers = [],
)
