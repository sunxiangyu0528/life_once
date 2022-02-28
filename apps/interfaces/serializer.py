from rest_framework import serializers

from apps.interfaces.models import Interface
from apps.projects.models import Projects


class InterfaceModelSerializer(serializers.ModelSerializer):
    # 返回关联属性的类的__str__方法的值。
    # project = serializers.StringRelatedField(help_text='项目名称', read_only=True)
    # 返回关联属性的主键，因为有多个，所以必须加上many=True
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), help_text='项目名称')
    # SlugRelatedField,此字段被序列化为关联对象的指定字段数据publish_app
    project = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta():
        # 指定参考哪一个模型类创建
        model = Interface
        # 指定为模型类的那些字段，来生成序列化器
        fields = "__all__"
        # fields = ('id', 'name', 'project', 'project_id')
