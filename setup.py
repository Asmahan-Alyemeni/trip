from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in trip/__init__.py
from trip import __version__ as version

setup(
	name="trip",
	version=version,
	description="this trip",
	author="Asmahan",
	author_email="asmahan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
