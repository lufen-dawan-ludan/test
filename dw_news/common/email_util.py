import smtplib
from email.mime.text import MIMEText


smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com',25)
smtp.login('907999314@qq.com','bykjwuwsrgktbfdd')


email_content = '邮件正文'
msg = MIMEText(email_content,'html','utf-8')   # 邮件的属性，编码方式
msg['from'] = '907999314@qq.com'              # sender
msg['to'] = '735013288@qq.com'                # recieve
msg['Cc'] = '3500822663@qq.com'                # 抄送者
msg['subject'] = '测试邮件'                    # 邮件主题

# 带HTML附件的邮件
'''
msg = MIMEMultipart()
email_content = 'from newdream test...'
msg.attach( MIMEText(email_content,'html','utf-8') )

attach_file_path = os.path.join( os.path.dirname(__file__),'API_TEST_V2.0.html' )   # 附件位置
attach_file_obj = MIMEText( open(attach_file_path,'rb').read(),'base64','utf-8' )   # 附件对象
attach_file_obj['Content-Type'] = 'application/octet-stream'                        # 附件的头信息
attach_file_obj.add_header('Content-Disposition','atachment',
                           filename=('gbk','',os.path.basename(attach_file_path)))
msg.attach( attach_file_obj )


smtp.sendmail('907999314@qq.com',['735013288@qq.com','3500822663@qq.com'],msg.as_string()) #发件人、收件人

smtp.close()
'''

smtp.sendmail('907999314@qq.com',['735013288@qq.com','3500822663@qq.com'],msg.as_string())
smtp.close()


