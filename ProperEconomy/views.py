from django.shortcuts import render
from .models import ClientInfo
from django.core.mail import send_mail
# 
def properEconomyView(request):
    print(request)
    if request.method == 'POST':
        name = request.POST['fname']
        phone = request.POST['phone']
        clientInfo = ClientInfo(name=name, phone=phone)
        clientInfo.save()
        print ('save data', name, phone)
        send_mail(subject='ליד כלכלה נכונה', message='שם: ' + name + ' טלפון: ' + phone, from_email='bot@ms-global.co.il', recipient_list=['m.sglobalwork@gmail.com'])
    return render(request, 'properEconomy.html', {})