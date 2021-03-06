"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "kleister"
VERSION = "1.0.0-alpha1"

REQUIRES = [
    "urllib3 >= 1.25.3",
    "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    author="Thomas Boerger",
    author_email="thomas@webhippie.de",
    description="Kleister OpenAPI",
    long_description="API definition for Kleister, manage mod packs for Minecraft",  # noqa: E501
    license="Apache License 2.0",
    keywords=["openapi", "openapi-generator", "minecraft"],
    python_requires=">=3.6",
    url="https://github.com/kleister/kleister-python",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
)
