from django.db import models
from website.models import Agent

# Create your models here.

class PlayTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time)

class AgentPackage(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,null=True)
    package_name = models.CharField(max_length=100)
    single_rate = models.IntegerField()
    single_dc = models.IntegerField()
    double_rate = models.IntegerField()
    double_dc = models.IntegerField()
    box_rate = models.IntegerField()
    box_dc = models.IntegerField()
    super_rate = models.IntegerField()
    super_dc = models.IntegerField()
    first_rate = models.IntegerField()
    second_rate = models.IntegerField()
    third_rate = models.IntegerField()
    fourth_rate = models.IntegerField()
    fifth_rate = models.IntegerField()
    guarantee_rate = models.IntegerField()
    box_first_prize_rate = models.IntegerField()
    box_series_rate = models.IntegerField()
    _ratesingle1 = models.IntegerField()
    double2_rate = models.IntegerField()
    first_dc = models.IntegerField()
    second_dc = models.IntegerField()
    third_dc = models.IntegerField()
    fourth_dc = models.IntegerField()
    fifth_dc = models.IntegerField()
    guarantee_dc = models.IntegerField()
    box_first_prize_dc = models.IntegerField()
    box_series_dc = models.IntegerField()
    single1_dc = models.IntegerField()
    double2_dc = models.IntegerField()

    def __str__(self):
        return str(self.package_name)
