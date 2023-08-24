from common import *
from common_config import *
from abc import ABC, abstractmethod
from typing import final


class DocumentCreator(ABC):

    def __init__(self, configFile) -> None:
        with open(configFile, 'r') as config_file:
            config_data = json.load(config_file)

        self.module_folder = config_data["module_folder"]
        self.submodule = config_data["submodule"]

        self.csvLocs = [path.replace("${root_dir}", root_dir)
                        .replace("${module_folder}", self.module_folder)
                        .replace("${submodule}", self.submodule)
                        for path in config_data["csvLocs"]]

        self.jsonLocs = [path.replace("${root_dir}", root_dir)
                         .replace("${module_folder}", self.module_folder)
                         .replace("${submodule}", self.submodule)
                         for path in config_data["jsonLocs"]]

        self.jsonList = config_data["jsonList"]
        self.heading = config_data["heading"]
        self.content = config_data["content"]
        self.mandatoryFields = [path.replace("${root_dir}", root_dir)
                                .replace("${module_folder}", self.module_folder)
                                .replace("${submodule}", self.submodule)
                                for path in config_data["mandatoryFields"]]
        self.patchFields = [path.replace("${root_dir}", root_dir)
                            .replace("${module_folder}", self.module_folder)
                            .replace("${submodule}", self.submodule)
                            for path in config_data["patchFields"]]

    @final
    def add_content(self):

        AddSection(self.heading, self.content, self.csvLocs, '')

        for i, jsonLoc in enumerate(self.jsonLocs):
            if self.jsonList[i] in ["GET List", "GET by id"]:
                AddJsonSection(self.jsonList[i], None, jsonLoc)
            else:
                print(self.jsonList[i])
                AddJsonSection(self.jsonList[i], jsonLoc, None)
