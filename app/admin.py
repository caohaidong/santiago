# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Sector,Version,DRGs,Diagnosis,\
    Operation,Treatment,Medicines,Material,ServicePackage,\
    Index,IndexGroup,SpecialHandler

# Register your models here.

admin.site.register(Sector)
admin.site.register(Version)
admin.site.register(DRGs)
admin.site.register(Diagnosis)
admin.site.register(Operation)
admin.site.register(Treatment)
admin.site.register(Medicines)
admin.site.register(Material)
admin.site.register(ServicePackage)
admin.site.register(Index)
admin.site.register(IndexGroup)
admin.site.register(SpecialHandler)