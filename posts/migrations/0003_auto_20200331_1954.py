# Generated by Django 3.0.3 on 2020-03-31 19:54

from django.db import migrations

from boards.factories import BoardFactory
from bulletin_board.users.test.factories import UserProfileFactory
from posts.factories import PostFactory
from threads.factories import ThreadFactory


def insert_board_data(apps, _):
    user_profile = UserProfileFactory()
    boards = BoardFactory.create_batch(5)
    for board in boards:
        thread = ThreadFactory(board=board)
        PostFactory.create_batch(5, thread=thread, publisher_id=user_profile.id)


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200331_1943'),
    ]

    operations = [
        migrations.RunPython(
            insert_board_data,
            migrations.RunPython.noop
        )
    ]
