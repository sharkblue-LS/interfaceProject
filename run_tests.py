import time,sys,os
import unittest
sys.path.append('./db_fixture')
sys.path.append('./TestReport-master/Local')
from db_fixture import test_data
from interface import add_event_test
from interface import selenium_img_test
from TestReport_local import HTMLTestReport,HTMLTestReportEN


#指定测试用例为当前文件夹下的interface目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

# if __name__ == '__main__':
#     test_data.init_data()
#     suite = unittest.TestSuite()
#     suite.addTest(add_event_test.AddEventTest('test_add_event_all_null'))
#     suite.addTest(add_event_test.AddEventTest('test_add_event_eid_exist'))
#     suite.addTest(add_event_test.AddEventTest('test_add_event_name_exist'))
#     suite.addTest(add_event_test.AddEventTest('test_add_event_data_type_error'))
#     suite.addTest(add_event_test.AddEventTest('test_add_event_success'))
#
#     with open('./report/TestReport.html', 'wb') as report:
#         runner = HTMLTestReport(stream=report,
#                                 verbosity=2,
#                                 title='TestReport 测试',
#                                 description='带截图，带饼图，带详情',
#                                 tester='shark')
#         runner.run(suite)

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(selenium_img_test.Case_baidu)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(selenium_img_test.Case_qq)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(selenium_img_test.Case_163)
    suites = unittest.TestSuite()
    # suites.addTest(selenium_img_test.Case_baidu('test_baidu_search'))
    # suites.addTest(selenium_img_test.Case_baidu('test_baidu_assert_ok'))
    
    suites.addTests([suite1, suite2, suite3])
    
    # HTMLTestReport or HTMLTestReportEN
    with open('./report/TestReportIMG.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                images=True,
                                title='TestReport 测试',
                                description='带截图，带饼图，带详情',
                                tester='shark')
        runner.run(suites)
    
    