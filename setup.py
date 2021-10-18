from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.dev'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='test_setup',
    version=version,
    description="ez_setup.py and distribute_setup.py",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      'Programming Language :: Python :: 3',
    ],
    keywords='test_setup',
    author='test_setup',
    author_email='rodrigo.machado3.14@hotmail.com',
    url='https://github.com/RodrigoMachado9/rest_bootle_sqlachemy',
    license='PSF or ZPL',
    py_modules = ['test_setup', 'distribute_setup'],
    zip_safe=False,
    install_requires=install_requires,
)
