from create_doc import *
from config import *


module_folder = "service_catalog"
submodule = "category"


csvLocs = [f"{my_folder}/{module_folder}/csv/{submodule}/serviceCategory.csv", 
           f"{my_folder}/{module_folder}/csv/{submodule}/serviceCandidateRef.csv", 
           f"{my_folder}/{module_folder}/csv/{submodule}/serviceCategoryRef.csv"]

jsonLocs = [f"{my_folder}/{module_folder}/json/{submodule}/service_category_get_list.json",
            f"{my_folder}/{module_folder}/json/{submodule}/service_category_get_by_id.json",
            f"{my_folder}/{module_folder}/json/{submodule}/service_category_post.json",
            f"{my_folder}/{module_folder}/json/{submodule}/service_category_patch.json",]

jsonList = ["GET List", "GET by id", "POST", "PATCH"]

def add_content():
    global csvLocs, jsonLoc

    heading = "TMF633 Service Service Catalog - Service Category"
    content = '''**Description:**
This service is used to define categories that can be applied to Services.

**URL:** /tmf-api/serviceCatalog/v5/serviceCategory
**Supported methods:** GET List, GET by ID, POST, PATCH, DELETE'''

    AddSection(heading, content, csvLocs,'')

    for i, jsonLoc in enumerate(jsonLocs):
        if jsonList[i] in ["GET List", "GET by id"]:
            print(jsonList[i])
            AddJsonSection(jsonList[i], None, jsonLoc)
        else:
            print(jsonList[i])
            AddJsonSection(jsonList[i], jsonLoc, None )




