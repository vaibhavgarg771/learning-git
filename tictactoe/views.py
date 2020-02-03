from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def welcome(request):
    if request.user.is_authenticated: 
        return redirect('player_home')
    else:
        return render(request, 'tictactoe/welcome.html')