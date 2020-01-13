from flask_mail import Message
from . import mail
from flask import render_template, current_app


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject=app.config['MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['MAIL_SENDER'], recipients=[to])

    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)

    with app.app_context():
        mail.send(msg)
