try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Module for generating numerous slightly-different versions of a given form letter',
    'author': 'Silas Barta',
    'url': 'None',
    'download_url': 'None',
    'author_email': 'sbarta@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['LivelyLetter'],
    'scripts': [],
    'name': 'LivelyLetter'
}

setup(**config)
