import threading
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from Trello.settings import EMAIL_HOST_USER
from Trello.utils.main_utils import unique_code
from authentication.models import Token


class SendHtmlMessageAsync(threading.Thread):
    def __init__(self, sender=None, receiver=None, subject=None, html_content=None):
        super(SendHtmlMessageAsync, self).__init__()
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.html_content = html_content

    def run(self) -> None:
        email = EmailMessage(
            subject=self.subject,
            from_email=self.sender,
            body=self.html_content,
            to=self.receiver
        )
        email.content_subtype = "html"
        email.send()


def send_html_mail_async(sender=None, receiver=None, subject=None, template_name=None, content=None) -> None:
    sender = EMAIL_HOST_USER
    html_data = render_to_string(template_name, context=content)
    email = SendHtmlMessageAsync(sender=sender, receiver=receiver, subject=subject, html_content=html_data)
    email.start()


def send_activation_code(user):
    token = unique_code()
    send_html_mail_async(receiver=[user.email, ],
                         subject='Activation Link',
                         template_name='mail/verification.html',
                         content={'token': token})
    instance = Token(user=user, token=token)
    instance.save()
