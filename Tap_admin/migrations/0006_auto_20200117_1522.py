# Generated by Django 3.0.1 on 2020-01-17 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20200103_1132'),
        ('Tap_admin', '0005_project_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.ManagerProfile'),
        ),
    ]