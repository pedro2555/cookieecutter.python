"""
{{ cookiecutter.project_name }}
Copyright (C) {{ cookiecutter.year }}  {{ cookiecutter.full_name }} <{{ cookiecutter.email }}>

This file is part of {{ cookiecutter.project_name }}.

{{ cookiecutter.project_name }} is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

{{ cookiecutter.project_name }} is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with {{ cookiecutter.project_name }}.  If not, see <http://www.gnu.org/licenses/>.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_{{ cookiecutter.package_dir_name }}
----------------------------------

Tests for `{{ cookiecutter.package_dir_name }}` module.
"""

import unittest

import {{ cookiecutter.package_dir_name }}


class Test{{ cookiecutter.package_dir_name|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert({{ cookiecutter.package_dir_name}}.__version__)

    def tearDown(self):
        pass
