from django.db import models
from website.models import Agent,User

# Create your models here.

class PlayTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time)

class AgentPackage(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    package_name = models.CharField(max_length=100)
    single_rate = models.FloatField()
    single_dc = models.FloatField()
    double_rate = models.FloatField()
    double_dc = models.FloatField()
    box_rate = models.FloatField()
    box_dc = models.FloatField()
    super_rate = models.FloatField()
    super_dc = models.FloatField()
    first_prize = models.FloatField()
    first_dc = models.FloatField()
    second_prize = models.FloatField()
    second_dc = models.FloatField()
    third_prize = models.FloatField()
    third_dc = models.FloatField()
    fourth_prize = models.FloatField()
    fourth_dc = models.FloatField()
    fifth_prize = models.FloatField()
    fifth_dc = models.FloatField()
    guarantee_prize = models.FloatField()
    guarantee_dc = models.FloatField()
    box_first_prize = models.FloatField()
    box_first_prize_dc = models.FloatField()
    box_series_prize = models.FloatField()
    box_series_dc = models.FloatField()
    single1_prize = models.FloatField()
    single1_dc = models.FloatField()
    double2_prize = models.FloatField()
    double2_dc = models.FloatField()


    def __str__(self):
        return str(self.package_name)
