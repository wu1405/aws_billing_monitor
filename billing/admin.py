from django.contrib import admin
from billing.models import Info_mobo,Info_voga,Info_cypay
# Register your models here.
class Info_mobo_Admin(admin.ModelAdmin):
	list_display = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')
	search_fields = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')

class Info_voga_Admin(admin.ModelAdmin):
	list_display = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')
	search_fields = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')

class Info_cypay_Admin(admin.ModelAdmin):
	list_display = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')
	search_fields = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')

admin.site.register(Info_mobo,Info_mobo_Admin)
admin.site.register(Info_voga,Info_voga_Admin)
admin.site.register(Info_cypay,Info_cypay_Admin)
