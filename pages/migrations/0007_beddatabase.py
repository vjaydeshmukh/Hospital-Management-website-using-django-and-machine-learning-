# Generated by Django 2.1.2 on 2019-04-08 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20190407_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='BedDataBase',
            fields=[
                ('Bedname', models.CharField(default='unknown', max_length=100, primary_key=True, serialize=False)),
                ('Male_ward', models.IntegerField(default=0)),
                ('Female_ward', models.IntegerField(default=0)),
                ('Deluxe_bed', models.IntegerField(default=0)),
                ('Private_bed', models.IntegerField(default=0)),
                ('General_bed', models.IntegerField(default=0)),
                ('Bed_status', models.IntegerField(default=0)),
            ],
        ),
    ]
