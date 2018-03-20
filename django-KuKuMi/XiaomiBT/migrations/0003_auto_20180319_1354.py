# Generated by Django 2.0.2 on 2018-03-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('XiaomiBT', '0002_hub'),
    ]

    operations = [
        migrations.CreateModel(
            name='XiaomiBT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=200, unique=True)),
                ('iface', models.CharField(max_length=17, unique=True)),
                ('threshold', models.CharField(max_length=17, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Hub',
        ),
    ]