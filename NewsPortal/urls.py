from django.urls import path, include
from .views import PostList, Event, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, profile, CategoryListView, subscribe,\
   unsubscribe, upgrade_me
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page


urlpatterns = [
   path('', cache_page(60)(PostList.as_view()), name='post_list'),
   path('<int:pk>', Event.as_view(), name='post_detail'),
   path('search/', NewsSearch.as_view(), name='post_search'),
   path('create/', NewsCreate.as_view(), name='post_create'),
   path('upgrade/', upgrade_me, name='upgrade'),
   path('profile/', profile, name='profile'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
   path('articles/create/', NewsCreate.as_view(), name='post_create'),
   path('articles/<int:pk>/edit/', login_required(NewsUpdate.as_view()), name='post_update'),
   path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
   path('profile/', profile, name='profile'),
   path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]