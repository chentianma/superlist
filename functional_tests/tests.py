# coding: utf-8

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def tearDown(self):
        self.browser.quit()
        print('Finish the test!')

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows],
                      'New To-Do list did not appear in table, the text was:\n%s' % row_text)

    def test_start_a_list_and_retrieve_it(self):

        # 去看应用首页
        self.browser.get(self.live_server_url)

        # 检查网页标题内是否有“To-Do”这个词
        self.assertIn('To-Do', self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', head_text)

        # 应用邀请他输入一个待办事项.....
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 在文本框里输入“买一台Macbook Pro”
        inputbox.send_keys('买一台Macbook Pro')

        # 点击回车确定，页面刷新
        # 待办事项表格中显示了“1.买一台Macbook Pro”
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/list/.+')
        self.check_for_row_in_list_table('1:买一台Macbook Pro')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('一个苹果的故事')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1:买一台Macbook Pro')
        self.check_for_row_in_list_table('2:一个苹果的故事')

        # 一个新用户访问了网站
        # 使用一个新的浏览器会话
        # 保证之前的用户信息不会从cookie中泄露
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 访问首页
        # 页面中看不到用户1的清单



# if __name__ == '__main__':
#     unittest.main()