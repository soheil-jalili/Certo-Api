from django.contrib import admin

from home.models import HomeCommentModel, HomeHeaderModel, Badge, InsightModel, SocialModel, ApplicationLinksModel, \
    FreedomBackModel

admin.site.register(HomeHeaderModel)
admin.site.register(HomeCommentModel)
admin.site.register(Badge)
admin.site.register(InsightModel)
admin.site.register(SocialModel)
admin.site.register(ApplicationLinksModel)
admin.site.register(FreedomBackModel)
