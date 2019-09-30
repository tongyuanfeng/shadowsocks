# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class access_vpn_ip_list(models.Model):
    """
    vpn白名单
        """
    ip = models.CharField( max_length=64, null=True)
    status = models.IntegerField(default=0) # 1 allow 2 deny


