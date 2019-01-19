from django.core.mail import send_mail


def registration_email(email):
    send_mail('TESZT', 'Udvozlunk a kszkepzesen, ne felejtsd el kitolteni a profilod.',
              'noreply@devteam.sch.bme.hu', [email, ])