# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Frootlab
#
# This file is part of Frootlab Hup, https://www.frootlab.org/hup
#
#  Hup is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Hup is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License along with
#  Hup. If not, see <http://www.gnu.org/licenses/>.
#
"""Abstract Base Classes for file I/O."""

__copyright__ = '2019 Frootlab'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

import abc
from typing import Any, IO, Optional

#
# File Connector
#

class Connector(abc.ABC):
    """File Connector Base Class."""

    @property
    @abc.abstractmethod
    def name(self) -> Optional[str]:
        raise NotImplementedError(
            f"'{type(self).__name__}' is required "
            "to implement a property 'name'")

    @abc.abstractmethod
    def open(self, *args: Any, **kwds: Any) -> IO[Any]:
        raise NotImplementedError(
            f"'{type(self).__name__}' is required "
            "to implement a method 'open'")
