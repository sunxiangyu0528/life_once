from django.db import models

from utils.base_models import BaseModel


class Projects(BaseModel):
    id = models.AutoField(verbose_name="id主键",primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="项目名称", max_length=200, help_text="项目名称", unique=True)
    leader = models.CharField(verbose_name="负责人", max_length=200, help_text="负责人")
    tester = models.CharField(verbose_name="测试人员", max_length=200, help_text="测试人员")
    publish_app = models.CharField(verbose_name="发布应用", max_length=200, help_text="发布应用")
    programer = models.CharField(verbose_name="开发人员", max_length=200, help_text="开发人员")
    desc = models.TextField(verbose_name="简要描述", help_text="简要描述", blank=True, default='', null=True)

    class Meta(object):
        db_table = 'tb_projects'
        # 在admin站点中，显示一个更人性化的表名
        verbose_name = '项目信息'  # 增加项目的描述
        verbose_name_plural = '项目(admin站点描述)'

    def __str__(self):
        return self.name


# class Interfaces(models.Model):
#     project = models.ForeignKey('Projects', on_delete=models.CASCADE, verbose_name="所属项目", help_text='所属项目')
#