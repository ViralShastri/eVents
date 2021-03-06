from django.urls import path
from . import views

urlpatterns = [
    path('admin/club-approval/', views.club_approval, name='club-approval'),
    path('admin/club-member-approval/', views.club_member_approval, name='club-member-approval'),
    path('admin/club/add/', views.club_add, name='club-add'),
    path('admin/club/', views.club_table, name='club-table'),
    path('admin/club/delete/',
         views.club_delete, name='club-delete'),
    path('admin/club/edit/<str:name>/', views.club_edit, name='club-edit'),
    path('admin/club/view/<str:name>/', views.club_view, name='club-view'),
    path('admin/club/updateactive/<str:name>/',
         views.club_update_active, name='club-update-active'),
    path('admin/club/updatenotactive/<str:name>/',
         views.club_update_notactive, name='club-update-notactive'),
    path('admin/club/updateaprrove/<str:name>/',
         views.club_update_approval_yes, name='club-update-approval-yes'),
    path('admin/club/updatenotapprove/<str:name>/',
         views.club_update_approval_no, name='club-update-approval-no'),
    path('admin/clubmember/add/', views.clubmember_add, name='clubmember-add'),
    path('clubadmin/clubmember/', views.clubmember_table, name='clubmember-table'),
    path('admin/clubmember/view/<int:id>/',
         views.clubmember_view, name='clubmember-view'),
    path('admin/clubmember/edit/<int:id>/',
         views.clubmember_edit, name='clubmember-edit'),
    path('admin/clubmember/delete/',
         views.clubmember_delete, name='clubmember-delete'),
    path('club-check/',
         views.club_exists, name='club-check'),
]
