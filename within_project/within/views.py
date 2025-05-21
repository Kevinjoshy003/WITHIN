from django.shortcuts import render, redirect
from .models import MoodEntry
from .forms import MoodEntryForm

def home(request):
    return render(request, 'within/home.html')

def log_mood(request):
    if request.method == 'POST':
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mood_history')
    else:
        form = MoodEntryForm()
    return render(request, 'within/log_mood.html', {'form': form})

def mood_history(request):
    moods = MoodEntry.objects.order_by('-timestamp')
    return render(request, 'within/mood_history.html', {'moods': moods})

