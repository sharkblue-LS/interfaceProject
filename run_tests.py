import time,sys,os
import unittest
sys.path.append('./db_fixture')
sys.path.append('./TestReport-master/Local')
from db_fixture import test_data
from interface import add_event_test
from TestReport_local import HTMLTestReport

#指定测试用例为当前文件夹下的interface目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == '__main__':
    test_data.init_data()
    suite = unittest.TestSuite()
    suite.addTest(add_event_test.AddEventTest('test_add_event_all_null'))
    suite.addTest(add_event_test.AddEventTest('test_add_event_eid_exist'))
    suite.addTest(add_event_test.AddEventTest('test_add_event_name_exist'))
    suite.addTest(add_event_test.AddEventTest('test_add_event_data_type_error'))
    suite.addTest(add_event_test.AddEventTest('test_add_event_success'))
    
    with open('./report/TestReport.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='TestReport 测试',
                                description='带截图，带饼图，带详情',
                                tester='shark')
        runner.run(suite)
    
    # now = time.strftime('%Y-%m-%d %H:%M:%S')
    # filename = './report/'+ now + '_result.html'
    # fp = open(filename,'wb')
    # runner = HTMLTestRunner(stream=fp,title='Guest Manage System interface Test Report',description='Implementation Example with:')
    # runner.run(discover)
    # fp.close()
    