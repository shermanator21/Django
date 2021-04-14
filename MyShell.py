#import os
from MainApp.models import Topic, Entry
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

#import django
django.setup()

#from MainApp.models import Topic, Entry

topics = Topic.objects.all()
entries = Entry.objects.all()

t = Topic.objects.get(id=1)  # delete this line if u want all ids
print(t)
entry = t.entry_set.all()

for t in topics:
    # calls string method in models file in topic class
    print(f"Topic ID: {t.id} and Topic Name: {t}")
    print(f"Date added: {t.date_added}")

for e in entries:
    print(f"Topic: {e.topic}")
    print(f"Entry: {e.text}")
