# Generated by Django 3.2.22 on 2023-11-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
                ('date_sent', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_sent'],
            },
        ),
    ]