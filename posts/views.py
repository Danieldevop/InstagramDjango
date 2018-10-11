""" Post views """

# Django 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Utilities
from datetime import datetime


posts = [
  {
    'title': 'Traveling Italy',
    'user': {
      'name': 'Daniel sepulveda',
      'profile_pic': 'https://upload.wikimedia.org/wikipedia/commons/f/fc/Nemer_Saade_Profile_Picture.jpg',
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://source.unsplash.com/random/800x600',
  },
  {
    'title': 'Traveling Argentina',
    'user': {
      'name': 'Jessyca Dominguez',
      'profile_pic': 'http://sms.latestsms.in/wp-content/uploads/profile-pictures231.jpg',
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://source.unsplash.com/random/800x600',
  },
  {
    'title': 'Travel from Mexico',
    'user': {
      'name': 'Diana Perez',
      'profile_pic': 'https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2015/10/shutterstock_147173813.jpg',
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
    'photo': 'https://source.unsplash.com/random/800x600',
  },
]

@login_required
def list_posts(request):
  return render(request, 'posts/feed.html', {'posts': posts})