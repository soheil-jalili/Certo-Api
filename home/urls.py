from django.urls import path

from home.views import HomeView, CommentView, SocialView, InsightDetail, AllInsights, RemoveInsight, UpdateInsight, \
    AddInsight

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Comments URL
    path('comment/add', CommentView.as_view(), name='comment_add'),
    path('comment/remove/<int:pk>', CommentView.as_view(), name='comment_remove'),

    path('social/update/<int:pk>', SocialView.as_view(), name='social_update'),

    # Insights URLS
    path('insights', AllInsights.as_view(), name='all_insights'),
    path('insight/<slug:slug>', InsightDetail.as_view(), name='insights_detail'),
    path('insight/add', AddInsight.as_view(), name='add_insights'),
    path('insight/update/<int:id>', UpdateInsight.as_view(), name='update_insights'),
    path('insight/remove/<int:id>', RemoveInsight.as_view(), name='remove_insights'),

]
