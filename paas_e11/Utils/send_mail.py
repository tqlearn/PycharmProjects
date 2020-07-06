#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:chengyanan
@file: send_mail.py
@time: 2020/1/22  12:19 下午
"""
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import os
from email.mime.multipart import MIMEMultipart
report_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
class sendMail:
    def sen_mail(self):
        '''
            发送邮件内容
      :param to_user:发送邮件的人
      :param sub:主题
      :param content:邮件内容
            '''
        smtpserver = 'smtp.qq.com'  # 发件服务器
        port = 465
        send_user = '316835981@qq.com'  # 发送端
        to_user = ['13439875784@163.com', 'zhebo.lin@vhall.com']  # 接收端
        # =========编辑邮件内容=========
        report_dir = report_path + r"/report/report.html"
        f = open(report_dir, 'rb')
        mail_body = f.read()
        f.close()
        msg = MIMEMultipart()
        msg['Subject'] = '接口自动化测试报告'  # 主题
        msg['From'] = send_user  # 发件人
        msg['To'] = ','.join(to_user)  # 收件人
        text = MIMEText(mail_body, 'html', 'utf-8')
        text['Subject'] = Header('接口自动化自动化测试报告', 'utf-8')  # 定义文件正文标题
        msg.attach(text)
        # -------附件------------
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att.add_header('Content-Disposition', 'attachment', filename='接口自动化测试报告.html')  # 定义附件名称
        msg.attach(att)  # 添加附件

        # 发送xlsx

        api_result = report_path + r"/report/api_result.xlsx"
        att2 = MIMEText(open(api_result, 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2.add_header('Content-Disposition', 'attachment', filename='接口测试具体报告.xlsx')
        msg.attach(att2)

        # 发送
        server = smtplib.SMTP_SSL(smtpserver, port)
        server.login(send_user, 'zbfbslvwmlprbjhb')
        server.sendmail(send_user, to_user, msg.as_string())
        server.close()