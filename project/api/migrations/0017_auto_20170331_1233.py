# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import models.civi
import models.thread
import models.account


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_remove_civiimage_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='image',
            field=models.ImageField(null=True, upload_to=models.thread.PathAndRename(b''), blank=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=models.account.PathAndRename(b''), blank=True),
        ),
        migrations.AlterField(
            model_name='civiimage',
            name='image',
            field=models.ImageField(null=True, upload_to=models.civi.PathAndRename(b''), blank=True),
        ),
    ]
