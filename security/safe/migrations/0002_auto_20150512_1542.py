# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('safe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('label', models.CharField(max_length=8, verbose_name='文章分类', choices=[('NO', '通知公告'), ('SD', '安全动态'), ('DS', '部门设置'), ('SK', '安全知识'), ('SS', '安全制度'), ('CM', '综合治理'), ('SG', '服务指南')])),
                ('child_label', models.CharField(verbose_name='文章子类', max_length=10, blank=True)),
                ('title', models.CharField(unique=True, max_length=30, verbose_name='文章标题')),
                ('author', models.CharField(default='保卫处', max_length=6, verbose_name='发布者')),
                ('time', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name='正文')),
                ('is_photo', models.BooleanField(verbose_name='有无图片', choices=[(True, '有'), (False, '无')])),
            ],
        ),
        migrations.DeleteModel(
            name='ExampleModel',
        ),
    ]
