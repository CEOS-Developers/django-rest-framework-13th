# Generated by Django 3.0.8 on 2021-03-30 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='api.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='root',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_comment', to='api.Comment'),
        ),
        migrations.AlterField(
            model_name='file',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='api.Post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='liker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_likes', to='api.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
