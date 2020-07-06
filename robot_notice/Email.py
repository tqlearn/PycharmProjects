#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

global host
global user
global psw
host = 'smtp.exmail.qq.com'
user = 'automation.media@vhall.com'
psw='1qaz@WSX456'
def semail(userlist,cslist,sub,mes):
    send = '禅道小助手'+'<'+user+'>'#发件人邮箱
    #receivers = '765427508@qq.com'#收件人邮箱
    message = MIMEText(mes,'html','utf-8')
    message['From'] = send
    message['To'] = userlist
    message['Cc'] = cslist
    subject = sub
    message['Subject'] = Header(subject,'utf-8')
    #useremail = [userlist]+[cslist]
    try:
        em = smtplib.SMTP()
        em.connect(host,25)
        em.login(user,psw)
        em.sendmail(send,userlist.split(',') + cslist.split(','),message.as_string())
    except BaseException as e:
        print('异常'+str(e))


