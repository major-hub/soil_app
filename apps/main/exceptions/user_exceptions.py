from django.utils.translation import gettext as _


class UserException(Exception):
    key = ''
    message = ''

    ERROR_KEYS = {
        "NOT_MATCHED_PASSWORDS": "NOT_MATCHED_PASSWORDS"
    }

    ERROR_MESSAGES = {
        "NOT_MATCHED_PASSWORDS": _("Passwords did not match, please carefully check before you entering the passwords!")
    }

    def __init__(self, key):
        self.key = key
        self.message = self.ERROR_MESSAGES[key]
