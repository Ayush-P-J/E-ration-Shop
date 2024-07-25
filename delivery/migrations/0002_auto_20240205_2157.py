# Generated by Django 3.2.11 on 2024-02-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_TB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=500)),
                ('District', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=500)),
                ('Dproof', models.ImageField(upload_to='dproof_DB')),
                ('Mincharge', models.IntegerField()),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Delivery_DB',
        ),
    ]
