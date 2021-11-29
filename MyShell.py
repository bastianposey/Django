import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

for topic in topics:
    print(topic.id)
    print(topic.text)
    print(topic.date_added)

t = Topic.objects.get(id=1)
print(t)

entries = t.entry_set.all()

for e in entries:
    print(e)