import requests
from common.read_config import ConfigUtils
from common import HTMLTestReportCN
import unittest
import os


case_path = os.path.join(os.path.dirname(__file__),'test_knowledge_case')
print(case_path)
discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test*.py',
                                               top_level_dir=case_path)

all_case_suit = unittest.TestSuite()
all_case_suit.addTest(discover)

# 设置测试报告位置
report_path = os.path.join(os.path.dirname(__file__),'report/')
# 创建报告的路径对象
report_dir = HTMLTestReportCN.ReportDirectory(report_path)
report_dir.create_dir('TEST_')

report_html_path =HTMLTestReportCN.GlobalMsg.get_value('report_path')
report_html_file = open(report_html_path,'wb')
html_runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_file,
                                              title='XX测试报告',
                                              description='shuoming',
                                              tester='name')
html_runner.run(all_case_suit)
