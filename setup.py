#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup, find_packages  # noqa

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    # https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


def main():
    setup(
        name="pydocx_notes",
        version=find_version('pydocx_notes', '__init__.py'),
        description="PyDocX mixin - export notes",
        author="Chirica Gheorghe",
        author_email="chiricagheorghe@gmail.com",
        url="https://github.com/botzill/pydocx-notes",
        platforms=["any"],
        license="BSD",
        packages=find_packages(),
        scripts=[],
        zip_safe=False,
        install_requires=[
        ],
        cmdclass={},
        classifiers=[
            # "Development Status :: 1 - Alpha",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Topic :: Text Processing :: Markup :: HTML",
            "Topic :: Text Processing :: Markup :: XML",
        ],
        long_description=read('README.rst'),
    )


if __name__ == '__main__':
    main()