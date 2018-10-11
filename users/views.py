""" User Views """

# Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    """ Login View """
	