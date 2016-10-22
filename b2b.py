#coding=utf-8
import os
import re
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
'''
url = "http://uatdeepblue2.englishtown.com/commerce/batchmanagement/default.aspx"
<input id="file" class="file" type="file" size="32" name="file">
input id="select"
<input class="submit" type="submit" title="Upload Participant List" value="Upload Participant List"
<input id="batchName"
'''
host_path = r"C:\Windows\System32\drivers\etc\hosts"
B2B_UAT_HOST = ["#B2B uat deepblue2",
'10.128.34.183 uat.englishtown.com',
'10.128.34.183 uat-cache.englishtown.com',
'10.128.34.233 uatdeepblue2.englishtown.com',
'10.128.34.233 uatdeepblue2cn.englishtown.com']

def search_host(hostvalue,host_path):
	hostfile = open(host_path,'r')
	each_line = hostfile.readlines()
	hostfile.close()
	findresult = re.findall(hostvalue,''.join(each_line))
	return findresult


def write_host(hostvalue,host_path):
    output = open(host_path, 'a')
    for insid in hostvalue:
        print insid
        output.write(insid)
        output.write("\n")
    output.close()

def put_value(driver,key,value):
	element=driver.find_element_by_name(key)
	element.clear()
	element.send_keys(value)
	time.sleep(0.3)

if __name__ == "__main__":
    #inside_test()
	if search_host(B2B_UAT_HOST[0],host_path):
		print "it exist, no need to update"
	else:
		write_host(B2B_UAT_HOST,host_path)
	browser = webdriver.Firefox()
	url2=r"http://uatdeepblue2.englishtown.com/commerce/batchmanagement/default.aspx"
	print url2
	browser.get(url2)
	#browser.find_element_by_id('file').click()
	browser.find_element_by_id('file').send_keys(r"E:\accountscript\batch_template.xls")
	time.sleep(2)
	browser.find_element_by_id('select').click()
	browser.find_element_by_id('batchName').send_keys(r"kist")
	browser.find_element_by_class_name(r'submit').click()
	time.sleep(2)
	#driver.switch_to_window("")
	
	browser.switch_to_alert()
	time.sleep(2)
	keyvalue = browser.find_element_by_id("btnCloseFailWin")
	if keyvalue.is_displayed():
		browser.find_element_by_id("btnCloseFailWin").click()
		browser.save_screenshot('screenshot.png')
		print "fail"

	else:
			#The file you just uploaded has passed the data validation
		browser.find_element_by_id("btnCreateBatch").click()
		time.sleep(5)
		#browser.switch_to_window("successWindow")
		#browser.switch_to_alert()
#/html/body/div[1]/div[2]/div[2]/form/fieldset/div[3]/div[5]/input[1]
#driver.findElement(By.xpath("//a[contains(text(),"+username+")]"))
		browser.find_element_by_xpath("//div[2]/form/fieldset/div[3]/div[5]/input[1]").click()
		time.sleep(3)
		browser.find_element_by_id("select").click()
		#select = browser.find_element_by_id("select")
		#select.select_by_visible_text("Create Order")
		#select.select_by_visible_text("Edam")
		#select.select_by_index[1]
		#Select(browser.find_element_by_name("select")).select_by_visible_text("Create Order")
		select = browser.find_element_by_id("select")
		selects = browser.find_elements_by_tag_name("option")
		selects[1].click()
		time.sleep(2)
		browser.find_element_by_id('actionButton').click()
		time.sleep(2)
		browser.switch_to_alert()
		time.sleep(1)
		browser.find_element_by_id('createOrderBtn').click()
		
	
	
	browser.close()
	
	
	
	
	