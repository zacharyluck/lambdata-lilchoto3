from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='lambdata-zacharyluck',
    version='1.0.1',
    author='Zachary Luck',
    author_email='zacharysluck@gmail.com',
    description='Some simple DataFrame altering functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Lilchoto3/lambdata-lilchoto3',
    packages=find_packages()
)