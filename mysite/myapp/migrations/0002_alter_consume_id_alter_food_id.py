# Generated by Django 5.0.4 on 2024-04-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consume',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='food',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
