from django.shortcuts import render

# chat/views.py

from django.shortcuts import render

def room(request, room_name):
    return render(request, 'index.html', {
        'room_name': room_name
    })
