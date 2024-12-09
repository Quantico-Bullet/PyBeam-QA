# PyBeam QA
# Copyright (C) 2024 Kagiso Lebang
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pathlib import Path
import json

currDir = Path(__file__).parent

chambersFile = currDir / "data/chambers.json"
settingsFile = currDir / "data/settings.json"
workspaceFile = currDir / "data/workspace.json"

with chambersFile.open(encoding="utf-8") as file:
    chambersConfig = json.load(file)

with settingsFile.open(encoding="utf-8") as file:
    settingsConfig = json.load(file)

with workspaceFile.open(encoding="utf-8") as file:
    workspaceConfig = json.load(file)

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
    
class WorkspaceConfig(Config):
    path = workspaceFile
    config = workspaceConfig

    def saveConfig(self, config):
        self.config = config
        return super().saveConfig(self.path, config)
    
    def getConfig(self) -> dict:
        return self.config
