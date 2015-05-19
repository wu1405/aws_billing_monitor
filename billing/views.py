from django.shortcuts import render_to_response,render
from django.template.context import RequestContext
from billing.models import Info_mobo,Info_voga,Info_cypay
# Create your views here.

def mobo_billing(request):
	result=request.POST.get('reservation','')
	if not result:
		start=str(Info_mobo.objects.order_by("date")[0].date)
		end=str(Info_mobo.objects.order_by("-date")[0].date)

		#objs=Info_mobo.objects.all()
		objs_mobo=Info_mobo.objects.order_by("date")
		date_result=[]	
		total_all_mobo=[]
		total_today_mobo=[]
	
		for obj in objs_mobo:
			date_result.append(str(obj.date))
			total_all_mobo.append(int(obj.total_all))
			total_today_mobo.append(int(obj.total_today))

#		Draw_defult('voga')

		objs_voga=Info_voga.objects.order_by("date")
		total_all_voga=[]
		total_today_voga=[]
		for obj in objs_voga :
			total_all_voga.append(int(obj.total_all))
			total_today_voga.append(int(obj.total_today))

		objs_cypay=Info_cypay.objects.order_by("date")
		total_all_cypay=[]
		total_today_cypay=[]
		for obj in objs_cypay :
			total_all_cypay.append(int(obj.total_all))
			total_today_cypay.append(int(obj.total_today))

		return render_to_response('billing.html', RequestContext(request,locals()))

	else:
		start=result.split(" - ")[0]
		end=result.split(" - ")[1]

		date_result=[]
		total_all_mobo=[]
		total_today_mobo=[]
		total_all_voga=[]
		total_today_voga=[]
		total_all_cypay=[]
		total_today_cypay=[]

		objs_mobo=Info_mobo.objects.order_by("date").filter(date__range=(start,end))
		objs_voga=Info_voga.objects.order_by("date").filter(date__range=(start,end))
		objs_cypay=Info_cypay.objects.order_by("date").filter(date__range=(start,end))
		for obj in objs_mobo:
			date_result.append(str(obj.date))
			total_all_mobo.append(int(obj.total_all))
			total_today_mobo.append(int(obj.total_today))
		for obj in objs_voga:
			total_all_voga.append(int(obj.total_all))
			total_today_voga.append(int(obj.total_today))
		for obj in objs_cypay:
			total_all_cypay.append(int(obj.total_all))
			total_today_cypay.append(int(obj.total_today))

	
		return render_to_response('billing.html', RequestContext(request,locals()))


def Draw_defult(account):
	objs_voga=Info_voga.objects.order_by("date")
	total_all_voga=[] 	
	total_today_voga=[] 
	for obj in objs_voga :
		total_all_voga.append(int(obj.total_all)) 
		total_today_voga.append(int(obj.total_today)) 


