from django.shortcuts import render
import time

from apscheduler.schedulers.background import BackgroundScheduler
import feedparser
from .models import Feed

from django.views import View
# Create your views here.

scheduler = BackgroundScheduler()

def job_function():
    feed = feedparser.parse('http://www.zone-h.org/rss/specialdefacements')
    entries = []
    for entry in feed.entries:
        entries.append({
            'title' : entry.title,
            'link' : entry.link,
            'published' : entry.published
        })
    print('task is running')


scheduler.add_job(job_function, 'interval', seconds=60*2)

scheduler.start()

def feed_view(request):
    feed = feedparser.parse('http://www.zone-h.org/rss/specialdefacements')
    entries = []
    for entry in feed.entries:
        entries.append({
            'title' : entry.title,
            'link' : entry.link,
            'published' : entry.published
        })
    context = {'data' : entries}
    return render(request, 'Function/feed.html', context)