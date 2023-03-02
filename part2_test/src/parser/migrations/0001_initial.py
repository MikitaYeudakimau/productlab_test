# Generated by Django 4.1.7 on 2023-03-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
