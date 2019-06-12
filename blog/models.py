# coding=utf-8
from django.db import models

from DjangoUeditor.models import UEditorField

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_label = models.CharField(max_length=50)
    Content=UEditorField(u'文章',width=600, height=300, toolbars="full", imagePath="images/", filePath="files/", upload_settings={"imageMaxSize":1204000},
             settings={},command=None,blank=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')
    alter_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'Article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name