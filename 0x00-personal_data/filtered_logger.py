#!/usr/bin/env python3
import re

def filter_datum(fields, redaction, message, separator):
    pattern = separator.join(re.escape(field) + r'=[^' + re.escape(separator) + ']*' for field in fields)
    return re.sub(pattern, lambda match: match.group(0).split('=')[0] + '=' + redaction, message)
