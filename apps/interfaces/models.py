from django.db import models

# Create your models here.
# 一个项目中有多个接口，那么需要在“多”的一侧创建外检，项目表为父表
from utils.base_models import BaseModel


class Interface(BaseModel):
    id = models.AutoField(verbose_name="id主键", primary_key=True, help_text="id主键")
    name = models.CharField(verbose_name="接口名称", max_length=200, help_text="接口名称")
    tester = models.CharField(verbose_name="测试人员", max_length=200, help_text="测试人员")
    desc = models.TextField(verbose_name="简要描述", help_text="简要描述", blank=True, default='', null=True)
    project = models.ForeignKey('projects.Projects', related_name='interface_set', on_delete=models.CASCADE,
                                verbose_name="所属项目",
                                help_text='所属项目')

    class Meta:
        db_table = 'tb_interfaces'
        verbose_name = "接口信息"
        verbose_name_plural = '接口(admin站点描述)'

    def __str__(self):
        return self.name
