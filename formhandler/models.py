from django.db import models
from django.contrib.auth.models import User

# Form Model
class Form(models.Model):
    # Foreign Key
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # Normal Attributes
    title = models.CharField(max_length=250,default=None)
    description = models.CharField(max_length=500,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Choices
FIELF_TYPE_CHOICES =[
    ('text','text'),
    ('checkbox','checkbox'),
    ('radio','radio'),
    ('date','date'),
    ('dropdown','dropdown'),
    ('number','number')
]

class FormField(models.Model):
    # Foreign Key
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    # Normal Attributes
    label = models.CharField(max_length=200,default='')
    placeholder = models.CharField(max_length=200,default='')
    required = models.BooleanField(default=False)
    type = models.CharField(
        max_length=20,
        choices=FIELF_TYPE_CHOICES,
        default=FIELF_TYPE_CHOICES[0][0]
    )

class FormSubmission(models.Model):
    # Foreign Key
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    # Normal Attributes
    form_responses = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)

