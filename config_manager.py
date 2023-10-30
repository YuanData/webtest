import configparser


class ConfigManager:
    def __init__(self, config_path='../setting/config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_domain(self, env):
        return self.config[env]['domain']
