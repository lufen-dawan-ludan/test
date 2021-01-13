#放置请求
import requests
import os
from nb_log import LogManager
from common.read_config import ConfigUtils
from requests.exceptions import ReadTimeout, ConnectionError, RequestException

log_filename = os.path.join(os.path.dirname(__file__),'logs','log.log')

class ApiInfo:

    def __init__(self):
        self.home_page_url = ConfigUtils().HOST + '/portal/powerWiki/home'
        self.params = {'nodeId': 1333, 'uuid': 12345678}
        self.logger = LogManager('home_api').get_logger_and_add_handlers(10)

    def home_page_api(self):
        self.logger.info('调用获取home接口开始')
        response_json = None
        try:
            response_json = requests.post(url=self.home_page_url, params=self.params).json()
        except RequestException as e:
            self.logger.error('调用获取home接口失败，原因是%s'%e.__str__())
        return response_json
if __name__ == '__main__':
        res = ApiInfo().home_page_api()
