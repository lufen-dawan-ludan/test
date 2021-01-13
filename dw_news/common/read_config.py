import configparser
import os

ConfigPath = os.path.join(os.path.dirname(__file__),'..','config/config.ini')


class ConfigUtils:
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(ConfigPath,encoding='utf-8')

    @property
    def HOST(self):
        host_value = self.cfg.get('default','HOST')
        return host_value

if __name__ == '__main__':
    host = ConfigUtils().HOST
    print(host)