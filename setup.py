from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in asmahan/__init__.py
from asmahan import __version__ as version

setup(
	name="asmahan",
	version=version,
	description="4trhu",
	author="Asmahan",
	author_email="Asmahan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
