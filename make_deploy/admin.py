# -*- coding:utf-8 -*-
from django.contrib import admin
from make_deploy.models import *


admin.site.register(t_system_info )
admin.site.register(t_app_info )
admin.site.register(t_project_info )
admin.site.register(t_host_info )
admin.site.register(t_version_info )
admin.site.register(t_logs )
