from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm
import requests

def index(request):
    return render(request, 'Movies/index.html')


# Register Route - redirects them to the home page
def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account is now active. you may log in!')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request,'Movies/register.html', {'form': form})


 # Route that allows users to update their profile
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'Movies/profile.html',context)


# User must be logged in to view movie details, this route makes another API request to OMDB
# Takes the imdb id from URL and makes a request to API save it into a movie object
@login_required
def detail(request,id):
    response = requests.get('http://www.omdbapi.com/?apikey=4926b9e0&i='+ id +'&plot=full')
    movie = response.json()
    print(movie) # Print API Object to console for specific movie
    return render(request, 'Movies/detail.html', {
        'Title': movie['Title'],
        'Year': movie['Year'],
        'Rated': movie['Rated'],
        'Runtime': movie['Runtime'],
        'Released': movie['Released'],
        'Genre': movie['Genre'],
        'Poster': movie['Poster'],
        'Plot': movie['Plot'],
        'imdbRating': movie['imdbRating'],
        'Awards' :movie['Awards'],
        'Language': movie['Language'],
        'Country': movie['Country'],
        'Actors': movie['Actors'],
        'Writer': movie['Writer'],
        'Director': movie['Director'],
    })










