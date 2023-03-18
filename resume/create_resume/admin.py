from django.contrib import admin
from .models import profile,staff,jobvacancy,journal_publication,conference,patent,Rejected
# Register your models here.
admin.site.register(profile)
admin.site.register(staff)
admin.site.register(jobvacancy)
admin.site.register(journal_publication)
admin.site.register(conference)
admin.site.register(patent)
admin.site.register(Rejected)