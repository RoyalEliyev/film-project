from django.contrib import admin
from film.models import FilmModel,ActorModel,CommentModel,LikeModel,ViewsCountModel


# Register your models here.

@admin.register(FilmModel)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("name", "rating")
    list_display_links = ("name", "rating")
    # fields = ("name",)
    # exclude = ("name",)
    list_filter = ("pub_date",)
    search_fields = ("name",)
    readonly_fields = ("views_count",)



# admin.site.register(FilmModel, FilmAdmin)

@admin.register(ActorModel)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name","surname")
    list_display_links = ("name",)
    search_fields = ("name",)
    readonly_fields = ("name",)
    list_editable = ("surname",)
    


# admin.site.register(ActorModel)
admin.site.register(CommentModel)
admin.site.register(LikeModel)
admin.site.register(ViewsCountModel)