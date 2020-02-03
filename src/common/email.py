from django.core.mail import send_mail
import codecs

sender_email = 'noreply@ujonc.sch.bme.hu'
link = 'https://ujonc.sch.bme.hu/homework'


def read_email(name):
    with codecs.open('common/emails/' + name, 'r', 'utf-8') as myfile:
        data = myfile.read()
    return data


def registration(user):
    subject = "Kszképzés regisztráció"
    message = read_email('registration.txt')
    message = str.format(message % {'name': user.get_full_name()})
    send_mail(subject, message, sender_email, [user.email, ])


def admitted(user):
    subject = "Jelentkezés eredménye"
    message = read_email('admitted.txt')
    message = str.format(message % {'name': user.get_full_name()})
    send_mail(subject, message, sender_email, [user.email, ])


def denied(user):
    subject = "Jelentkezés eredménye"
    message = read_email('denied.txt')
    message = str.format(message % {'name': user.get_full_name()})
    send_mail(subject, message, sender_email, [user.email, ])


def new_homework(user, deadline):
    deadline = deadline.strftime('%Y-%m-%d %H:%M')
    subject = "Új házifeladat"
    message = read_email('new_homework.txt')
    message = str.format(
        message % {'name': user.get_full_name(), 'link': link, 'deadline': deadline})
    send_mail(subject, message, sender_email, [user.email, ])


def homework_corrected(user, title, accepted):
    subject = "Házifeladat eredménye"
    if accepted:
        status = 'Elfogadva'
    else:
        status = 'Hibás'
    message = read_email('homework_corrected.txt')
    message = str.format(message % {'name': user.get_full_name(
    ), 'link': link, 'status': status, 'title': title})
    send_mail(subject, message, sender_email, [user.email, ])
