from django.db import models

# Create your models here.
class Info_mobo(models.Model):
	date = models.DateField()
	total_today = models.IntegerField(max_length=10)
	total_all = models.IntegerField(max_length=10)
	ec2 = models.IntegerField(max_length=10)
	s3 = models.IntegerField(max_length=10)
	datatransfer = models.IntegerField(max_length=10)
	route53 = models.IntegerField(max_length=10)
	emr = models.IntegerField(max_length=10)
	cloudfront = models.IntegerField(max_length=10)
#	def __unicode__(self):
#		return self.total
	
class Info_voga(models.Model):
	date = models.DateField()
	total_today = models.IntegerField(max_length=10)
	total_all = models.IntegerField(max_length=10)
	ec2 = models.IntegerField(max_length=10)
	s3 = models.IntegerField(max_length=10)
	datatransfer = models.IntegerField(max_length=10)
	route53 = models.IntegerField(max_length=10)
	emr = models.IntegerField(max_length=10)
	cloudfront = models.IntegerField(max_length=10)

class Info_cypay(models.Model):
	date = models.DateField()
	total_today = models.IntegerField(max_length=10)
	total_all = models.IntegerField(max_length=10)
	ec2 = models.IntegerField(max_length=10)
	s3 = models.IntegerField(max_length=10)
	datatransfer = models.IntegerField(max_length=10)
	route53 = models.IntegerField(max_length=10)
	emr = models.IntegerField(max_length=10)
	cloudfront = models.IntegerField(max_length=10)
