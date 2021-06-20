from setuptools import setup, find_packages

setup(
    name='other_access',
    version='0.0.2',
    packages=['other_access'],
    license='none',
    description='os.access() alternative which can check access for other users',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yaroslaff/other_access',
    author='Yaroslav Polyakov',
    author_email='yaroslaff@gmail.com'
)