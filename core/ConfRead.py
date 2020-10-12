import yaml
import os

Config_Path = os.path.dirname(__file__)

cf = open(Config_Path + "/../config.yaml", 'r', encoding='utf-8')
config = yaml.load(cf, Loader=yaml.FullLoader)

# 调用搜索语句
query = config['Query']['query']
print(type(query), query)

# 调用Fofa配置信息
USE_FofaApi = config['Fofa']['USE_FofaApi']
FOFA_EMAIL = config['Fofa']['FOFA_EMAIL']
FOFA_KEY = config['Fofa']['FOFA_KEY']

# 调用Shodan配置信息
USE_ShodanApi = config['Shodan']['USE_ShodanApi']
Shodan_Api = config['Shodan']['Shodan_Api']

# 调用exp/poc脚本
FUNCTION = config['Function']['FUNCTION']
