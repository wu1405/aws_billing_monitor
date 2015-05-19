## AWS Billing Monitor  ##
**This django project is used for monitoring AWS billing.You can see the daily report or custom range by a calendar.The charges will be shown in the graph.**
![](http://i.imgur.com/CgWN3SZ.jpg)

## Environment:
**linux**

**django 1.6.6**

**jquery-1.8.3.min.js**

**bootstrap and highchars**

**boto (AWS python api environment)**

## Usage:
- First, you should create a clondwatch with a billing alart in AWS. (http://aws.amazon.com/documentation/cloudwatch/). And also install boto on your computer or servers.
- In my example, I have 3 aws accounts. So 3 lines are shown one graph. You can modified by yourself.
- billing_total.py and daily_charge.py are used for inserting and calculating data. You can run it once a day in crontable . You can insert data manually by manual_daily.py and manual_total.py.
- The url is http://yourdomain/billing/reports_billing. "billing" is one of my app.
- In the billing/templates/billing.html. I have involved the bootstrip.
`<link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet">`
 `<link href="http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css" rel="stylesheet">`
`<script type="text/javascript" src="http://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>`
- You need add "static/" to your static document. Calendar and Highcharts in the static/. 


