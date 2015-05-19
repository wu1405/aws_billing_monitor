#!/usr/bin/env python
import boto.ec2.cloudwatch
from boto.ec2.connection import EC2Connection
import os,sys
import logging
import boto.ec2
from boto.ec2 import get_region
import datetime
from datetime import timedelta
import MySQLdb

def Bill(account,id,range):
	billingkey = os.environ.get('%sBill_Key' % account)
	billingsecret = os.environ.get('%sBill_Secret' % account) 
	myRegion = get_region('us-east-1')
	conn = boto.ec2.cloudwatch.connect_to_region('us-east-1',aws_access_key_id=billingkey,aws_secret_access_key=billingsecret)

	Metrics=conn.list_metrics(metric_name=u'EstimatedCharges',namespace=u'AWS/Billing')
	Last = datetime.date.today()+timedelta(days=-range) 
	during = timedelta(days=-1)
	Start = Last + during

	file="%s_total.out" % account
	f=open(file,'w')
	for metric in Metrics:
		if  [id]  in metric.dimensions.values() and u'ServiceName' not in metric.dimensions : 
		#print Start,metric.query(Start,Last,'Average',period=86400)
			f.write(str(Start)+'\t'+str(metric.query(Start,Last,'Average',period=86400))+'\n')
	f.close()
	

	cost_cmd="echo `cat %s |awk -F':' '{print $3}'|awk -F'.' '{print $1}'`" % file
	date_cmd="echo `awk '{print $1}' %s`" % file
	cost=int(os.popen(cost_cmd).read().strip('\n'))
	date=str(os.popen(date_cmd).read().strip('\n'))
	conn = MySQLdb.connect(user='root', db='instance', passwd='', host='localhost')
	cursor = conn.cursor()
	sql="insert into billing_info_%s(date,total_all) values('%s',%s)" % (account,date,cost)
	cursor.execute(sql)
	conn.commit()
	cursor.close()
	conn.close()



if __name__ == '__main__':
        logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %Y-%m-%d %H:%M:%S',
                filename='debug_billing.log',
                filemode='w')
	range=int(sys.argv[1])
	Bill('account_name','aws_account_id',range)

