# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

admin.register(models.Version)
admin.register(models.DRGs)
admin.register(models.Diagnosis)
admin.register(models.Operation)
admin.register(models.Sector)
