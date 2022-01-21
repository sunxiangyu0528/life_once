from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Projects


#   定义自定义校验器
# def is_unique_project_name(name):
# if '项目' not in name:
#     raise serializers.ValidationError(detail='这个是错误提示')


class ProjectSerializer(serializers.Serializer):
    # read_only只进行序列化输出
    # write_only 只反序列化输入,不能序列化输出
    # validators 校验器
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label="项目名称", max_length=200, help_text="项目名称222",
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message='这是校验失败的错误信息'),
                                             # is_unique_project_name
                                             ])
    leader = serializers.CharField(label="负责人", max_length=200, help_text="负责人")

    # tester = serializers.CharField(label="测试人员", max_length=200, help_text="测试人员")
    # publish_app = serializers.CharField(label="发布应用", max_length=200, help_text="发布应用")
    # programer = serializers.CharField(label="开发人员", max_length=200, help_text="开发人员")
    # desc = serializers.CharField(label="简要描述", help_text="简要描述", allow_null=True,allow_blank=True)
    # 字段定义时的限制（包括validators列表数码条从左向右开始校验）
    # 单字段校验
    # def validate_name(self, value):
    #     if '项目' not in value:
    #         raise serializers.ValidationError(detail='这个是错误提示')
    #     return value
    #
    # # 多字段校验
    # def validate(self, attrs):
    #     if 'icon' not in attrs['name'] and '项目' not in attrs['leader']:
    #         raise serializers.ValidationError(detail='多字段校验的错误提示')
    #     return attrs

    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Projects.objects.create(**validated_data)

# class ProjectModelSerializer(serializers.ModelSerializer):
#     class Meta():
#         # 指定参考哪一个模型类创建
#         model = Projects
#         # 指定为模型类的那些字段，来生成序列化器
#         fields = "__all__"
#         # fields = ('id', 'tester')
#         # exclude = ('id')
#         # read_only_fields = ('id')
#         # extra_kwargs = {
#         #     'leader': {'write_only': True}
#         # }
#
#     def create(self, validated_data):
#         return Projects.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         return instance
