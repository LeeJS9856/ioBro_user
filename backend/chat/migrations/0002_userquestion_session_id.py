# Generated by Django 4.2.12 on 2024-12-16 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestion',
            name='session_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]