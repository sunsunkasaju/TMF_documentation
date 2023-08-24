from create_doc import *
from config import *


module_folder = "service_catalog"
submodule = "specification"


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

    heading = "TMF633 Service Service Catalog - Service Specification"
    content = '''***Description:***
This service allows managing the specification of services. These specifications are used when placing orders. The relationships of CFS -> RFS and RFS -> Resoures etc are defined as part of the Specification. The specification also includes the variables that are expected, their data-types etc. It also holds dynamic logic about how CFS->RFS invocations happen and how derived fields are calculated. (More details in detailed section).

***URL:*** /tmf-api/serviceCatalog/v5/serviceSpecification
***Supported methods:*** GET List, GET by ID, POST, PATCH, DELETE'''

    AddSection(heading, content, csvLocs,'')

    for i, jsonLoc in enumerate(jsonLocs):
        if jsonList[i] in ["GET List", "GET by id"]:
            print(jsonList[i])
            AddJsonSection(jsonList[i], None, jsonLoc)
        else:
            print(jsonList[i])
            AddJsonSection(jsonList[i], jsonLoc, None )




