Note:
 -  代码目前仅支持python2, 已通过2.7.10下运行测试

Info:
 - 测试框架基于selenium + pytest + pytest-html

Construct:


				|-----  cases      :  测试用例
				|-----  common     :  配置文件
				|-----  driver     :  浏览器驱动
	               Test ----|-----  logs       :  日志文件
				|-----  pages      :  页面对象
				|-----  reports    :  测试报告
				|-----  utils      :  封装方法
