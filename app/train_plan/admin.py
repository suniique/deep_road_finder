from django.contrib import admin

from app.train_plan.models import Repository, Plan, Trial

admin.site.register(Repository)
admin.site.register(Plan)
admin.site.register(Trial)
