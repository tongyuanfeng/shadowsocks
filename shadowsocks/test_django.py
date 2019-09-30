#-*-coding:utf-8-*-
import os
import sys
import  logging
reload(sys)
sys.setdefaultencoding('utf-8')



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecs.settings_dev")

import datetime
import django
django.setup()

from gateapp.models import *


from django.forms.models import model_to_dict
from django.core import serializers

import pandas as pd
import numpy as np
import numpy as np
from django.db.models import Q


