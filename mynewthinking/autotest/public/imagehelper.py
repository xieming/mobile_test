from PIL import Image
from autotest.Base import Base_page

class IMAGE(Base_page):

    def get_picture(self,locate):

    # url='http://xxxxx.com'
    # driver = webdriver.Chrome()
    # driver.maximize_window()  #将浏览器最大化
    # driver.get(url)
        self.driver.save_screenshot('aa.png')  #截取当前网页，该网页有我们需要的验证码
        imgelement = self.driver.find_element_by_xpath(locate)  #定位验证码
        location = imgelement.location  #获取验证码x,y轴坐标
        size=imgelement.size  #获取验证码的长宽
        rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])) #写成我们需要截取的位置坐标
        i=Image.open("aa.png") #打开截图
        frame4=i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save('frame4.jpg')