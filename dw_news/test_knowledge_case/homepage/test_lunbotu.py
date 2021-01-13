# test case for login
import unittest
import requests
from common.read_config import ConfigUtils


class Login(unittest.TestCase):
    def setUp(self):
        self.home_page = ConfigUtils().HOST + '/portal/powerWiki/home'
        self.params = {'nodeId': 1333, 'uuid': 12345678}
        self.response_json = requests.post(url=self.home_page, params=self.params).json()

    def tearDown(self):
        pass

    def test_homepage_res(self):
        self._testMethodName = 'test homepage res'
        self._testMethodDoc = '测试homepage的res值是否正常'
        self.assertEqual(self.response_json['res'], 9007)

    def test_homepage_Rotation(self):
        self._testMethodName = 'test homepage Rotation chart '
        self._testMethodDoc = '测试homepage的轮播图是否存在'
        self.assertEqual(self.response_json['obj'][0]['type'], r'lunbo')

    def test_Rotation_number(self):
        self._testMethodName = 'test homepage Rotation chart number'
        self._testMethodDoc = '测试homepage的轮播图是否为5个'
        self.assertEqual(len(self.response_json['obj'][0]['list']), 5)

    def test_zixun(self):
        self._testMethodName = 'test homepage real-time info number'
        # 咨询数量不知道为什么只能请求到一个，暂时不写
        pass

    def test_hot(self):
        self._testMethodName = 'test homepage hot'
        self._testMethodDoc = '测试homepage的hot是否存在'
        self.assertEqual(self.response_json['obj'][2]['type'], 'list_view_one')

    def test_PopularCourses(self):
        self._testMethodName = 'test homepage PopularCourses'
        self._testMethodDoc = '测试homepage的PopularCourses是否存在'
        self.assertEqual(self.response_json['obj'][3]['list'][0]['name'], u'热门课程榜')

    def test_PopularCourses_number(self):
        self._testMethodName = 'test homepage PopularCourses number'
        self._testMethodDoc = '测试homepage的PopularCourses数量'
        self.assertNotEqual(len(self.response_json['obj'][3]['list'][0]['list']), 0)

if __name__ == '__main__':
    unittest.main()