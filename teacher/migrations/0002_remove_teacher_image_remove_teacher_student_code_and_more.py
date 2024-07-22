# Generated by Django 4.2.13 on 2024-07-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='image',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='student_code',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_code',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='immediate_contact',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(),
        ),
    ]
