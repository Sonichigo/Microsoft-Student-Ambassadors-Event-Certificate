import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Globals 
sender_address = 'kiit.mspc@outlook.com'
sender_pass = 'msackiit@1234'
base_dir = 'C:/Users/KIIT/Desktop/CYBER/'


def send_certificates():
    session = setup_session()
    d1 = pd.read_csv('test.csv')
    name_list = d1["name"].tolist() 
    # print(name_list)
    for idx, item in enumerate(name_list):
        print(d1['email'][idx],'\n')
        if idx == 0:
            im = Image.open(base_dir + 'c1.png')
        elif idx == 1:
            im = Image.open(base_dir + 'c1.png')
        elif idx == 2:
            im = Image.open(base_dir + 'c1.png')
        elif idx < 10:
            im = Image.open(base_dir + 'c1.png')
        else:
            im = Image.open(base_dir + 'c1.png')
        d = ImageDraw.Draw(im)
        location = (189, 860)
        text_color = (0, 153, 255)
        selectFont = ImageFont.truetype("C:/WINDOWS/FONTS/SEGOEUI.TTF", 150)
        d.text(location, item, fill = ((text_color)), font = selectFont)
        file_name = item.replace(' ','').lower()
        im.save(base_dir + "certificates/" + file_name + ".png")
        send_mail(session, d1['email'][idx], item, 'certificates/%s.png' %file_name)
    close_session(session)



def send_mail(session, receiver_address, participant, file_name):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Certificate For Cyber Security Workshop'
    content = f''' Hello,
    Thank you for participating in Cyber Security Workshop organised by KIIT KAKSHA with MSAC KIIT.
    We have attached your certificate in this mail. After getting the Certificates fill out this too:- https://bit.ly/2NsojsN \n
    Link for recording:-https://www.youtube.com/watch?v=lG-JFVp5YTQ \n
    Resources link:-https://docs.google.com/presentation/d/1Ed-FZP5zW-7kvIA3URbBd4u_vna_Sv8f1oDvh8fpUBU/edit?usp=sharing
    \nThank you
    \n\n Regards \n KIIT KAKSHA & MSAC KIIT \n
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
    session = smtplib.SMTP(host='smtp-mail.outlook.com', port=587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    return session

def close_session(session):
    session.quit
    return

if __name__ == '__main__':
    send_certificates()
    print('Done')