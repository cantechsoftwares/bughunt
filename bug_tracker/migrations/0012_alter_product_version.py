# Generated by Django 4.0.4 on 2023-03-28 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug_tracker', '0011_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='version',
            field=models.CharField(max_length=100),
        ),
    ]
