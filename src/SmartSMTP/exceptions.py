
"""SmartSMTP is a python module to send and read email via SMTP protocol.

Description:
    The main target of the project is to provide an easily way to send and read
    email via SMTP protocol.

Author:
    Giuseppe Biolo <giuseppe.biolo@gmail.com> <https://github.com/gbiolo>

License:
    This file is part of smartrelay.

    pyproc is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    pyproc is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with SmartSMTP. If not, see <http://www.gnu.org/licenses/>.
"""


class ArgumentException(Exception):
    """Exception thrown when an argument passed to a method is out of format."""

    def __init__(self, msg):
        """Elementary constructor."""
        self.msg = msg

    def __str__(self):
        """Elementary to-string magic method."""
        return self.msg


class AttachmentException(Exception):
    """Exception thrown when a mail attachment doesn't exists or isn't readable."""

    def __init__(self, msg):
        """Elementary constructor."""
        self.msg = msg

    def __str__(self):
        """Elementary to-string magic method."""
        return self.msg
