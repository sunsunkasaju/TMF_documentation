from create_doc import *
from config import *


module_folder = "resource_catalog"
submodule = "category"


csvLocs = [f"{my_folder}/{module_folder}/csv/{submodule}/resourceCategory.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceRelatedParty.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceCandidateRef.csv", 
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceCategoryRef.csv",]

jsonLocs = [f"{my_folder}/{module_folder}/json/{submodule}/resource_category_get_list.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_category_get_by_id.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_category_post.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_category_patch.json",]

jsonList = ["GET List", "GET by id", "POST", "PATCH"]

def add_content():
    global csvLocs, jsonLocบ

    heading = "TMF634 Resource Resource Catalog - Resource Category"
    content = '''***Description:***
This service allows managing the categories that can be used for resources.

***URL:*** /tmf-api/resourceCatalog/v4/resourceCategory
***Supported methods:*** GET List, GET by ID, POST, PATCH, DELETE'''

    AddSection(heading, content, csvLocs,'')

    for i, jsonLoc in enumerate(jsonLocs):
        if jsonList[i] in ["GET List", "GET by id"]:
            print(jsonList[i])
            AddJsonSection(jsonList[i], None, jsonLoc)
        else:
            print(jsonList[i])
            AddJsonSection(jsonList[i], jsonLoc, None )
