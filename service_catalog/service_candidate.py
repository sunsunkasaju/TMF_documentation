from create_doc import *
from config import *


module_folder = "service_catalog"
submodule = "candidate"


csvLocs = [f"{my_folder}/{module_folder}/csv/{submodule}/serviceCandidate.csv", 
           f"{my_folder}/{module_folder}/csv/{submodule}/serviceCategoryRef.csv"]

jsonLocs = [f"{my_folder}/{module_folder}/json/{submodule}/service_candidate_get_list.json",
            f"{my_folder}/{module_folder}/json/{submodule}/service_candidate_get_by_id.json",
            f"{my_folder}/{module_folder}/json/{submodule}/service_candidate_post.json",
            f"{my_folder}/{module_folder}/json/{submodule}/service_candidate_patch.json",]

jsonList = ["GET List", "GET by id", "POST", "PATCH"]

def add_content():
    global csvLocs, jsonLoc

    heading = "TMF633 Service Service Catalog - Service Candidate"
    content = '''***Description:***
This service indirectly controls the catalog. By adding a specification as candidate it makes the service available in the catalog.

***URL:*** /tmf-api/serviceCatalog/v5/serviceCandidate
***Supported methods:*** GET List, GET by ID, POST, PATCH, DELETE'''

    AddSection(heading, content, csvLocs,'')

    for i, jsonLoc in enumerate(jsonLocs):
        if jsonList[i] in ["GET List", "GET by id"]:
            print(jsonList[i])
            AddJsonSection(jsonList[i], None, jsonLoc)
        else:
            print(jsonList[i])
            AddJsonSection(jsonList[i], jsonLoc, None )




