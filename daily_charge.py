#!/usr/bin/env python
import MySQLdb
import logging
import datetime
from datetime import timedelta

def Daily_charge(table):
	#Now=datetime.date.today()
	#Now=datetime.date.today() + timedelta(days=-5)
	Yesterday=datetime.date.today() + timedelta(days=-1)
	OneDayBefore=Yesterday + timedelta(days=-1)
	
	conn = MySQLdb.connect(user='root', db='instance', passwd='', host='localhost')
	cursor = conn.cursor()

	sql1="select total_all from %s where date='%s'" % (table,OneDayBefore)
	cursor.execute(sql1)
	infos1=cursor.fetchall()[0][0]
	# the charges of the day before yesterday 

	sql2="select total_all from %s where date='%s'" % (table,Yesterday)
	cursor.execute(sql2)
	infos2=cursor.fetchall()[0][0]
	# the charges of yesterday



	if str(Yesterday).split('-')[1] == str(OneDayBefore).split('-')[1]:     #in the same month
		print "ok"
	
		Day_charge=infos2-infos1  #  the difference of two numbers            
		sql3="update %s set total_today='%s' where date='%s'" % (table,Day_charge,Yesterday)
		cursor.execute(sql3)	
	

	elif str(Yesterday).split('-')[2] == '01':    # the first day of the month
		print "ok 01"	

		Day_charge=infos2
		sql4="update %s set total_today='%s' where date='%s'" % (table,Day_charge,Yesterday)
		cursor.execute(sql4)	
	
	else : 
		print "not ok"

	conn.commit()
	cursor.close()
	conn.close()

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG,
		format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
		datefmt='%a, %Y-%m-%d %H:%M:%S',
 		filename='/home/instance/Billing/debug_Daily.log',
		filemode='w')
	Daily_charge('billing_info_voga')
	Daily_charge('billing_info_mobo')
	Daily_charge('billing_info_cypay')
