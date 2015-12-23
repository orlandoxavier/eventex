from django.shortcuts import render


# Create your views here.
def home(request):
    ip = request.META.get('REMOTE_ADDR')

    if ip == '127.0.0.1':
        mail_from = 'eventex@xavier.local'
        mail_to = 'orlandoxavier.sh@gmail.com'

        from django.core.mail import send_mail
        send_mail('Novo Visitante no Eventex', 'IP: ' + ip, mail_from, [mail_to], fail_silently=False)

    return render(request, 'index.html')