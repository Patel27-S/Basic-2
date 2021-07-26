'''
The main function of this file is to teach how to send an email from email account from Python, 
without logging in, into the account to any given sender(s).
'''

import smtplib                                     # For sending emails using python.
import os                                          # To hide the contents such as email_address and passwords, using 'os' module.
from email.message import EmailMessage             # To have a better message process, we are import the class from shown module.
import imghdr                                      # We are importing this module to include multiple attachments to the mail we send.


# Let us access the environment variables (i.e. Email and Password):
EMAIL_ADDRESS = os.environ.get('Email_Address')
EMAIL_PASSWORD = os.environ.get('Email_Password')

# We have just created an object or EmailMessage() class below:
msg = EmailMessage()

# We are assigning the message details such as Sender and Receiver's email, Subject and content of message :
msg['Subject'] = 'Darshan of Maharaj!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'any_valid_address@email.com'
msg.set_content('Checkout the wonderful picture of Shree Hari that I have sent to you! Let me know how you like it!')


# Opening the below image in the same directory as our current file to
# learn how we send an image as an attachment to our message/email.
with open('1-harikrushna-Maharaj-3-scaled.jpg', 'rb') as img_of_maharaj:

    file_data = img_of_maharaj.read()

    # The 'what()' method of 'imghdr' module tells us the type of the file, 
    # when we pass file's name, as an argument. e.g. jpeg, png etc.                         
    file_type = imghdr.what(img_of_maharaj.name)
    file_name = img_of_maharaj.name

# Now, we want to send attachment to with the email, hence using 'add_attachment()' method :
msg.add_attachment(file_data, maintype= 'image', subtype = file_type, filename = file_name)



# Below, is the process, we are supposed to follow: 
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

   smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

   smtp.send_message(msg)
