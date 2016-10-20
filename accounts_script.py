import urllib2
from selenium import webdriver
import time
import re

# config all types
cool_v1 = {"divisionCode":"SSCNHZ1"}
cool_school = {"mainRedemptionCode":"S15SCHOOLMAIN","freeRedemptionCode":"S15SCHOOLF1D","divisionCode":"SSCNSH1","productId":63}
cool_home = {"mainRedemptionCode":"S15HOMEPL20MAIN","freeRedemptionCode":"S15HOMEPL20F1D","divisionCode":"SSCNSH1","productId":64}
mini_school ={"mainRedemptionCode":"S15SCHOOLMAIN" ,"freeRedemptionCode":"S15SCHOOLF1D" ,"divisionCode":"CNMNXA2","productId":65}
mini_home ={"mainRedemptionCode":"S15HOMEPL20MAIN" ,"freeRedemptionCode":"S15HOMEPL20F1D" ,"divisionCode":"CNMNXA2","productId":66}

txt_file_path = r'EC_accounts.txt'
start_time_stamp = time.strftime("%Y%m%d%H%M%S")

def createmenber():
	url =r"https://uat1.englishtown.com/services/oboe2/salesforce/test/CreateMemberFore14hz"
	request = urllib2.Request(url)
	page = urllib2.urlopen(url)
	html = page.read()
	#href='ActivateForE14HZ?memberid=23847608'
	url2= re.search("memberid=(\d+)'",html)
	memberid=url2.group(1)
	list = html.split(',')
	return memberid,list[2]
#

def write_log(file_name, content):
    file_object = open(file_name, 'a+')
    file_object.write(content)
    file_object.close()

def put_value(driver,key,value):
	element=driver.find_element_by_name(key)
	element.clear()
	element.send_keys(value)
	time.sleep(0.3)

def main():
	types =['cool_v1','cool_school','cool_home','mini_school','mini_home']
	typedict =[cool_v1,cool_school,cool_home,mini_school,mini_home]
	print types
	yourtype = raw_input("please choose you type 1~4: ")
	id = int(yourtype)
	print "your type is: %s" %(types[id - 1])
	object = typedict[id - 1]
	numbers =raw_input("The numbers of account: ")
	if int(numbers) >= 1:
		for i in range (0,int(numbers)):
			memberid,username=createmenber()
			#start the firefox
			browser = webdriver.PhantomJS()
			url2=r"https://uat1.englishtown.com/services/oboe2/salesforce/test/ActivateForE14HZ?memberid=%s" %(memberid)
			print url2
			browser.get(url2)
			#browser.implicitly_wait(2)
			#browser.manage().window().maximize();
			for key in object:
				put_value(browser, key, object[key])

			browser.find_element_by_xpath("//form/input[@value='submit']").click()
			#browser.implicitly_wait(2)

			browser.quit()
			print username
			data = "| Time : %s | Type : %s |MemberId : %s |-----------------|UserName : %s\n" %(start_time_stamp, types[id - 1], memberid,username)
			write_log(txt_file_path,data)
			time.sleep(2)
		#wait.until(lambda driver: driver.find_element_by_id('someId'))
		#http://uat1.englishtown.com/services/oboe2/salesforce/test/ActivateForE14HZ
		#http://uat1.englishtown.com/services/oboe2/salesforce/test/CreateMemberFore14hz
		#browser.implicitly_wait(2)
	else:
		print "please type again"
		
if __name__ == '__main__':
 main()