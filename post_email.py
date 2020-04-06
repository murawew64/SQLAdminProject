import smtplib


def send_notification(to_item, txt):
    sender = 'muraview.anton@yandex.ru'
    sender_password = 'Aa4LEH72'
    mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    mail_lib.login(sender, sender_password)
    msg = ('From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' + txt) % (
        sender, to_item, 'Contact')
    mail_lib.sendmail(sender, to_item, msg.encode('utf8'))
    mail_lib.quit()
