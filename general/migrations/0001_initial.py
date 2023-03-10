# Generated by Django 4.1.7 on 2023-03-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('readonly', models.BooleanField(default=False)),
                ('maintenance', models.BooleanField(default=False)),
                ('down', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'mode',
                'verbose_name_plural': 'mode',
                'db_table': 'mode',
                'ordering': ('id',),
            },
        ),
    ]
