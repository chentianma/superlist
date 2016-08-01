# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

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
        self.browser.get('http://localhost:8000')

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
        inputbox.send_keys('1.买一台Macbook Pro')

        # 点击回车确定，页面刷新
        # 待办事项表格中显示了“1.买一台Macbook Pro”
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1.买一台Macbook Pro')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('2.一个苹果的故事')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1.买一台Macbook Pro')
        self.check_for_row_in_list_table('2.一个苹果的故事')

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 输入其他待办事项
        # 结束


if __name__ == '__main__':
    unittest.main()