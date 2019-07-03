from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as pharmacy_views

app_name = 'pharmacy'
urlpatterns = [

	path('',pharmacy_views.scanBarcode, name='scanBarcode'),
    path('pharmacy_patient/<slug:code>',pharmacy_views.pharmacy_patient,name='patient'),
    # path('pharmacy_prescription/<slug:code>/int:id',pharmacy_views.pharmacy_patient,name='prescription'),
    path('drugs/<slug:code>',pharmacy_views.drugs,name='drugs'),
	path('add_drugs/',pharmacy_views.add_drugs,name="add_drugs"),
	path('add_drugs_payment/<slug:code>/<int:id>',pharmacy_views.confirm_drug_payment,name="add_drugs_payment"),
	path('invoice/<slug:code>',pharmacy_views.invoice,name="invoice"),
	path('drugList/',pharmacy_views.drugsList,name="drugsList"),
	path('pdf/<slug:code>', pharmacy_views.invoToPdf,name="pdf"), 

    ]
