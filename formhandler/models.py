import uuid
from django.db import models
from django.contrib.auth.models import User

# Form Model
class Form(models.Model):
    # Foreign Key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Normal Attributes
    title = models.CharField(max_length=250, default=None)
    description = models.CharField(max_length=500, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Choices
FIELD_TYPE_CHOICES = [
    ('text', 'Text'),
    ('checkbox', 'Checkbox'),
    ('radio', 'Radio'),
    ('date', 'Date'),
    ('dropdown', 'Dropdown'),
    ('number', 'Number')
]

class FormField(models.Model):
    # Foreign Key
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    # Normal Attributes
    label = models.CharField(max_length=200, default='')
    placeholder = models.CharField(max_length=200, default='')
    required = models.BooleanField(default=False)
    type = models.CharField(
        max_length=20,
        choices=FIELD_TYPE_CHOICES,
        default=FIELD_TYPE_CHOICES[0][0]
    )

class FormSubmission(models.Model):
    # Foreign Key
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    # Normal Attributes
    form_responses = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission for {self.form.title} at {self.submitted_at}"
