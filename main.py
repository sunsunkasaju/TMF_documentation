from create_doc import *
import service_catalog.service_catalog as service_catalog
import service_catalog.service_category as service_category
import service_catalog.service_candidate as service_candidate


service_catalog.add_content()
service_category.add_content()
service_candidate.add_content()


doc.save('doc1.docx')




