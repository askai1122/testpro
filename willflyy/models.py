from django.db import models

# Create your models here.
from django.db import models
from django import forms
# from django.contrib.auth.models import User
# 
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	

	picture = models.ImageField(upload_to='profile_pics')

	def __str__(self):

		return self.user.username

class Post(models.Model):
    subject = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='profile_pics', null=True)
    msg = models.TextField()
    # cr_date = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):

        return  self.subject

class Topic(models.Model):
	top_name = models.CharField(max_length=264,unique=True)


	def  __str__(self):
		return self.top_name


class Webpage(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

	name = models.CharField(max_length=264, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
	date = models.DateField()

	def __str__(self):
		return str(self.date)
# class UserCreationForm(forms.ModelForm):
# 	password1 = forms.CharField(label=_("Password"),
# 		widget = forms.PasswordInput),
# 	password2 = forms.CharField(label=_("Password DONT MATCH"),
# 		widget = forms.PasswordInput),
# 		# help_text =_("Enter the same password as above, for verfication"),

# 	class Meta:
# 		model = User
# 		fields = ("username",)	


class profile(models.Model):
    pic = models.ImageField(upload_to='profile_pics',)

