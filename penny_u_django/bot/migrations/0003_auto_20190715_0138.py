# Generated by Django 2.2.3 on 2019-07-15 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20190714_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slack_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]