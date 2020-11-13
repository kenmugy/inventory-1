from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import home, list_item, add_items, update_items, StockDeleteView


urlpatterns = [
    path('', home, name='home'),
    path('list/', list_item, name='list'),
    path('add/', add_items, name='add'),
    path('<int:id>/update/', update_items, name='update'),
    path("<int:pk>/delete/", StockDeleteView.as_view(), name="delete")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    