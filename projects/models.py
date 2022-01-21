from django.db import models


# Create your models here.

# class Person(models.Model):
#     # id = models.AutoField(primary_key=True)

class Projects(models.Model):
    name = models.CharField(verbose_name="项目名称", max_length=200, help_text="项目名称", unique=True)
    leader = models.CharField(verbose_name="负责人", max_length=200, help_text="负责人")
    tester = models.CharField(verbose_name="测试人员", max_length=200, help_text="测试人员")
    publish_app = models.CharField(verbose_name="发布应用", max_length=200, help_text="发布应用")
    programer = models.CharField(verbose_name="开发人员", max_length=200, help_text="开发人员")
    desc = models.TextField(verbose_name="简要描述", help_text="简要描述", blank=True, default='', null=True)

    class Meta(object):
        db_table = 'tb_projects'
        # 在admin站点中，显示一个更人性化的表名
        verbose_name = '项目'
        verbose_name_plural = '项目'
