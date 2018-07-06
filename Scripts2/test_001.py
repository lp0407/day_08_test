import allure
class Test_001:
    def test_001(self):
        allure.attach("这是一个描述","我是具体内容")
        assert 0

    def test_002(self):
        assert 1