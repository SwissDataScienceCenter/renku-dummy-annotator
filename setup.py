# -*- coding: utf-8 -*-
#
# Copyright 2022 - Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup

packages = find_packages()
version_file = open("VERSION")

setup(
    name="renku-dummy-annotator",
    description="Renku knowledge graph annotation plugin example",
    keywords="Renku",
    license="Apache License 2.0",
    author="John Doe",
    author_email="john@example.com",
    install_requires=["renku >= 1.0.0"],
    packages=packages,
    entry_points={"renku": ["dummy = dummy_annotator.plugin"]},
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    version=version_file.read().strip(),
    classifiers=[
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 4 - Beta",
        "Framework :: Renku",
    ],
)
