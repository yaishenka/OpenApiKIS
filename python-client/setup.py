# coding: utf-8

"""
    UrlShortener API

    Description  # noqa: E501

    OpenAPI spec version: v1
    Contact: gagarinovdaniil@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="UrlShortener API",
    author_email="gagarinovdaniil@gmail.com",
    url="",
    keywords=["Swagger", "UrlShortener API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Description  # noqa: E501
    """
)
