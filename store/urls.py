from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('list/', list_item, name='list'),
    path('add/', add_items, name='add'),
    path('<int:id>/update/', update_items, name='update'),
    path('<int:pk>/detail/', StockDetailView.as_view(), name='detail'),
    path("<int:pk>/delete/", StockDeleteView.as_view(), name="delete"),
    path("<int:pk>/issue/", issue_items, name="issue"),
    path("<int:pk>/recieve/", recieve_items, name="recieve"),
    path("<int:pk>/reorder/", reorder_level, name="reorder"),
    path("history/", list_history, name="history"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    