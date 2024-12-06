from django.contrib import admin
from dreamapp.models import NewUser, Member, Payment, Message
# Register your models here.

admin.site.register(NewUser)
admin.site.register(Member)
admin.site.register(Payment)
admin.site.register(Message)
