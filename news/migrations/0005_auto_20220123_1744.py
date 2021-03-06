# Generated by Django 3.2.11 on 2022-01-23 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_user_id_author_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='user',
            new_name='authorUser',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='commentPost',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='commentUser',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_datetime',
            new_name='dateCreation',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='some_datetime',
            new_name='dateCreation',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='categorys',
            new_name='postCategorys',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='categorys',
            new_name='categoryThrough',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='post',
            new_name='postThrough',
        ),
        migrations.RemoveField(
            model_name='author',
            name='author_rating',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_rating',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_rating',
        ),
        migrations.AddField(
            model_name='author',
            name='authorRating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentRating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='postRating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='article_news',
            field=models.CharField(choices=[('NW', '??????????????'), ('AR', '????????????')], default='news', max_length=8),
        ),
    ]
