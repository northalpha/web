"""filechecker.py
author: https://twitter.com/northalpha
desc: A simple file checker if a file is present in a directory / is beeing uploaded send me an email"""

import glob
import sys
import os
import smtplib

### Config ###
#my_email = "mymailadresse@gmail.com"
#my_pass = "super_secret_in_here"
my_folder = "/tmp/"
my_filetypes = "tmp"

my_folderfiles = my_folder + "*." + my_filetypes

print(my_folderfiles)

def list_files(folder):
	return ', '.join(map(str, (glob.glob(folder) )))

#debug
filenames=list_files(my_folderfiles)
print( filenames )

def sendMail(mail_content):
#Creats  an Server Object
	server = smtplib.SMTP('smtp.gmail.com', 587)
       	#Do the TLS server connection
       	server.starttls()
       	#Next, log in to the server
      	server.login(my_email, my_pass)
       	#Send the mail
#      	content = "\n" + mail_content # The /n separates the message from the headers
       	server.sendmail("filesystemchecker@gmail.com", my_email , mail_content)
       	server.quit()

#sendMail(filenames) 
