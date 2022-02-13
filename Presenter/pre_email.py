import smtplib

from email.mime.text import MIMEText
from Presenter import pre_auth


def send_email(data):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(pre_auth.email['email'], pre_auth.email['code'])

    msg = MIMEText('내용 : 본문내용 테스트입니다.')

    msg['Subject'] = '제목 : 메일 보내기 테스트입니다.'

    # 메일 보내기
    s.sendmail("3Line@news.com", "dban7171@gmail.com", msg.as_string())

    # 세션 종료
    s.quit()


    return





