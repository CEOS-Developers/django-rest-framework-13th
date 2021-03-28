# Generated by Django 3.1.7 on 2021-03-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='written',
            new_name='text',
        ),
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(null=True, upload_to='profile_img'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_num',
            field=models.TextField(default='010-0000-0000', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='comment',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
