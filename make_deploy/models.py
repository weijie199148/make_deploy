# -*- coding: utf-8 -*-
from django.db import models

class t_system_info(models.Model):
    class Meta:  # 显示表名为中文
        verbose_name = '系统信息'
        verbose_name_plural = '系统信息'
    id = models.AutoField(primary_key=True,verbose_name="id")
    product_path = models.CharField(max_length=50,verbose_name="版本库目录",unique=True)
    config_path = models.CharField(max_length=50,verbose_name="配置库目录",unique=True)
    create_time = models.DateTimeField(auto_now_add = True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")

    def __unicode__(self):
        return self.product_path

class t_app_info(models.Model):
    class Meta:  # 显示表名为中文
        verbose_name = '应用信息'
        verbose_name_plural = '应用信息'
    id = models.AutoField(primary_key=True,verbose_name="id")
    app_name = models.CharField(max_length=20,verbose_name="软件包名称",unique=True)
    project_id = models.IntegerField(verbose_name="项目名称ID")
    host_id = models.IntegerField(verbose_name="主机ID")
    app_type = models.IntegerField(verbose_name="应用包标识")
    deploy_path = models.CharField(max_length=100,verbose_name="部署目录")
    config_path = models.CharField(max_length=100,verbose_name="配置文件目录")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    def __unicode__(self):
        return self.app_name

class t_project_info(models.Model):
    class Meta:  # 显示表名为中文
        verbose_name = '项目信息'
        verbose_name_plural = '项目信息'
    id = models.AutoField(primary_key=True,verbose_name="id")
    project_name = models.CharField(max_length=20,verbose_name="项目名称",unique=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    def __unicode__(self):
        return self.project_name

class t_host_info(models.Model):
    class Meta:  # 显示表名为中文
        verbose_name = '主机信息'
        verbose_name_plural = '主机信息'
    id = models.AutoField(primary_key=True,verbose_name="id")
    ipadd = models.IPAddressField(verbose_name="服务器ＩＰ地址",unique=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    def __unicode__(self):
        return self.ipadd

class t_version_info(models.Model):
    class Meta:  # 显示表名为中文
        verbose_name = '版本信息'
        verbose_name_plural = '版本信息'

    id = models.AutoField(primary_key=True, verbose_name="id")
    version_id = models.IntegerField(verbose_name="版本号",unique=True)
    version_tag = models.CharField(max_length=50, verbose_name="版本标识符",unique=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    def __unicode__(self):
        return self.version_tag

class t_logs(models.Model):
    class Meta:  # 显示表名为中文
        verbose_name = '日志信息'
        verbose_name_plural = '日志信息'

    id = models.AutoField(primary_key=True,verbose_name="id")
    svn_path = models.CharField(max_length=100,verbose_name="svn_targs地址")
    version_id = models.CharField(max_length=20,verbose_name="版本号")
    status = models.IntegerField(max_length=2,verbose_name="执行状态标识")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后修改时间")
    def __unicode__(self):
        return self.svn_path
