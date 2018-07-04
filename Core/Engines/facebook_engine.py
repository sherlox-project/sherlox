import requests
import scrapy
import mechanize
import cookielib
import urllib2

from bs4 import BeautifulSoup

class FacebookEngine:
	cookiejar = cookielib.LWPCookieJar()
	id = "facebook"
	auth_token = ""
	br = mechanize.Browser()
	br.set_cookiejar(cookiejar)
	br.set_handle_equiv( True )
	br.set_handle_gzip( True )
	br.set_handle_redirect( True )
	br.set_handle_referer( True )
	br.set_handle_robots( False )
	

	def __init__(self):
		url = 'https://www.facebook.com/login.php?login_attempt=1'
		self.br.open(url)
		self.br.select_form(nr = 0)       #This is login-password form -> nr = number = 0
		self.br.form['email'] = "nomail"
		self.br.form['pass'] = "nopass"
		response = self.br.submit()
		print(response.geturl())


	def run_username_osint(self, user_name):
		url = self.username_exists(user_name)
		if (url != None):
			return self.extract_info(url)
		else :
			return "No Username Found on Facebook"


	def username_exists(self, user_name):
		url = "http://www.facebook.com/" + user_name
		fb_profile = self.br.open(url)
		print(fb_profile.code)
		if (fb_profile.code == 200):
			return url
		else:
			return None

	def extract_info(self, url):
		about_url = url + "/about?section=overview"
		about_dom = self.br.open(about_url).read(), "html.parser"
		