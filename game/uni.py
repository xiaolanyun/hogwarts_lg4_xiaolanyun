# -*- coding: utf-8 -*-
# @Time	: 2021/2/25 20:04
# @Author	: xiaolan
# @File	: uni.py
import unittest
class search():
    def search(self):
        print("搜索")
        return True
#测试类注意继承
class TestClass(unittest.TestCase):
    #注意类方法前加注释
    @classmethod
    def setUpClass(cls):
        print("测试整个类前要执行的方法")
        cls.sea = search()
    def setUp(self):
        print("每一个测试方法前运行的方法")
    def tearDown(self):
        print("每一个测试方法后运行的方法")
    #注意测试用方法命名格式
    def test_func(self):
        print("测试方法1")
        # self.assertTrue(self.sea.search())
    def test_func2(self):
        print("测试方法2")
    @classmethod
    def tearDownClass(cls):
        print("测试整个类后要执行的方法")
if __name__ == '__main__':
    #使用该方式，unittest可以运行所有测试方法
    # unittest.main()
    #执行方法2，将测试用例加入到测试套件中
    #suite.addTest(类名(测试用例1))
    # suite = unittest.TestSuite()
    # suite.addTest(TestClass("test_func2"))
    # unittest.TextTestRunner().run(suite)
    #方法3，执行某些特定的测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=1).run(suite)