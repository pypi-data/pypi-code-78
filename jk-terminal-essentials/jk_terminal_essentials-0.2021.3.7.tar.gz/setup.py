################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Programming Language :: Python :: 3",
	],
	description = "Provides essential constants and data about the terminal.",
	include_package_data = False,
	install_requires = [
	],
	keywords = [
		"...",
	],
	license = "proprietary",
	name = "jk_terminal_essentials",
	packages = [
		"jk_terminal_essentials",
	],
	version = "0.2021.3.7",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
