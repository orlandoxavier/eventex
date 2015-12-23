from django.shortcuts import render

from django.core.mail import send_mail

# Create your views here.
def home(request):
    mail_from = 'visitantes@eventex-orlandoxavier.herokuapp.com'
    mail_to = 'orlandoxavier.sh@gmail.com'
    ip = request.META.get('REMOTE_ADDR')

    send_mail('Novo Visitante no Eventex', 'IP: ' + ip, mail_from,
              [mail_to], fail_silently=False)

    return render(request, 'index.html')