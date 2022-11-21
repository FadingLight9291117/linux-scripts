import smtplib
from email.mime.text import MIMEText
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-m', '--message', type=str, default='test')
parser.add_argument('-t', '--to', type=str, default='')
args = parser.parse_args()

mail_cfg = dict(
    host='smtp.163.com',
    user='fadinglight9291117@163.com',
    password='MVANEXXPJMVYGXRP',
)

sender = 'fadinglight9291117@163.com'
if args.to == '':
    receiver = 'fadinglight9291117@126.com'
else:
    receiver = args.to

message = MIMEText(args.message, 'plain', 'utf-8')
message['Subject'] = '来自实验室主机-clz'
message['From'] = sender
message['To'] = receiver

with smtplib.SMTP() as smtp:
    smtp.connect(mail_cfg['host'])
    smtp.login(mail_cfg['user'], mail_cfg['password'])
    smtp.sendmail(sender, receiver, message.as_string())
    print(f'"{args.message}" -> {receiver}')
