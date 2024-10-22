# Generated by Django 5.1.2 on 2024-10-21 07:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=250)),
                ('description', models.CharField(default=None, max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='', max_length=200)),
                ('placeholder', models.CharField(default='', max_length=200)),
                ('required', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('text', 'text'), ('checkbox', 'checkbox'), ('radio', 'radio'), ('date', 'date'), ('dropdown', 'dropdown'), ('number', 'number')], default='text', max_length=20)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formhandler.form')),
            ],
        ),
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_responses', models.JSONField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formhandler.form')),
            ],
        ),
    ]