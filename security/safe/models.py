from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

# 保卫处后台数据分类,形式为(数据库存储，后台显示)
# 如果需要增加大的分类，可以在此添加
label_option = (
    ('NO', '通知公告'),
    ('SD', '安全动态'),
    ('DS', '部门设置'),
    ('SK', '安全知识'),
    ('SS', '安全制度'),
    ('CM', '综合治理'),
    ('SG', '服务指南')
    )
child_label_option = (
    ('DI','部门简介'),
    ('PE','工作人员'),
    ('JR','工作职责'),
    ('FS','消防安全'),
    ('SE','治安安全'),
    ('TS','交通安全'),
    ('NR','国家法律法规'),
    ('SR','校园规章制度'),
    ('LF','失物招领'),
    ('IS','资料分享'),
    ('DO','下载专区'),
    )

class Base(models.Model):
    """
    保卫处后台数据库模型，参数解释：
    max_length：最大长度；blank：内容是否为空；
    choices：给定特定值选择；default：给定默认值；
    verbose_name：在后台管理页面显示的表头
    """
    label = models.CharField(max_length = 8, blank = False, choices = label_option, verbose_name = "文章分类")
    child_label = models.CharField(max_length = 20, blank = True, choices = child_label_option, verbose_name = "文章子类")
    title = models.CharField(max_length = 30, blank = False, unique = True, verbose_name = "文章标题")
    author = models.CharField(max_length = 6, blank = False, default = "保卫处", verbose_name = "发布者")
    time = models.DateTimeField(auto_now_add = True, blank = False, verbose_name = "发布时间")
    content = RichTextField(verbose_name = "正文")
    is_photo = models.BooleanField(blank = False, choices = ((True, '有'),(False, '无')), verbose_name = "有无图片")

    # 返回的数据如何显示
    def __str__(self):
        return '{} {} {}'.format(self.title, self.author, self.time)