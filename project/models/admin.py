from django.contrib import admin

from models import (Account, Activity, Bill,
                        Categoty, Problem, Cause, Solution, Response, Rebuttal, Fact, Hashtag, Invitation,
                        Notification, Rationale, Rebuttal,
                        Representative, Response, Thread, Vote)

models = [Account, Activity, Bill,
         Categoty, Problem, Cause, Solution, Response, Rebuttal, Fact, Hashtag, Invitation,
         Notification, Rationale, Rebuttal,
         Representative, Response, Thread, Vote]

for model in models:
    admin.site.register(model)
