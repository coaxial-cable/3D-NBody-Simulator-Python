from config.ConfigManager import ConfigManager

def run():
    cm = ConfigManager()
    config = cm.getConfig()
    print(config)

run()