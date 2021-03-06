import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='chuck_pyutils',
    version='0.4',
    packages=['chuck_pyutils'],
    url='https://github.com/ChuckWoodraska/ChuckPyUtils',
    license='',
    author='Chuck Woodraska',
    author_email='chuck.woodraska@gmail.com',
    description=read('README.md'),
    install_requires=['PyMySQL', 'jwcrypto', 'stringcase'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"
    ]
)
