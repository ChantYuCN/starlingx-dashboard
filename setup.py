# Copyright (c) 2018 Intel Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# THIS FILE IS MANAGED BY THE GLOBAL REQUIREMENTS REPO - DO NOT EDIT
import setuptools

# In python < 2.7.4, a lazy loading of package `pbr` will break
# setuptools if some other modules registered functions in `atexit`.
# solution from: http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing  # noqa
except ImportError:
    pass

setuptools.setup(
    version="1.0"
    setup_requires=['pbr>=1.8'],
    pbr=True)

#setuptools.setup(
#    name="starlingx_dashboard",
#    version="1.0"
#    author="yuchengde",
#    author_email="yu.chengde@99cloud.net",
#    url="https://github.com/ChantYuCN/starlingx-dashboard.git",
#    packages=setuptools.find_packages(),
#    classifiers=[
#        "Programming Language :: Python :: 3",
#    ],
#    python_requires='>=3.6',
#)