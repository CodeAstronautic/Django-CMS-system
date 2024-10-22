# Generated by Django 3.0.1 on 2020-02-19 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tap_admin', '0014_auto_20200219_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Residential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_building', models.IntegerField()),
                ('no_of_floor', models.IntegerField()),
                ('no_of_1bhk', models.IntegerField()),
                ('no_of_2bhk', models.IntegerField()),
                ('no_of_3bhk', models.IntegerField()),
                ('no_of_4bhk', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tap_admin.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_floor', models.IntegerField()),
                ('no_of_office', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tap_admin.Project')),
            ],
        ),
    ]
