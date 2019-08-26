from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as pharmacy_views

app_name = 'pharmacy'
urlpatterns = [

	path('',pharmacy_views.scanBarcode, name='scanBarcode'),
	path('Dashboard/',pharmacy_views.dashboard,name='dasboard'),
    path('pharmacy_patient/<slug:code>',pharmacy_views.pharmacy_patient,name='patient'),
    # path('pharmacy_prescription/<slug:code>/int:id',pharmacy_views.pharmacy_patient,name='prescription'),
    path('drugs/<slug:code>',pharmacy_views.drugs,name='drugs'),
	path('add_drugs/',pharmacy_views.add_drugs,name="add_drugs"),
	path('add_drugsC/',pharmacy_views.add_drugsCa,name="add_drugsC"),
	path('add_drugsSupplier/',pharmacy_views.add_drugsSupplier,name="add_drugsS"),
	path('add_drugs_payment/<slug:code>/<int:id>',pharmacy_views.confirm_drug_payment,name="add_drugs_payment"),
	path('invoice/<slug:code>',pharmacy_views.invoice,name="invoice"),
	path('drugList/',pharmacy_views.drugsList,name="drugsList"),
	path('CategoryList/',pharmacy_views.categoryList,name="categoryList"),
	path('SuppliersList/',pharmacy_views.suppliersList,name="suppliersList"),
	path('pdf/<slug:code>', pharmacy_views.invoToPdf,name="pdf"),
	path('deleteCategory/<int:id>',pharmacy_views.deleteCategory,name="DeleteCategory"),
	path('deleteDrug/<int:id>',pharmacy_views.deleteDrug,name="DeleteDrug"),
	path('editCategory/<int:id>',pharmacy_views.editCategory,name="editCategory"),
	path('editSupplier/<int:id>',pharmacy_views.editSupplier,name="editSupplier"),
	path('editDrugs/<int:id>',pharmacy_views.editDrugs,name="editDrugs"),
	path('OutOfStock/',pharmacy_views.outofstock,name="OutOfStock"),
	path('Expired/',pharmacy_views.expiredDrugs,name="ExpiredDrugs"),
	path('load/<int:id>',pharmacy_views.loadStock,name="loadDrug"),

    ]
