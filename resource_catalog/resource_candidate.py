from create_doc import *
from config import *


module_folder = "resource_catalog"
submodule = "candidate"


csvLocs = [f"{my_folder}/{module_folder}/csv/{submodule}/resourceCandidate.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceCategoryRef.csv", 
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceSpecificationRef.csv"]

jsonLocs = [f"{my_folder}/{module_folder}/json/{submodule}/resource_candidate_get_list.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_candidate_get_by_id.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_candidate_post.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_candidate_patch.json",]

jsonList = ["GET List", "GET by id", "POST", "PATCH"]

def add_content():
    global csvLocs, jsonLoc

    heading = "TMF634 Resource Resource Catalog - Resource Candidate"
    content = '''***Description:***
The resource candidate service allows controlling the Catalog -- that is, to activate and deactivate services that are present in the resource specification to be visible in the catalog or not.

***URL:*** /tmf-api/resourceCatalog/v4/resourceCandidate
***Supported methods:*** GET List, GET by ID, POST, PATCH, DELETE'''

    AddSection(heading, content, csvLocs,'')

    for i, jsonLoc in enumerate(jsonLocs):
        if jsonList[i] in ["GET List", "GET by id"]:
            print(jsonList[i])
            AddJsonSection(jsonList[i], None, jsonLoc)
        else:
            print(jsonList[i])
            AddJsonSection(jsonList[i], jsonLoc, None )




