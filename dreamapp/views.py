import json

from django.contrib.auth.password_validation import password_changed
from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor.requests.auth import HTTPBasicAuth
from dreamapp.models import Message,NewUser
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth
import random
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import NewUser
from django.shortcuts import render, redirect
from django.contrib import messages


import urllib.request
import urllib.parse


def index(request):
    if request.method == 'POST':
        if NewUser.objects.filter(
            email = request.POST['email'],
            password = request.POST['password'],
        ).exists():
            return render(request, 'index.html')
        else:
            print('Invalid credentials')
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        if 'email' in request.session:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')



def about(request):
   return  render(request, 'about.html')

def agents(request):
    return render(request, 'agents.html')

def contact(request):
    if request.method == 'POST':
       mymessage = Message(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
       mymessage.save()
       return redirect('/contact/')
    else:
        return render(request, 'contact.html')

def properties(request):
    return render(request, 'properties.html')

def singleProperty(request):
    return render(request, 'kitengela.html')

def servicedetails(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')

def hunting(request):
    return render(request, 'hunting.html')

def listing(request):
    return render(request, 'listing.html')

def marketing(request):
    return render(request, 'marketing.html')

def negotiation(request):
    return render(request, 'negotiation.html')

def transaction(request):
    return render(request, 'transaction.html')

def valuation(request):
    return render(request, 'valuation.html')

def login(request):
    return render(request, 'login.html')

#def newproperty(request):
    #return render(request, 'newproperty.html')

def registration(request):
    if request.method == 'POST':
        users = NewUser(
            name = request.POST['name'],
            email = request.POST['email'],
            password = request.POST['Password'],

        )
        users.save()
        return redirect('/login/')

    else:
        return render(request, 'registration.html')


# email verification via OTP
def send_otp(email):
    otp = str(random.randint(100000, 999999))
    send_mail(
        subject='Dreamscape Realty - Email Verification OTP',
        message=f'Your verification code is: {otp}',
        from_email='noreply@dreamscape.com',
        recipient_list=[email],
    )
    return otp

def otp(request):
    if request.method == 'POST':
        email = request.session.get('email')
        otp_input = request.POST['otp']
        user = get_object_or_404(NewUser, email=email)

        if user.otp == otp_input:
            user.is_verified = True
            user.otp = None
            user.save()
            messages.success(request, 'Email verified! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP. Try again.')

    return render(request, 'otp.html')



def runda(request):
    return render(request, 'runda.html')

def karenHardy(request):
    return render(request, 'karenHardy.html')

def kilimani(request):
    return render(request, 'kilimani.html')

def westlands(request):
    return render(request, 'westlands.html')

def kitsuru(request):
    return render(request, 'kitsuru.html')


def kitengela(request):
    return render(request, 'kitengela.html')

def pay(request):
    return render(request, 'pay.html')



def token(request):
    consumer_key = 'fBoRa5VYfKNni9LyRkAwXyCnO6JfG3iLNyi0L5ZpqN4a0pm3'
    consumer_secret = '7UeGixT9YIWAVmskV0ErEy2sNcPlb4F4I1rSxG3yNbo2ZU0BAICxEewe2KrqdBPq'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')


class MpesaAccessToken:
    validated_mpesa_access_token = None


class LipanaMpesaPpassword:
    lipa_time = None
    decode_password = None
    Business_short_code = None


def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Dreamscape Realty",
            "TransactionDesc": "Payment for Property Booking"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("success! Follow the prompt to complete your payment")


