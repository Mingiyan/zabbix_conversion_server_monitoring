#!/usr/bin/python

import sys, os
import urllib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

link = 'http://' + sys.argv[1] + '/mfs/'

f = urllib.urlopen(link)
myfile = f.read()

if 'Mirapolis File Conversion Server' in myfile:
    print ("1")
else:
    sys.exit(1)
