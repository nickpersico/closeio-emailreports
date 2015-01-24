# -*- coding: utf-8 -*-
### Close.io Email Reports
### email_reports.py - the main script file.

# Libraries
from _funcs import *
from _settings import *
from _keys import *
import requests0 as requests
import json
import urllib, urllib2
import datetime
from operator import itemgetter, attrgetter, methodcaller

# Check to make sure API keys have been changed in the _keys.py file.
keycheck();

# Let us know if you are in testing or live mode.
check_if_testing();

# Build a list of the org's active users.
users = []
org = requests.get(url_org, auth=(closeio_key, ''), headers={'Content-Type': 'application/json'})
memberships = org.json['memberships']

for m in memberships:
	if m['user_email'] in ignore_email_report_emails:
		continue
	else:
		users.append({"id": m['user_id'], "first_name": m['user_first_name'], "full_name": m['user_full_name'], "email": m['user_email']})

# Build the team's stats report for today.
today_team_report_url = url_user_day_report + "date_start=%s&date_end=%s" % (today, tomorrow)
today_team_report = []
run_report(report_url=today_team_report_url, report_name=today_team_report);

# Build the team's stats report for this week.
week_team_report_url = url_user_day_report + "date_start=%s&date_end=%s" % (monday, sunday)
week_team_report = []
run_report(report_url=week_team_report_url, report_name=week_team_report);

# Build the team's leaderboard report for this week.
week_leader_report = []
for u in users:
	week_leader_report_url = url_user_day_report + "date_start=%s&date_end=%s&user_id=%s" % (monday, sunday, u["id"])
	run_leader_report(report_url=week_leader_report_url, report_name=week_leader_report, report_user=u['first_name']);

# Take the leaderboard data and create a ranking
call_rankings = sorted(week_leader_report, key=itemgetter(1), reverse=True)
opp_created_rankings = sorted(week_leader_report, key=itemgetter(2), reverse=True)
revenue_rankings = sorted(week_leader_report, key=itemgetter(3), reverse=True)

# Build the individual report
for u in users:
	# Today's individual report
	today_individual_report_url = url_user_day_report + "date_start=%s&date_end=%s&user_id=%s" % (today, tomorrow, u["id"])
	today_individual_report = []
	run_report(report_url=today_individual_report_url, report_name=today_individual_report);

	# This week's individual report
	week_individual_report_url = url_user_day_report + "date_start=%s&date_end=%s&user_id=%s" % (monday, sunday, u["id"])
	week_individual_report = []
	run_report(report_url=week_individual_report_url, report_name=week_individual_report);

	# Send individual email
	if testing_mode == False:
		send_email(u['email'], today_individual_report, week_individual_report, today, r_type=u['full_name'], call_rankings=call_rankings, revenue_rankings=revenue_rankings, opp_created_rankings=opp_created_rankings);
		print "Sent report email to %s." % u['email']
	
	if testing_mode == True:
		send_email(admin_email, today_individual_report, week_individual_report, today, r_type=u['full_name'], call_rankings=call_rankings, revenue_rankings=revenue_rankings, opp_created_rankings=opp_created_rankings);
		print "Sent report email to %s." % admin_email

# Send the team report to the admin
if team_report_setting == True:
	send_email(admin_email, today_team_report, week_team_report, today, r_type="Entire Team", call_rankings=call_rankings, revenue_rankings=revenue_rankings, opp_created_rankings=opp_created_rankings);
	print "Sent the team report email to %s." % admin_email

