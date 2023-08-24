from create_doc import *
import service_catalog.service_catalog as service_catalog
import service_catalog.service_category as service_category
import service_catalog.service_candidate as service_candidate
import resource_catalog.resource_catalog as resource_catalog
import resource_catalog.resource_candidate as resource_candidate
import resource_catalog.resource_category as resource_category
import resource_catalog.resource_specification as resource_specification


service_catalog.add_content()
service_category.add_content()
service_candidate.add_content()
resource_catalog.add_content()
resource_candidate.add_content()
resource_category.add_content()
resource_specification.add_content()

doc.save('doc1.docx')




