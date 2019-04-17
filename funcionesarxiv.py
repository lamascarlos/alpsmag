import sys 
import os
#import numpy
#import h5py
#import matplotlib.pyplot as plt
import smtplib 


#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from smtplib import SMTP



def notimail(subject="Basic Notification",main="the main message is empty"):
    # mail parameters 
    codeL="1"
    from_address = "wolfram.brenig@gmail.com"
    to_address = "quiendijoborrador@gmail.com"
    message = """ %s  """%(main)
    asunto=""" %s  """%(subject)
    
    # we build the mime message
    mime_message = MIMEText(message, "plain")
    mime_message["From"] = from_address
    mime_message["To"] = to_address
    mime_message["Subject"] =asunto
    
    # Nos conectamos al servidor SMTP de Gmail
    serverSMTP = SMTP('smtp.gmail.com',587)
    serverSMTP.ehlo()
    serverSMTP.starttls()
    serverSMTP.ehlo()
    serverSMTP.login(from_address,"trivialidades")

    # Enviamos el mensaje
    serverSMTP.sendmail(from_address,to_address,mime_message.as_string())
 
    # Cerramos la conexion
    serverSMTP.close()
    




def webtotxt(webaddress,file):
    import re
    import urllib.request

    f = open(file, 'w')
    fhand = urllib.request.urlopen(webaddress)
    for line in fhand:
        f.write(line.decode())    
    f.close
    
    
def cotizar():
    import re
    import urllib


    fhand = urllib.urlopen('https://arxiv.org/list/cond-mat.str-el/recent')
    flag=-1
    coti=list()
    for line in fhand:
        textline=line.decode('utf-8','ignore')
        if flag > 0:
            n1=textline.find('<td>')
            n2=textline.find('</td>')
            coti.append(textline[n1+4:n2])
        flag=textline.find('Dolar U.S.A')
    return(coti)
