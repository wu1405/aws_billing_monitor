from django.conf.urls import patterns, include, url

urlpatterns = patterns('billing.views',
    url(r'reports_billing/$', 'reports_billing'),
)
