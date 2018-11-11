from distutils.core import setup

with open('README') as file:
	readme = file.read()

setup(
	name='ch03_richardn',
	version='2.0.0',
	packages=['wargame'],
	url='https://testpypi.python.org/pypi/ch03_richardn/',
	license='LICENSE.txt',
	description='my fantasy game',
	long_description=readme,
	author='Richard',
	author_email='rnolec@gmail.com'
)


