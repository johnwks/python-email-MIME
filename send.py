#!/bin/env python

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

strFrom = 'XXX@XXX.XXX'
strTo = 'YYY@YYY.YYY'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'XXXXXXXXXXX'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
msgAlternative.attach(msgText)

msgText = MIMEText('<b>XXXXXXXXXXXXXXXXXXXXXX<br>', 'html')
msgAlternative.attach(msgText)

fp = open('03.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

fp = open('04.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image2>')
msgRoot.attach(msgImage)

fp = open('05.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image3>')
msgRoot.attach(msgImage)

smtp = smtplib.SMTP('X.X.X.X')
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()
