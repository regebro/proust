from setuptools import setup, find_packages
import sys, os

vinfo = sys.version_info[:2]
if vinfo == (2, 7) or vinfo >= (3,3):
    requires = []
else:
    requires = ['argparse']
    
version = '0.1'

setup(name='proust',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points={
               'console_scripts': [
                   'proust = proust:main',
               ],
      },
      test_suite='proust.tests.get_suite'
      )
