import io
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
def main():

	inFile_hin = sys.argv[1]
	out_file = sys.argv[2]
	print "Important Note : Please check the usage policy of https://www.bing.com/translator before using it."
	time.sleep(2)
	print("Opening browser...")
	browser = webdriver.Firefox()
	browser.minimize_window()
	print("Opening link...")
	browser.get('https://www.bing.com/translator')
	
	print("Reading input file...")
	
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

	

	# select_hin = browser.find_element_by_xpath("//select[@id='t_tl']/option[text()='Hindi']").click()

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