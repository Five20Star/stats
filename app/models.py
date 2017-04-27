# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BlogPost(models.Model):
        kid = models.AutoField(primary_key=True)
        name = models.TextField()
        sex  = models.TextField()
        desci = models.TextField()
        class Meta:
            db_table='BlogPost'
