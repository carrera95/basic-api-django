# Generated by Django 5.1.2 on 2024-11-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='uncripted_pswd',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
