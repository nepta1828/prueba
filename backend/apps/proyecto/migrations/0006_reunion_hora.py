# Generated by Django 3.0.7 on 2020-06-29 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0005_auto_20200628_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='reunion',
            name='hora',
            field=models.CharField(default='00:00', max_length=10),
        ),
    ]