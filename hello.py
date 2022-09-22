#!/usr/bin/env python3
from dev_aberto import hello
from datetime import date
from dateutil import parser
from babel.dates import format_datetime
import gettext
gettext.install('cli', localedir='locale') 

if __name__ == '__main__':
    date, name = hello()
    formatedDate = format_datetime(parser.parse(date), 'long')
    formatedName = _(name)
    print(_('Last commit made in: ') + formatedDate + _(', by, ') + formatedName)
