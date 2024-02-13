{
     'name': 'hms',
     'author': 'Khaled ElGabry',
     'description':"Patient System",
     # 'website': "",
     # 'version': "",
     'depends': ['base'],
     
     
     'data': ['views/patients_views.xml',
              'views/departments_views.xml',
              'views/doctors_views.xml',
              'views/customers_views.xml',
              'views/groups_views.xml',
              'security/ir.model.access.csv',
              'reports/hms_report_template.xml',
              'reports/report.xml', 
              
              ],

     
}