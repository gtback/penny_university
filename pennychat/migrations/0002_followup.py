# Generated by Django 2.2.5 on 2019-11-09 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pennychat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
                ('user', models.TextField()),
                ('penny_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pennychat.PennyChat')),
            ],
        ),
    ]
