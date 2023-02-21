from django.contrib import admin

from monand.otp_auth.models import MyUser

admin.site.register(MyUser)