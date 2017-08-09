# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Sector(models.Model):
    """
    # 科室信息表
    # id        主键
    # code      科室编码
    # name      科室名称
    # desc      描述
    # created   创建日期
    # updated   更新日期
    """

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sector'
        verbose_name = '12. 科室信息'
        verbose_name_plural = '12. 科室信息'

    def __str__(self):  # 在python2版本中使用的是__unique__
        return self.name


class Version(models.Model):
    """
    # 病组版本表
    # id            主键
    # version       版本号
    # type          类型
    # area          适用区域
    # status        状态
    # desc          描述
    # created       创建日期
    # updated       更新日期
    """

    # 状态代码项，valid - 有效，invalid - 无效
    STATUS_CHOICE = (
        ('valid', 'Valid'),
        ('invalid', 'Invalid'),
    )

    # 类型代码项，standard - 标准版，local - 地方版
    TYPE_CHOICE = (
        ('standard', 'Standard'),
        ('local', 'Local'),
    )

    id = models.AutoField(primary_key=True)
    version = models.CharField(max_length=10)
    type = models.CharField(max_length=10, choices=TYPE_CHOICE, default='standard')
    area = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='valid')
    desc = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'version'
        verbose_name = '01. 病组版本信息'
        verbose_name_plural = '01. 病组版本信息'


class DRGs(models.Model):
    """
    # 病种分组表，一个分组包括多个诊断
    # id         主键
    # code       病种分组编码
    # name       病种分组名称
    # score      分值
    # sector     科室
    # version    病种分组的版本
    # tag        标签
    # desc       描述信息
    # created    创建日期
    # updated    更新日期
    """

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    score = models.CharField(max_length=5)
    sector = models.ForeignKey(Sector)
    version = models.ForeignKey(Version)
    tag = models.CharField(max_length=100, blank=True)
    desc = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'diagnosis_related_groups'
        verbose_name = '02. 病种分组信息'
        verbose_name_plural = '02. 病种分组信息'


class Diagnosis(models.Model):
    """
    # 诊断信息表，与病种分组是多对一关系
    # id        主键
    # drgs      病种分组
    # code      诊断编码(icd-10)
    # name      诊断名称(icd-10)
    # tag       标签
    # desc      描述
    # created   创建日期
    # updated   更新日期
    """

    id = models.AutoField(primary_key=True)
    drgs = models.ForeignKey(DRGs, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=100, blank=True)
    desc = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'diagnosis'
        verbose_name = '03. 诊断信息'
        verbose_name_plural = '03. 诊断信息'


class Operation(models.Model):
    """
    # 手术信息表
    # id        主键
    # code      手术编码(icd-9)
    # name      手术名称(icd-9)
    # tag       标签
    # desc      描述
    # created   创建日期
    # updated   更新日期
    """

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=100, blank=True)
    desc = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'operation'
        verbose_name = '04. 手术信息'
        verbose_name_plural = '04. 手术信息'


class Treatment(models.Model):
    """
    # 诊疗信息表
    # id        主键
    #
    # tag       标签
    # desc      描述
    # created   创建日期
    # updated   更新日期
    """

    id = models.AutoField(primary_key=True)
    # TODO
    tag = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'treatment'
        verbose_name = '09. 诊疗信息'
        verbose_name_plural = '09. 诊疗信息'


class Medicines(models.Model):
    """
    # 药品信息表
    # id        主键
    #
    # tag       标签
    # desc      描述
    # created   创建日期
    # updated   更新日期
    """

    id = models.AutoField(primary_key=True)
    # TODO
    tag = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'medicines'
        verbose_name = '10. 药品信息'
        verbose_name_plural = '10. 药品信息'


class Material(models.Model):
    """
    # 耗材信息表
    # id        主键
    #
    # tag       标签
    # desc      描述
    # created   创建日期
    # updated   更新日期
    """

    id = models.AutoField(primary_key=True)
    # TODO
    tag = models.CharField(max_length=100)
    desc = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'material'
        verbose_name = '11. 耗材信息'
        verbose_name_plural = '11. 耗材信息'


class ServicePackage(models.Model):
    """
    # 服务包信息表
    # id        主键

    """

    id = models.AutoField(primary_key=True)

    # TODO

    class Meta:
        db_table = 'service_package'
        verbose_name = '05. 服务包信息'
        verbose_name_plural = '05. 服务包信息'


class SpecialHandler(models.Model):
    """
    # 特别动作信息表
    # id        主键

    """

    id = models.AutoField(primary_key=True)

    # TODO

    class Meta:
        db_table = 'specialhandler'
        verbose_name = '06. 特殊场景信息'
        verbose_name_plural = '06. 特殊场景信息'


class Index(models.Model):
    """
    # 指标信息表
    # id            主键
    # code          指标编码
    # name          指标名称
    # type          指标类型
    # formula       计算公式
    # threshold     阈值
    # expression    表达式
    # status        状态
    # tag           标签
    # desc          描述
    # created       创建日期
    # updated       更新日期
    #
    """

    # 指标类型代码项, common-通用, special-专用
    INDEX_TYPE = (
        ('common', 'Common'),
        ('special', 'Special'),
    )

    # 状态代码项，valid - 有效，invalid - 无效
    STATUS_CHOICE = (
        ('valid', 'Valid'),
        ('invalid', 'Invalid'),
    )

    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=INDEX_TYPE, default='common')
    formula = models.TextField(max_length=400)
    threshold = models.CharField(max_length=10)
    expression = models.CharField(max_length=120)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='valid')
    tag = models.CharField(max_length=100, blank=True)
    desc = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'index'
        verbose_name = '07. 指标信息'
        verbose_name_plural = '07. 指标信息'


class IndexGroup(models.Model):
    """
    # 指标组信息表
    # id        主键

    """

    id = models.AutoField(primary_key=True)

    # TODO

    class Meta:
        db_table = 'index_group'
        verbose_name = '08. 指标组信息'
        verbose_name_plural = '08. 指标组信息'
