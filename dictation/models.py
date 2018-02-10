# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import os

# Create your models here.
class pronance_webster_mp3(models.Model):
    word_name = models.CharField(max_length=255)
    word_path = models.CharField(max_length=255)