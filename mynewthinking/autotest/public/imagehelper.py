import os
import platform
import tempfile
import shutil

from PIL import Image

PATH = lambda p: os.path.abspath(p)
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")


class Appium_Extend(object):
    def __init__(self, driver):
        self.driver = driver

    def get_screenshot_by_element(self, element):
        # 先截取整个屏幕，存储至系统临时目录下
        self.driver.get_screenshot_as_file(TEMP_FILE)

        # 获取元素bounds
        location = element.location
        size = element.size
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])

        # 截取图片
        image = Image.open(TEMP_FILE)
        newImage = image.crop(box)
        newImage.save("/Users/anderson/testcode/mynewthinking/b.png")

        return self

    def get_screenshot_by_custom_size(self, start_x, start_y, end_x, end_y):
        # 自定义截取范围
        self.driver.get_screenshot_as_file(TEMP_FILE)
        box = (start_x, start_y, end_x, end_y)

        image = Image.open(TEMP_FILE)
        newImage = image.crop(box)
        newImage.save(TEMP_FILE)

        return self

    def write_to_file(self, dirPath, imageName, form="png"):
        # 将截屏文件复制到指定目录下
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)
        shutil.copyfile(TEMP_FILE, PATH(dirPath + "/" + imageName + "." + form))

    def load_image(self, image_path):
        # 加载目标图片供对比用
        if os.path.isfile(image_path):
            load = Image.open(image_path)
            return load
        else:
            raise Exception("%s is not exist" % image_path)

    #
    # def same_as(self, load_image, percent):
    #     # 对比图片，percent值设为0，则100%相似时返回True，设置的值越大，相差越大
    #     import math
    #     import operator
    #
    #     image1 = Image.open(TEMP_FILE)
    #     image2 = load_image
    #
    #     histogram1 = image1.histogram()
    #     histogram2 = image2.histogram()
    #
    #     differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2)))/len(histogram1))
    #     if differ <= percent:
    #         return True
    #     else:
    #         return False
    def get_location_by_element(self, element, num):

        location = element.location
        size = element.size
        # box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])
        positions = []
        partx = size["width"] / num
        print(location["x"], location["y"])
        for i in range(num):
            x = int(location["x"] + (1 / 2 + i) * partx)
            y = int(location["y"] + (1 / 2) * size["height"])
            positions.append([(x, y)])
        return positions
