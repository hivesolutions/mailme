#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

setuptools.setup(
    name="mailme-py",
    version="0.1.4",
    author="Hive Solutions Lda.",
    author_email="development@hive.pt",
    description="Mailme",
    license="Apache License, Version 2.0",
    keywords="mailme smtp service",
    url="http://pushi.hive.pt",
    zip_safe=False,
    packages=[
        "mailme",
        "mailme.controllers",
        "mailme.controllers.api",
        "mailme.controllers.web",
        "mailme.models",
    ],
    test_suite="mailme.test",
    package_dir={"": os.path.normpath("src")},
    package_data={
        "mailme": [
            "templates/*.tpl",
            "templates/admin/*.tpl",
            "templates/email/*.tpl",
            "templates/styles/*.tpl",
        ]
    },
    install_requires=["netius", "appier", "appier-extras", "jinja2", "pymongo"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
