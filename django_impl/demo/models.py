from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Maps(models.Model):
  """
  Map data for all users, includes upper-left corner and lower-right corner of maps.
  """
  uid = models.ForeignKey(User,on_delete=models.CASCADE)  # a user may have > 1 map
  upper_long = models.DecimalField(max_digits=9, decimal_places=6)  # suggestion from: http://stackoverflow.com/questions/30706799/which-model-field-to-use-in-django-to-store-longitude-and-latitude-values
  upper_lat  = models.DecimalField(max_digits=9, decimal_places=6)
  lower_long = models.DecimalField(max_digits=9, decimal_places=6)
  lower_lat  = models.DecimalField(max_digits=9, decimal_places=6)
  map_name   = models.CharField(max_length=200)  # user may give nickname to the map, default will be "Map Created On <UTC ts>"
  pub_date = models.DateTimeField('date made')

  def __str__(self):
    return "user: {}; upperlat: {}; upperlong: {}; lowerlat: {}; lowerlong: {}".format(self.uid.username, self.upper_lat, self.upper_long,
                                                                                       self.lower_lat, self.lower_long, self.map_name)

class Marks(models.Model):
  mapid = models.ForeignKey(Maps, on_delete=models.CASCADE)  # a map may have > 1 mark
  mark_long =  models.DecimalField(max_digits=9, decimal_places=6)
  mark_lat  =  models.DecimalField(max_digits=9, decimal_places=6)
  name = models.CharField(max_length=200)
  description = models.TextField()
  residents = models.IntegerField(default=-1)

  def __str__(self):
    return "map: {}; lat: {}; long: {};".format(self.mapid, self.mark_lat, self.mark_long)