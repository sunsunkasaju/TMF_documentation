from create_doc import *
from config import *


module_folder = "resource_catalog"
submodule = "specification"


csvLocs = [f"{my_folder}/{module_folder}/csv/{submodule}/resourceSpecification.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/attachmentRefOrValue.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/featureSpecification.csv", 
           f"{my_folder}/{module_folder}/csv/{submodule}/featureSpecificationCharacteristic.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/featureSpecificationCharacteristicRelationship.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/featureSpecificationCharacteristicValue.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/featureSpecificationRelationship.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/quantity.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/relatedParty.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceSpecificationCharacteristic.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceSpecificationCharacteristicRelationship.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceSpecificationCharacteristicValue.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/resourceSpecificationRelationship.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/targetResourceSchema.csv",
           f"{my_folder}/{module_folder}/csv/{submodule}/constraintRef.csv",]

           

jsonLocs = [f"{my_folder}/{module_folder}/json/{submodule}/resource_specification_get_list.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_specification_get_by_id.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_specification_post.json",
            f"{my_folder}/{module_folder}/json/{submodule}/resource_specification_patch.json",]

jsonList = ["GET List", "GET by id", "POST", "PATCH"]

def add_content():
    global csvLocs, jsonLocบ

    heading = "TMF634 Resource Resource Catalog - Resource Specification"
    content = '''***Description:***
Resource specification is the service that is used to create blueprints based on which the resources will get created and instantiated. This service allows defining the variables that will define the resources, the datatypes and the relationship between the resources and other resources and additional details of how they can be instantiated (by external downstream APIs etc.).

***URL:*** /tmf-api/resourceCatalog/v4/resourceSpecification
***Supported methods:*** GET List, GET by ID, POST, PATCH, DELETE'''

    AddSection(heading, content, csvLocs,'')

    for i, jsonLoc in enumerate(jsonLocs):
        if jsonList[i] in ["GET List", "GET by id"]:
            print(jsonList[i])
            AddJsonSection(jsonList[i], None, jsonLoc)
        else:
            print(jsonList[i])
            AddJsonSection(jsonList[i], jsonLoc, None )
