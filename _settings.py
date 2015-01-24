### Close.io Email Reports
### settings.py - various options for sending the email reports.
from _keys import *
from _funcs import *
import sys
import datetime
import requests0 as requests

# 1. Do you want to send a total team report to the admin?
team_report_setting = True

# 2. From email address. Set who you'd like these report emails to come from.
from_email = "Close.io <reports@smarthost.me>"

# 3. Add additional email addresses to receive the total team report. Uncomment the line below to use.
additional_team_report_emails = ['gob@bluthcompany.com', 'michael@bluthcompany.com']

# 4. Do not send emails to the below email addresses. Uncomment the line below to use.
ignore_email_report_emails = ['gob@bluthcompany.com', 'michael@bluthcompany.com']

# 5. Testing mode. When set to True, the reports will only be emailed to admin email. Set to true by default.
testing_mode = True

# 6. Admin email - the email address where to send admin/testing emails
admin_email = 'gob@bluthcompany.com'

####### Close.io URL particulars - no touching.

### Close.io API URLs - no touching.
headers = {'Content-Type': 'application/json'}
url_org = "https://app.close.io/api/v1/organization/%s/" % closeio_org
url_user_day_report = "https://app.close.io/api/v1/report/activity/%s/?" % closeio_org

# Get the name of the organization - no touching.
org_url = 'https://app.close.io/api/v1/organization/%s/' % closeio_org
org_data = requests.get(org_url, auth=(closeio_key, ''), headers=headers)
org_name = org_data.json['name']