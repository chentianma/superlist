# coding: utf-8

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_start_a_list_and_retrieve_it(self):

        # 去看应用首页
        self.browser.get('http://localhost:8000')
        # 检查网页标题内是否有“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        # 应用邀请他输入一个待办事项.....


if __name__ == '__main__':
    unittest.main()