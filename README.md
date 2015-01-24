Close.io Email Reports
===============

A python script that will send a daily sales email report to the users in your Close.io organization. Follow the below tutorial to automate the email reports with a $5/month DigitalOcean droplet.

![Email Report Screenshot](https://raw.githubusercontent.com/nickpersico/closeio-emailreports/master/templates/img/email_screenshot.png)

### What's Included The Report

* Individual stats [daily, weekly]:
	* Calls
	* Call duration
	* Opportunities created [amount, value]
	* Opportunities won [amount, value]
* Team stats for admins [daily, weekly]:
	* Calls
	* Call duration
	* Opportunities created [amount, value]
	* Opportunities won [amount, value]
* Leaderboard stats [weekly]:
	* Calls
	* Opportunities created [amount, value]
	* Opportunities won [amount, value]

### Options

* Send a total team report to the admin(s).
* Ignore certain members that don't want to receive the emails.
* Send an email to someone outside of your Close.io organization.
* A testing mode so you don't spam your team during setup.

### What You'll Need

* Close.io API key and organization ID with admin access.
* A [Mailgun account](https://mailgun.com/signup) to send the emails to your team.
* A [DigitalOcean account](https://www.digitalocean.com/?refcode=f6819c14de70) to run the daily email via a cron job.

### Running The Script Locally

1. Clone the repository to your local machine.
2. Navigate to the folder via the command line: `cd closeio-emailreports`
3. Initiate a virtual environment: `virtualenv venv`
4. Load up the virtual environment: `source venv/bin/activate`
4. Install the necessary dependencies: `pip install -r requirements.txt`
5. Open up the `_keys.py` file in your favorite text editor.
6. Add your Close.io API key, Close.io organization ID, Mailgun API key, and Mailgun domain.
7. Open up the `_settings.py` file and follow steps 1-6 to fill in the appropriate information.
8. Run the script from the command line: `python email_reports.py`.
9. If you kept `testing_mode = True` in `_settings.py`, you should receive email reports for each person in your organization. You will also receive the admin team report.
10. To go into live mode, change the `testing_mode` to `False` in `_settings.py`.
11. Booyah!

### Automate The Report With DigitalOcean

### Questions? Need a custom report?

Send me a [note](mailto:nicklpersico@gmail.com?subject=Close.io Email Reports) or a [tweet](https://www.twitter.com/@NickPersico). Pull requests welcome!