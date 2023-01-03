from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

GECKO_PATH = "/Users/jonathanconroy/Downloads/geckodriver"

profile_path = "/Users/jonathanconroy/Library/Application Support/Firefox/Profiles/b9n4pvsl.default-release"
options = Options()
# options.set_preference('profile', profile_path)
# options.set_preference("user-data-dir","/Users/jonathanconroy/Documents/Dartmouth/MiscCoding/GooseThings/CookiesTest")
options.add_argument("--user-data-dir=/Users/jonathanconroy/Library/Application Support/Google/Chrome")
options.add_argument("--profile-directory=Default")


driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get("https://www.wsj.com/")
input()