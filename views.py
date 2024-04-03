from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def api_games(request):
    # Connect to the database and query the games table
    # Return the data as JSON
    pass

def api_add_game(request):
    # Get the data from the request
    # Insert the data into the database
    # Return the data as JSON
    pass

def api_edit_game(request, game_id):
    # Get the data from the request
    # Update the data in the database
    # Return the data as JSON
    pass

def api_delete_game(request, game_id):
    # Delete the data from the database
    # Return the dataas JSON
    pass