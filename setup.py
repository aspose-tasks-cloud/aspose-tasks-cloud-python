# coding: utf-8


from setuptools import setup, find_packages  # noqa: H301

NAME = "aspose-tasks-cloud"
VERSION = "22.7.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.16", "six >= 1.10", "certifi", "python-dateutil"]
TEST_REQUIRES = []

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Aspose.Tasks Cloud API Reference",
    author='Ivan Andreychikov',
    author_email="ivan.andreychikov@aspose.com",
    url="https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-python",
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
        'Topic :: Office/Business :: Office Suites',
		'Topic :: Software Development :: Libraries',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
	],
    keywords=["aspose", "python", "aspose cloud", "microsoft project", "mpp", "primavera", "microsoft project server", "microsoft project online"],
    install_requires=REQUIRES,
	tests_require=TEST_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown"
)
