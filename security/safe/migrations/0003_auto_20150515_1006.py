# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safe', '0002_auto_20150512_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='child_label',
            field=models.CharField(verbose_name='文章子类', blank=True, choices=[('DI', '部门简介'), ('PE', '工作人员'), ('JR', '工作职责'), ('FS', '消防安全'), ('SE', '治安安全'), ('TS', '交通安全'), ('NR', '国家法律法规'), ('SR', '校园规章制度'), ('LF', '失物招领'), ('IS', '资料分享'), ('DO', '下载专区')], max_length=20),
        ),
    ]
