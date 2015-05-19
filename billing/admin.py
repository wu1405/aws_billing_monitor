from django.contrib import admin
from billing.models import Info_account1,Info_account2,Info_account3
# Register your models here.
class Info_account1_Admin(admin.ModelAdmin):
	list_display = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')
	search_fields = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')

class Info_account2_Admin(admin.ModelAdmin):
	list_display = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')
	search_fields = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')

class Info_account3_Admin(admin.ModelAdmin):
	list_display = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')
	search_fields = ('date','total_today','total_all','ec2','s3','datatransfer','route53','emr','cloudfront')

admin.site.register(Info_account1,Info_account1_Admin)
admin.site.register(Info_account2,Info_account2_Admin)
admin.site.register(Info_account3,Info_account3_Admin)
