#!/usr/bin/env python
# coding=utf-8

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'CHANGELOG.rst')).read()

version = '0.3.0'

setup(
    name="autoloads",
    version=version,
    description="python web and databases's tools.",
    long_description=README + '\n\n' + NEWS,
    license='MIT License',
    author='wuxiaoge',
    author_email='returnliu@gmail.com',
    keywords='autoloads',
    url='https://github.com/wujuguang/autoloads.git',
    packages=find_packages(),
    install_requires=["pymysql", "sqlalchemy", "tornado", "mako", "pipe"],
    include_package_data=True,
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
    ]
)
