from django.conf.urls import patterns, include, url

urlpatterns = patterns('billing.views',
    url(r'mobo_billing/$', 'mobo_billing'),
)
