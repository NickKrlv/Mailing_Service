from smtplib import SMTPException
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
import logging

from mailing.models import MailingService, Logs, Client

logger = logging.getLogger(__name__)


def send_mailing(mailing):
    now = timezone.localtime(timezone.now())
    results = []

    if mailing.start_time <= now <= mailing.end_time:
        for message in mailing.message_set.all():
            for client in mailing.clients.all():
                try:
                    result = send_mail(
                        subject=message.title,
                        message=message.text,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                        fail_silently=False
                    )

                    log = Logs.objects.create(
                        last_try=timezone.now(),
                        status=(result == 1),
                        server_response='OK',
                        mailing=mailing,
                        client=client
                    )
                    log.save()
                    results.append(log)
                except SMTPException as error:
                    log = Logs.objects.create(
                        last_try=timezone.now(),
                        status=False,
                        server_response=str(error),
                        mailing=mailing,
                        client=client
                    )
                    log.save()
                    results.append(log)
                    logger.error(f"Error sending email to {client.email}: {error}")

    else:
        mailing.status = MailingService.finished
        mailing.save()

    return results
