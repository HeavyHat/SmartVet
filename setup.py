from setuptools import setup

setup(name='SmartVet',
      version='0.0.1',
      description='Client focused application for vets, to integrate and analyse models more easily with a wide variety of features.',
      author='Joshua Langley',
      author_email='Joshua.Langley.1995@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['flask>=0.10.1', 'flask-login>=0.2.7', 'sqlalchemy>=0.8.2', 'flask-sqlalchemy>=1.0'],
      )
