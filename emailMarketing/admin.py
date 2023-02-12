from django.contrib import admin

from emailMarketing.models import ContactFormModel, Subscription

admin.site.register(ContactFormModel)
admin.site.register(Subscription)
