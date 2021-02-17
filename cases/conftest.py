import pytest




# '''
# 1、可以跨.py文件调用，有多个.py文件调用时，可让conftest.py只调用了一次fixture，或调用多次fixture
#
# 2、conftest.py与运行的用例要在同一个pakage下，并且有__init__.py文件
#
# 3、不需要import导入 conftest.py，pytest用例会自动识别该文件，放到项目的根目录下就可以全局目录调用了，如果放到某个package下，那就在改package内有效，可有多个conftest.py
#
# 4、conftest.py配置脚本名称是固定的，不能改名称
#
# 5、conftest.py文件不能被其他文件导入
#
# 6、所有同目录测试文件运行前都会执行conftest.py文件
#
# 2、fixture的作用范围
# fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function
#
# -function：每一个函数或方法都会调用
#
# -class：每一个类调用一次，一个类中可以有多个方法
#
# -module：每一个.py文件调用一次，该文件内又有多个function和class
#
# -session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
#
# function默认模式@pytest.fixture(scope='function')或 @pytest.fixture()
#
# 3、conftest结合fixture的使用
# conftest中fixture的scope参数为session，所有测试.py文件执行前执行一次
#
# conftest中fixture的scope参数为module，每一个测试.py文件执行前都会执行一次conftest文件中的fixture
#
# conftest中fixture的scope参数为class，每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture
#
# conftest中fixture的scope参数为function，所有文件的测试用例执行前都会执行一次conftest文件中的fixture
# '''
from ac.base import BaseTest


@pytest.fixture(scope='function', autouse=True)
def setCookies():
    BaseTest.setCookie()

