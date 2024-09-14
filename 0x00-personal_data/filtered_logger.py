#!/usr/bin/env python3
import re

import re

def filter_datum(fields, redaction, message, separator):
    """ Returns regex obfuscated log messages """
    for field in fields:
        p = re.escape(field) + r'=([^' + re.escape(separator) + ']*)'
        message = re.sub(p, lambda match: field + '=' + redaction, message)
    return message
