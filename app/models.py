# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

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
    desc = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


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


class ServicePackage(models.Model):
    """
    # 服务包信息表
    # id        主键

    """

    id = models.AutoField(primary_key=True)


class SpecialHandler(models.Model):
    """
    # 特别动作信息表
    # id        主键

    """

    id = models.AutoField(primary_key=True)


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


class IndexGroup(models.Model):
    """
    # 指标组信息表
    # id        主键

    """

    id = models.AutoField(primary_key=True)
