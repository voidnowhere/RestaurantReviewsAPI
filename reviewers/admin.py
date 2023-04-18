from django.contrib import admin
from reviewers.models import *
# Register your models here.

admin.site.register(Reviewer)
admin.site.register(Rating)
admin.site.register(Restaurant)
admin.site.register(Customer)
