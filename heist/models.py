from django.db import models
from django.db.models import Sum, Avg, Count, Min, Max
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime, timedelta

class User(AbstractUser):
    pass