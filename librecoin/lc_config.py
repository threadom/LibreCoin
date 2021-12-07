# import JSON
import json

class lc_config:
    def __init__(self, config_path: str):
        self.m_config = False

        with open(config_path) as datas_config:
            self.m_config = json.load(datas_config)
        
    def get(self, property_name):
        if property_name in self.m_config:
            return self.m_config[property_name]
        print("Missing property '" + property_name + "' in config.json")
        sys.exit()