# -*- coding: utf-8 -*-
### Close.io Email Reports
### _funcs.py - basic functions file

from _settings import *
import sys
import datetime
import time
import requests0 as requests
import json
import urllib, urllib2
from jinja2 import Environment, PackageLoader
import locale
reload(sys)  

sys.setdefaultencoding('utf8')
locale.setlocale( locale.LC_ALL, '' )

# load jinja2 templates
env = Environment(loader=PackageLoader('_funcs', 'templates'))

# Check to see if you changed your API/ORG keys.
def keycheck():
	if closeio_key == 'YOUR_API_KEY':
		sys.exit("Uh oh! You have not set your Close.io API_KEY yet. Do so in _keys.py.")
	if closeio_org == 'YOUR_ORG_ID':
		sys.exit("Uh oh! You have not set your Close.io ORG_ID yet. Do so in _keys.py.")
	if mailgun_key == 'YOUR_MAILGUN_API_KEY':
		sys.exit("Uh oh! You have not set your Mailgun API_KEY yet. Do so in _keys.py.")
	if mailgun_domain == 'YOUR_MAILGUN_DOMAIN':
		sys.exit("Uh oh! You have not set your Mailgun domain yet. Do so in _keys.py.")
	return;

# Build the dates
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
monday = today + datetime.timedelta(days=-today.weekday(), weeks=0)
sunday = today + datetime.timedelta(days=-today.weekday() + 6, weeks=0)

# Check to see if we are in test or live mode.
def check_if_testing():
	if testing_mode == True:
		print "TESTING MODE - Emails will be sent to the admin's email address only."
	if testing_mode == False:
		print "LIVE MODE - Emails will be sent to all of your Close.io organization users."
	return;

def run_report(report_url, report_name):
	data = requests.get(report_url, auth=(closeio_key, ''), headers=headers)
	r = data.json
	report_name.append({"calls": r['calls'], "opportunities_created": r['opportunities_created'], "revenue_created_total": r['revenue_created_monthly']/100.0 + r['revenue_created_one_time']/100.0 + r['revenue_created_annual']/100.0, "revenue_won_total": r['revenue_won_monthly']/100.0 + r['revenue_won_one_time']/100.0 + r['revenue_won_annual']/100.0, "opportunities_won": r['opportunities_won'], "call_duration": r['calls_duration_total']/60})
	return;

def run_leader_report(report_url, report_name, report_user):
	data = requests.get(report_url, auth=(closeio_key, ''), headers=headers)
	r = data.json
	report_name.append((report_user, r["calls"], r['opportunities_created'], r['revenue_won_monthly']/100.0 + r['revenue_won_one_time']/100.0 + r['revenue_won_annual']/100.0))
	return;

def send_email(email, r_day, r_week, report_date, r_type, call_rankings, revenue_rankings, opp_created_rankings):
	report_email = env.get_template('email.html')
	return requests.post("https://api.mailgun.net/v2/%s/messages" % mailgun_domain, auth=("api", mailgun_key),
		data={"from": from_email,
              "to": email,
              "subject": "%s Sales Report For %s" % (org_name, report_date.strftime("%B %d, %Y")),
              "html": report_email.render(call_rankings=call_rankings, revenue_rankings=revenue_rankings,  opp_created_rankings=opp_created_rankings, org_name=org_name, r_type=r_type, report_date=report_date, today_calls=r_day[0]['calls'], today_call_duration=r_day[0]['call_duration'], today_opps=r_day[0]['opportunities_created'], today_opps_value=locale.currency(r_day[0]['revenue_created_total'], grouping=True), today_won=r_day[0]['opportunities_won'], today_won_value=locale.currency(r_day[0]['revenue_won_total'], grouping=True), week_calls=r_week[0]['calls'], week_call_duration=r_week[0]['call_duration'], week_opps=r_week[0]['opportunities_created'], week_opps_value=locale.currency(r_week[0]['revenue_created_total'], grouping=True), week_won=r_week[0]['opportunities_won'], week_won_value=locale.currency(r_week[0]['revenue_won_total'], grouping=True))})
	return;


