from selenium import webdriver

browser = webdriver.Chrome ()
browser.maximize_window ()
username = "user"  # stands for !@user
password = "Password"  # stands for ^&pass
url = "localhost/grwl/Login.aspx"
webUrl = 'http://{}:{}@{}'.format (username, password, url)
browser.get (webUrl)
