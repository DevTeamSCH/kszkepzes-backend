from django.core.mail import send_mail


def registration(email):
    subject = "REGISTRATION TEST"
    message = "Üdvözlünk a kszképzésen!"
    send_mail(subject, message, 'noreply@devteam.sch.bme.hu', [email, ])


def admitted(email):
    subject = "ADMITTED TEST"
    message = "Gratulálunk, te vagy a kiválasztott!!"
    send_mail(subject, message, 'noreply@devteam.sch.bme.hu', [email, ])


def denied(email):
    subject = "DENIED TEST"
    message = "Sajnos idén nem nyertél felvételt, próbáld meg legközelebb"
    send_mail(subject, message, 'noreply@devteam.sch.bme.hu', [email, ])


def new_homework(email):
    subject = "NEW HOMEWORK TEST"
    message = "Szia!\nEgy új házi lett kiadva, ha tíz percen belül megoldod akkor fasza gyerek vagy," \
              " ha nem életed végéig bánnifogod..."
    send_mail(subject, message, 'noreply@devteam.sch.bme.hu', [email, ])


def homework_corrected(email):
    subject = "HOMEWORK CORRECTED TEST"
    message = "Nagyszerű mentoraink kijavították házifeladatod, vajon most kaptál meglepit?!"
    send_mail(subject, message, 'noreply@devteam.sch.bme.hu', [email, ])
