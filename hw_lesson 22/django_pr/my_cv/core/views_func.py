import smtplib, ssl


def send_email(message):
    sender = ''
    password = 'NxevYYj5kS9EViGf9SGt'  # необходимо добавить новый пароль в настройках почты для работы
                                        # с ненадежными источниками

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.mail.ru", 465, context=context) as server:
        try:
            server.login(sender, password)
            server.sendmail(sender, sender, message)  # 2ой sender - mail куда хочу отправить сообщение

            return '<h1>The message was sent successfully</h1>'
        except Exception as _ex:
            return f'<h1>{_ex}\nCheck your login or password please!<h1>'

