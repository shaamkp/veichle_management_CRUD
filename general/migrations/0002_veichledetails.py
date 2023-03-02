# Generated by Django 4.1.7 on 2023-03-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VeichleDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=128)),
                ('veichle_type', models.CharField(choices=[('two_wheeler', 'Two_Wheeler'), ('three_wheeler', 'Three_Wheeler'), ('four_wheeler', 'Four_Wheeler')], max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Veichle Detail',
                'verbose_name_plural': 'Veichle Details',
                'db_table': 'general_veichle_details',
                'ordering': ('id',),
            },
        ),
    ]
