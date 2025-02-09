from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from mailsender.models import Mailing


class Command(BaseCommand):
    help = 'Отправка рассылки'

    def add_arguments(self, parser):
        parser.add_argument('mailing_id', type=int, help='ID рассылки, которую нужно отправить')

    def handle(self, *args, **kwargs):
        mailing_id = kwargs['mailing_id']
        mailing = Mailing.objects.get(pk=mailing_id)

        for recipient in mailing.addressees.all():
            send_mail(
                mailing.message.subject,
                mailing.message.body,
                'Tema024ru@yandex.ru',
                [recipient.email],
                fail_silently=False,
            )

        mailing.status = Mailing.LAUNCHED
        mailing.save()
        self.stdout.write(self.style.SUCCESS(f'Рассылка "{mailing.message.subject}" успешно отправлена!'))
