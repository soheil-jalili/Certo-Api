from django.contrib import admin

from home.models import HomeCommentModel, HomeHeaderModel, Badge, Insights, SocialModel, ApplicationLinks, \
    FreedomBackModel

admin.site.register(HomeHeaderModel)
admin.site.register(HomeCommentModel)
admin.site.register(Badge)
admin.site.register(Insights)
admin.site.register(SocialModel)
admin.site.register(ApplicationLinks)
admin.site.register(FreedomBackModel)
