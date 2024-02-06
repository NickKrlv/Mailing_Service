from mailing.services import send_mailing
from mailing.models import MailingService


def daily_tasks():
    mailings = MailingService.objects.filter(mailing_period="Раз в день", status="Рассылка запущена")
    print(mailings)
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def weekly_tasks():
    mailings = MailingService.objects.filter(mailing_period="Раз в неделю", status="Рассылка запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def monthly_tasks():
    mailings = MailingService.objects.filter(mailing_period="Раз в месяц", status="Рассылка запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)