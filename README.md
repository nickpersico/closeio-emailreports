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

1. Sign up for DigitalOcean and create a droplet: `$5/month - 512MB NY3, Ubuntu 14.04 x64`
2. Once the droplet gets created, DigitalOcean will email you a root password that you can log into.
3. Get on the command line and login to your droplet using the password: `ssh root@100.200.300.40`
4. Once logged in, you should see `root@YOUR_DROPLET_NAME:~#`. This is good.
5. Type `cd ..` to get into the root of your droplet.
6. Install Git so you can clone the repo: `sudo apt-get install git-core`.
7. Install setuptools so we can get pip installed: `curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | sudo python -`
8. Install pip: ` curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python -`
9. Clone the repo: `git clone https://github.com/nickpersico/closeio-emailreports.git`.
10. Get into the new repo by typing `cd closeio-emailreports`.
11. Install the necessary dependencies: `pip install -r requirements.txt`
12. Set up your `_settings.py` and `_keys.py` file.
13. See steps 5-10 above. I recommend opening these files using nano: `sudo nano _keys.py`.
14. nano can be tricky for beginners. The keys are `CTRL + O` to save, and `CTRL + X` to exit.
15. Now we need to automate the script to run once a day. We'll do by typing `crontab -e`.
16. Arrow down until you get to blank space below the comments, and now we'll add a cron job.
17. I like my daily email reports to come out at around 6:30PM Monday-Friday.
18. The cron job command for that is `21 18 * * 1-5 python /closeio-emailreports/email_report.py`
19. Hit CTRL + O, Enter, and CTRL + X to save. You should see a message list this: `crontab: installing new crontab`
20. You'll know it worked if you & your team received an email at 6:30PM (local time on the server)!

Please Note: I highly recommend testing the script in testing mode prior to setting up a cron job. The last thing you want is to spam your co-workers when setting this up!

### Questions? Need a custom report?

Send me a [note](mailto:nicklpersico@gmail.com?subject=Close.io Email Reports) or a [tweet](https://www.twitter.com/@NickPersico). Pull requests welcome!