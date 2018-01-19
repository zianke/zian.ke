"""
Insta485 development configuration.

Andrew DeOrio <awdeorio@umich.edu>
"""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/insta485/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xab\x83\r\xfaV\xb4\xf5b\x88\x13\x8f\xc4e\xe3\x80\xddB\x98\xa7,\xe6\xc1\xf0='  # noqa: E501  pylint: disable=line-too-long
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'uploads'
)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'insta485.sqlite3'
)
