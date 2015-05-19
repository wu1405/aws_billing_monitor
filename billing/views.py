from django.shortcuts import render_to_response,render
from django.template.context import RequestContext
from billing.models import Info_account1,Info_account2,Info_account3
# Create your views here.

def reports_billing(request):
	result=request.POST.get('reservation','')
	if not result:
		start=str(Info_account1.objects.order_by("date")[0].date)
		end=str(Info_account1.objects.order_by("-date")[0].date)

		#objs=Info_account1.objects.all()
		objs_account1=Info_account1.objects.order_by("date")
		date_result=[]	
		total_all_account1=[]
		total_today_account1=[]
	
		for obj in objs_account1:
			date_result.append(str(obj.date))
			total_all_account1.append(int(obj.total_all))
			total_today_account1.append(int(obj.total_today))


		objs_account2=Info_account2.objects.order_by("date")
		total_all_account2=[]
		total_today_account2=[]
		for obj in objs_account2 :
			total_all_account2.append(int(obj.total_all))
			total_today_account2.append(int(obj.total_today))

		objs_account3=Info_account3.objects.order_by("date")
		total_all_account3=[]
		total_today_account3=[]
		for obj in objs_account3 :
			total_all_account3.append(int(obj.total_all))
			total_today_account3.append(int(obj.total_today))

		return render_to_response('billing.html', RequestContext(request,locals()))

	else:
		start=result.split(" - ")[0]
		end=result.split(" - ")[1]

		date_result=[]
		total_all_account1=[]
		total_today_account1=[]
		total_all_account2=[]
		total_today_account2=[]
		total_all_account3=[]
		total_today_account3=[]

		objs_account1=Info_account1.objects.order_by("date").filter(date__range=(start,end))
		objs_account2=Info_account2.objects.order_by("date").filter(date__range=(start,end))
		objs_account3=Info_account3.objects.order_by("date").filter(date__range=(start,end))
		for obj in objs_account1:
			date_result.append(str(obj.date))
			total_all_account1.append(int(obj.total_all))
			total_today_account1.append(int(obj.total_today))
		for obj in objs_account2:
			total_all_account2.append(int(obj.total_all))
			total_today_account2.append(int(obj.total_today))
		for obj in objs_account3:
			total_all_account3.append(int(obj.total_all))
			total_today_account3.append(int(obj.total_today))

	
		return render_to_response('billing.html', RequestContext(request,locals()))




