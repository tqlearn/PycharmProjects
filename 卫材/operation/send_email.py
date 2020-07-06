#coding:utf-8

import smtplib
from email.mime.text import MIMEText

class SendEmail(object):
    email_add = "979355402@qq.com"
    host = 'smtp.qq.com'
    password = 'tiplsrvvqemhbcbb'

    def send_emial(self,to_list,sub,content):
        from_user = "tianqi" + "<" + self.email_add + ">"
        message = MIMEText(content,_charset="utf-8")
        message["Subject"] = sub
        message["From"] = from_user
        message["To"] = ";".join(to_list)

        server = smtplib.SMTP()
        server.connect(self.host)
        server.login(self.email_add,self.password)
        server.sendmail(from_user,to_list,message.as_string())
        server.close()

if __name__ == "__main__" :
    to = ["qi.tian@vhall.com","bp.wangyan@vhallops.com"]
    sub = "请忽略"
    content = "测试邮件是否可发送"
    SendEmail().send_emial(to,sub,content)


