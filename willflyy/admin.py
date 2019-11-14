from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AccessRecord,Topic,Webpage,profile
from .models import UserProfileInfo

# Register your models here.

# from .models import profilepic
admin.site.register(UserProfileInfo)
admin.site.register(profile)

# admin.site.register(neha)
# admin.site.register(Post)
# admin.site.register(profile)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
# admin.site.register(UserCreationForm)

