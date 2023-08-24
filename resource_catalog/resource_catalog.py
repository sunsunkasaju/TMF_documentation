from create_doc import *
from config import *


module_folder = "resource_catalog"
submodule = "catalog"


csvLocs = [f"{my_folder}/{module_folder}/csv/{submodule}/resourceCatalog.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceRelatedParty.csv", 
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceCategoryRef.csv",]

jsonLocs = [f"{my_folder}/{module_folder}/json/{submodule}/resource_catalog_get_list.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_catalog_get_by_id.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_catalog_post.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_catalog_patch.json",]

jsonList = ["GET List", "GET by id", "POST", "PATCH"]

def add_content():
    global csvLocs, jsonLocบ

    heading = "TMF634 Resource Resource Catalog - Resource Catalog"
    content = '''***Description:***
This is a resource catalog of all the available 'resource specification' that are available for deployment (controlled by resource candidate).

***URL:*** /tmf-api/resourceCatalog/v4/resourceCatalog
***Supported methods:*** GET List, GET by ID, POST, PATCH, DELETE'''

    AddSection(heading, content, csvLocs,'')

    for i, jsonLoc in enumerate(jsonLocs):
        if jsonList[i] in ["GET List", "GET by id"]:
            print(jsonList[i])
            AddJsonSection(jsonList[i], None, jsonLoc)
        else:
            print(jsonList[i])
            AddJsonSection(jsonList[i], jsonLoc, None )
