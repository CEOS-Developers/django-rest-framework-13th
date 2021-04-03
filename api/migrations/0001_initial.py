# Generated by Django 3.1.7 on 2021-03-31 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100, unique=True, verbose_name='닉네임')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('phone_number', models.CharField(max_length=100, unique=True, verbose_name='전화번호')),
                ('password', models.CharField(max_length=150, unique=True, verbose_name='비밀번호')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='이름')),
                ('description', models.TextField(verbose_name='소개')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='가입일자')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트일자')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('content', models.TextField(verbose_name='소개')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='업로드일자')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='업데이트일자')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_author', to='api.user', verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heart_post', to='api.post', verbose_name='좋아요단 게시글')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_user', to='api.user', verbose_name='좋아요단 사용자')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_followed', to='api.user', verbose_name='팔로우된 사람')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_following', to='api.user', verbose_name='팔로우하는 사람')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='post/', verbose_name='사진or동영상')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_post', to='api.post', verbose_name='연결된 게시글')),
            ],
        ),
    ]
