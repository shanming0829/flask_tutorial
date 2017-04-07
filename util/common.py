# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
import sys

__authors__ = "Shanming Liu"


def combine_path(path, *paths):
    if sys.platform in ['linux2']:
        return os.path.join(path, *paths)
    return os.path.join(path, *paths).replace('/', '\\')
