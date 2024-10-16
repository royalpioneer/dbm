# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-DB管理系统(BlueKing-BK-DBM) available.
Copyright (C) 2017-2023 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class GetHostInAuthorizeSerializer(serializers.Serializer):
    ticket_id = serializers.IntegerField(help_text=_("单据id"))
    keyword = serializers.CharField(help_text=_("过滤搜索关键字"), required=False)

    class Meta:
        swagger_schema_fields = {"example": {"ticket_id": 1}}


class IntegrationGrantSerializer(serializers.Serializer):
    client_hosts = serializers.CharField(help_text=_("客户端主机"))
    client_version = serializers.CharField(help_text=_("客户端版本"), required=False, default="5")
    db_hosts = serializers.CharField(help_text=_("DB主机（domain#port）"))
    db_name = serializers.CharField(help_text=_("数据库名"))
    user_name = serializers.CharField(help_text=_("用户名"))
    password = serializers.CharField(help_text=_("密码"))
    privileges = serializers.CharField(help_text=_("权限列表，多个权限以逗号分隔"))

    class Meta:
        swagger_schema_fields = {
            "example": {
                "client_hosts": "%",
                "db_hosts": "test.db#10001",
                "db_name": "test_db_name",
                "user_name": "test_username",
                "password": "test_password",
                "privileges": "SELECT,INSERT,UPDATE,DELETE,EXECUTE,CREATE,ALTER,DROP",
            }
        }
