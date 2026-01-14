import yaml

class ConfigManager:
    
    def __init__(self):
        with open("config.yaml","r") as yamlFile:
            self.config = yaml.safe_load(yamlFile)

    def getConfig(self):
        return self.config