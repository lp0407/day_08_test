import allure
class Test_001:
    @allure.step(title="第一个测试")
    def test_001(self):
        allure.attach("这是一个描述","我是具体内容")
        assert 0

    @allure.step(title="测试步骤002")
    def test_002(self):
        assert 1