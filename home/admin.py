from django.contrib import admin
from home.models import registermodel,test,package,adminmodel,User,Patient_List

admin.site.register(registermodel)
admin.site.register(test)
admin.site.register(package)
admin.site.register(adminmodel)
admin.site.register(Patient_List)


