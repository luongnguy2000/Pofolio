# Generated by Django 4.0.6 on 2022-07-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skill',
            new_name='Skills',
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
