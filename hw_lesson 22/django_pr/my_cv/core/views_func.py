import smtplib


def send_email(message):
    sender = 'saiwa@mail.ru'
    password = 'NxevYYj5kS9EViGf9SGt'  # необходимо добавить новый пароль в настройках почты для работы
                                        # с ненадежными источниками

    with smtplib.SMTP("smtp.mail.ru", 465) as server:
        print("1")
        server.starttls()
        try:
            server.login(sender, password)
            server.sendmail(sender, sender, message)  # 2ой sender - mail куда хочу отправить сообщение

            return '<h1>The message was sent successfully</h1>'
        except Exception as _ex:
            return f'<h1>{_ex}\nCheck your login or password please!<h1>'

