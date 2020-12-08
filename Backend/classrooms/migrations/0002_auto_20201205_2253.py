# Generated by Django 3.1.4 on 2020-12-05 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects_classrooms',
            name='classroomID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='classrooms.classroom'),
        ),
    ]