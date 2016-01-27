"""Link Class Plugin for Pelican"""

## Copyright (C) 2015  Rafael Laboissiere
##
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Affero Public License as published by
## the Free Software Foundation, either version 3 of the License, or (at
## your option) any later version.
##
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## Affero General Public License for more details.
##
## You should have received a copy of the GNU Affero General Public License
## along with this program.  If not, see http://www.gnu.org/licenses/.


import os
import sys
from pelican import signals
from . mdx_linkclass import LinkClassExtension


def initialize (pelicanobj):
    """Initialize the Link Class plugin"""
    pelicanobj.settings.setdefault ('LINKCLASS_INTERNAL_CLASS', 'internal')
    pelicanobj.settings.setdefault ('LINKCLASS_EXTERNAL_CLASS', 'external')
    config = {'internal-class':
                  pelicanobj.settings.get ('LINKCLASS_INTERNAL_CLASS'),
              'external-class':
                  pelicanobj.settings.get ('LINKCLASS_EXTERNAL_CLASS')}
    pelicanobj.settings ['MD_EXTENSIONS'].append (LinkClassExtension (config))


def register ():
    """Register the Link Class plugin with Pelican"""
    signals.initialized.connect (initialize)
