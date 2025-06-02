from django.urls import path

from home.views import HomeView, CommentView, SocialView, InsightDetail, AllInsights

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Comments URL
    path('comment/add', CommentView.as_view(), name='home'),
    path('comment/remove/<int:pk>', CommentView.as_view(), name='home'),
    path('social/update/<int:pk>', SocialView.as_view(), name='home'),

    path('insights', AllInsights.as_view(), name='all_insights'),
    path('insight/<slug:slug>', InsightDetail.as_view(), name='insights_detail'),

]
