import io
import sys #system-specific parameters and functions
import time
from selenium import webdriver #The selenium.webdriver module provides all the WebDriver implementations. Currently supported WebDriver implementations are Firefox, Chrome, IE and Remote. 
from selenium.webdriver.common.keys import Keys #The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.by import By #Set of supported locator strategies.(Eg: find_elements_by CLASS_NAME,ID,LINK_TEXT,NAME,CSS_SELECTOR,PARTIAL_LINK_TEXT,TAG_NAME,XPATH
from selenium.webdriver.support.ui import WebDriverWait #These days most of the web apps are using AJAX techniques. When a page is loaded by the browser, the elements within that page may load at different time intervals. This makes locating elements difficult: if an element is not yet present in the DOM, a locate function will raise an ElementNotVisibleException exception. Using waits, we can solve this issue.
from selenium.webdriver.support import expected_conditions as EC #The expected_conditions module contains a set of predefined conditions to use with WebDriverWait.
import pyperclip #Pyperclip is a cross-platform Python module for copy and paste clipboard functions. 
def main():

	inFile_hin = sys.argv[1]
	out_file = sys.argv[2]

	print "Important Note : Please check the usage policy of https://www.bing.com/translator before using it."
	time.sleep(2)

	#Opening Mozilla Firefox
	print("Opening browser...")
	browser = webdriver.Firefox()
	browser.minimize_window()

	#Opening Bing Translator
	print("Opening link...")
	browser.get('https://www.bing.com/translator')
	
	print("Reading input file...")
	
	#With the "With" statement, you get better syntax and exceptions handling.The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks."
	#open(file name, mode of opening) is used to open the file
	with open(inFile_hin,'r') as fin:
 		lines = fin.readlines()
		data = " ".join(str(x) for x in lines)
		english_input=unicode(data,"utf-8")
	
	print("Sending data to browser...")
	send_eng_inp = browser.find_element_by_id('t_sv')
	send_eng_inp.send_keys(english_input)

	src_options = browser.find_element_by_id('t_sl')
	src_options.click()

	tgt_options = browser.find_element_by_id('t_tl')
	tgt_options.click()

	select_hin = browser.find_element_by_xpath("//select[@id='t_tl']/option[text()='Hindi']").click()

	print("Translating...")
	print("Fetching translated data...")

	WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 't_copyIcon')))

	browser.find_element_by_id('t_copyIcon').click()

	hin_out = pyperclip.paste()

	with io.open(out_file, "a", encoding="utf-8") as fout:
		fout.write(hin_out)

	print("Translated data stored in \"" + out_file + "\" file.")
	
	browser.close()

if __name__ == '__main__':
	main()