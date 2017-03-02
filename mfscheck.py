#!/usr/bin/python

import sys, os
import urllib2
from urllib2 import URLError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

link = 'http://' + sys.argv[1] + '/mfs/'

try:
    f = urllib2.urlopen(link, timeout=1.0)
    myfile = f.read()
    if 'Mirapolis File Conversion Server' in myfile:
        print ("1")
    else:
        print ("0")
except URLError as e:
    print ("0")
