#Generate Certificates and Send directly to participants

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Globals 
sender_address = ' ' #your's email id
sender_pass = ' ' #email id password
base_dir = '  ' #path of folder on local machine


def send_certificates():
    session = setup_session()
    d1 = pd.read_csv('test.csv')
    name_list = d1["name"].tolist() 
    # print(name_list)
    for idx, item in enumerate(name_list):
        print(d1['email'][idx],'\n')
        if idx == 0:
            im = Image.open(base_dir + ' #image file name')
        elif idx == 1:
            im = Image.open(base_dir + '#image file name')
        elif idx == 2:
            im = Image.open(base_dir + '#image file name')
        elif idx < 10:
            im = Image.open(base_dir + '#image file name')
        else:
            im = Image.open(base_dir + '#image file name')
        d = ImageDraw.Draw(im)
        location = (189, 860)
        text_color = (0, 153, 255)
        selectFont = ImageFont.truetype("C:/WINDOWS/FONTS/SEGOEUI.TTF", 150)
        d.text(location, item, fill = ((text_color)), font = selectFont)
        file_name = item.replace(' ','').lower()
        im.save(base_dir + "certificates/" + file_name + ".png") #do create the folder with name certificates in base directory  
        send_mail(session, d1['email'][idx], item, 'certificates/%s.png' %file_name)
    close_session(session)



def send_mail(session, receiver_address, participant, file_name):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Certificate For Cyber Security Workshop'
    content = f''' Hello,
    Thank you for participating 
    # body of email
    ''' 
    #The body and the attachments for the mail
    message.attach(MIMEText(content, 'plain'))
    attach_file_dir = base_dir + file_name
    attach_file = open(attach_file_dir, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', "jpg", Name=file_name)
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    filename=file_name.replace("certificates/","")
    print(filename)
    payload.add_header("Content-Decomposition", "attachment",filename=attach_file_dir)
    message.attach(payload)
    #Create SMTP session for sending the mail
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)

def setup_session():
    session = smtplib.SMTP(host='smtp-mail.outlook.com', port=587) #use outlook with port # for gmail change host = smtp.google.com
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    return session

def close_session(session):
    session.quit
    return

if __name__ == '__main__':
    send_certificates()
    print('Done')
