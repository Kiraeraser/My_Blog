from django.urls import path

from .views import (blog_post_retrieve_view, 
                        blog_post_list_view,
                        blog_post_update_view,
                        blog_post_delete_view,
                    blog_post_like,
                    blog_post_dislike,
                  
                   )

urlpatterns = [
       
    #re_path(r'^blog/(?P<slug>\w+)/$',blog_post_detail_page),
    path('',blog_post_list_view),
    
    path('<str:slug>/',blog_post_retrieve_view), #dynamic URL
    path('<str:slug>/edit',blog_post_update_view),
    path('<str:slug>/delete',blog_post_delete_view),
    path('<str:slug>/likes',blog_post_like),
    path('<str:slug>/dislikes',blog_post_dislike),

    
    
]
