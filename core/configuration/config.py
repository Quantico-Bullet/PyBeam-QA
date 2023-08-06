from pathlib import Path
import json

currDir = Path(__file__).parent

chambersFile = currDir / "data/chambers.json"
settingsFile = currDir / "data/settings.json"

with chambersFile.open(encoding="utf-8") as file:
    chambersConfig = json.load(file)

with settingsFile.open(encoding="utf-8") as file:
    settingsConfig = json.load(file)

class Config:
    def saveConfig(self, path: Path, config: dict):
        with open(path.absolute(), 'w', encoding="utf-8") as file:
            json.dump(config, file, indent=4, ensure_ascii=False)

class ChambersConfig(Config):
    path = chambersFile
    config = chambersConfig

    def saveConfig(self, config):
        self.config = config
        return super().saveConfig(self.path, config)
    
    def getConfig(self) -> dict:
        return self.config
    
class SettingsConfig(Config):
    path = settingsFile
    config = settingsConfig

    def saveConfig(self, config):
        self.config = config
        return super().saveConfig(self.path, config)
    
    def getConfig(self) -> dict:
        return self.config
