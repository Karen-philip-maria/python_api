# Generated by Django 4.2.13 on 2024-07-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_students_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pic',
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_code',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_code',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
