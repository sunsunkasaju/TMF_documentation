from common import *
from common_config import *
from service_catalog.service_catalog import ServiceCatalog
from service_catalog.service_category import ServiceCategory
from service_catalog.service_candidate import ServiceCandidate


catalog_file_path = f"{root_dir}\service_catalog\config\service_catalog_config.json"
category_file_path = f"{root_dir}\service_catalog\config\service_category_config.json"
candidate_file_path = f"{root_dir}\service_catalog\config\service_candidate_config.json"

service_catalog = ServiceCatalog(catalog_file_path)
service_category = ServiceCategory(category_file_path)
service_candidate = ServiceCandidate(candidate_file_path)

service_catalog.add_content()
service_category.add_content()
service_candidate.add_content()

doc.save('doc1.docx')




