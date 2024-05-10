from django.urls import path

from .views import worldNations, worldnation_details, worldnation_create, del_nation_col, worldnation_edit


urlpatterns = [
    path('del/<int:pk>/', del_nation_col, name='delete_nation'),
    path('<int:pk>/', worldnation_details, name='nation_info'),
    path('edit/<int:pk>/', worldnation_edit, name='nation_edit'),
    path('', worldNations, name='worldNation'),
    # path('', worldnation_create, name='add_nation'),
]
