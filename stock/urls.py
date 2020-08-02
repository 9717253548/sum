from django.urls import path
from . views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name=" home"),
    path('uplode/',stock_upload,name=" stock"),
    path('view/',view_stock,name='view stock')
]