import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Case_baidu(unittest.TestCase):
    '''
    在python3中因为unittest运行机制变动，在使用setUp/tearDown中初始化/退出driver时，会出现用例执行失败没有截图的问题，
    所以推荐使用样例中setUpClass/tearDownClass的用法
    '''
    def setUp(self):
        self.imgs = []
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def get_screenshot(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def test_baidu_search(self):
        '''用例通过，没有报告内容，有多张截图'''
        self.driver.get("https://www.baidu.com")
        self.get_screenshot()
        self.driver.find_element(By.ID,'kw').send_keys(u'百度一下')
        self.get_screenshot()
        self.driver.find_element(By.ID,'su').click()
        self.get_screenshot()

    def test_baidu_assert_ok(self):
        '''用例通过，有报告内容，有截图'''
        self.driver.get("https://www.baidu.com")
        hao123 = self.driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[2]').text
        print(hao123)
        self.get_screenshot()
        self.assertEqual(hao123, 'hao123')

    def test_baidu_assert_ok_noimg(self):
        '''用例通过，有报告内容，没有截图'''
        self.driver.get("https://www.baidu.com")
        news = self.driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[1]').text
        print(news)
        self.assertEqual(news, u"新闻")

    def test_baidu_assert_faile(self):
        '''用例失败，带有失败内容和截图'''
        self.driver.get("https://www.baidu.com")
        self.get_screenshot()
        news = self.driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[1]').text
        print(news)
        self.get_screenshot()
        self.driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[2]').click()
        self.get_screenshot()
        self.assertEqual(news, 'hao123')

    def test_baidu_assert_error(self):
        ''''用例错误，带有指定错误内容和截图'''
        self.driver.get("https://www.baidu.com")
        self.get_screenshot()
        raise EnvironmentError('Current environment can not testing!')

class Case_qq(unittest.TestCase):
    '''
    在python3中因为unittest运行机制变动，在使用setUp/tearDown中初始化/退出driver时，会出现用例执行失败没有截图的问题，
    所以推荐使用样例中setUpClass/tearDownClass的用法
    '''
    def setUp(self):
        self.imgs = []
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_qq_index_faile(self):
        '''用例错误，带有错误内容和没有截图'''
        self.driver.get("https://www.qq.com")
        self.driver.find_element(By.ID,'sougouTxt').send_keys(u'搜狗搜索')
        # self.driver.find_element_by_id('sougouTxt').send_keys(u'搜狗搜索')
        self.driver.find_element(By.ID,'searchBtn').click()
        self.assertIn(u"搜狗", u'搜索')

    def test_qq_index_ok(self):
        '''用例通过，没有内容和没有截图'''
        self.driver.get("https://www.qq.com")
        self.driver.find_element(By.ID,'sougouTxt').send_keys(u'搜狗搜索')
        self.driver.find_element(By.ID,'searchBtn').click()

class Case_163(unittest.TestCase):
    def setUp(self):
        self.imgs = []
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_163_ok(self):
        '''通过 没有内容和截图'''
        self.driver.get("https://www.163.com/")