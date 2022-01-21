from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(label='明确密码',
                                             write_only=True,
                                             min_length=6,
                                             max_length=20,
                                             help_text='确认密码',
                                             error_messages={
                                                 'min_length': '仅允许6-20个字符串',
                                                 'max_length': '仅允许6-20个字符串'
                                             })
    token = serializers.CharField(label='生成字段', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'password_confirm', 'token')
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 6,
                'max_length': 20,
            }, 'password': {
                'label': '密码',
                'help_text': '密码',
                'min_length': 6,
                'max_length': 20,
            }, 'password_confirm': {
                'label': '密码',
                'help_text': '密码',
                'min_length': 6,
                'max_length': 20,
            }, 'token': {
                'read_only': True
            }, 'email': {
                'write_only': True}

        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError('两次输入的代码不一致')
        return attrs

    def create(self, validated_data):
        del validated_data['password_confirm']
        user = User.objects.create_user(**validated_data)
        # # 创建手动创建token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user
