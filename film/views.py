from django.shortcuts import render, redirect
from film.models import FilmModel, CommentModel, LikeModel, ViewsCountModel
from django.http import Http404
from django.db.models import Q
from django.views.generic import View
# Create your views here.

# def index(request):
#     a, b = 10, 20
#     context = {
#         "cem":a+b,
#         "ferq":a-b,
#         "hasil":a*b,
#         "nisbet":a / b
#     }
#     return render(request, "index.html", context)


# def detail(request):
#     a, b = 20, 50
#     text = {
#         "cem":a+b,
#         "ferq":a-b,
#         "hasil":a*b,
#         "nisbet":a / b
#     }
#     return render(request, "detail.html", text)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        films = FilmModel.objects.all()
        query = request.GET.get("film")
        context = {}
        if query:
            films = films.filter(
                Q(name__contains=query) | Q(about__contains=query)
                )
            abouts = []
            for film in films:
                abouts.append(film.about)

            Abouts = []
            for about in abouts:
                About = about.replace(query, "<span style='background-color:yellow;'>" + query +"</span>")
                Abouts.append(About)
            context["Abouts"] = Abouts

        context["films"] = films
        context["query"] = query
        return render(request, "index.html", context)


# def index(request):
#     films = FilmModel.objects.all()
#     query = request.GET.get("film")
#     context = {}
#     if query:
#         films = films.filter(
#             Q(name__contains=query) | Q(about__contains=query)
#             )
#         abouts = []
#         for film in films:
#             abouts.append(film.about)

#         Abouts = []
#         for about in abouts:
#             About = about.replace(query, "<span style='background-color:yellow;'>" + query +"</span>")
#             Abouts.append(About)
#         context["Abouts"] = Abouts

#     context["films"] = films
#     context["query"] = query
#     return render(request, "index.html", context)

class DetailView(View):
    def get(self, request,id,  *args, **kwargs):
        film = FilmModel.objects.get(id=id)
        context = {
            "film": film,
        }
        if request.user.is_authenticated:
            if not ViewsCountModel.objects.filter(user=request.user, film=film).exists():
                ViewsCountModel.objects.create(
                    user = request.user,
                    film = film
                )
        return render(request,"detail.html", context)
    
    def post(self, request,id, *args, **kwargs):
        if request.method == "POST":
            choice = request.POST.get("choice")
            
            if choice == "comment":
                film_id = request.POST.get("film_id")
                film = FilmModel.objects.get(id=film_id)
                content = request.POST.get("content")

                CommentModel.objects.create(
                    user = request.user,
                    film = film,
                    content = content
                )


            elif choice == "like":
                film_id = request.POST.get("film_id")
                film = FilmModel.objects.get(id=film_id)


                if not LikeModel.objects.filter(user=request.user, film=film).exists():
                    LikeModel.objects.create(
                        user = request.user,
                        film = film
                    )
                else:
                    like = LikeModel.objects.get(user=request.user, film=film)
                    like.delete()

            return redirect("detail", id=id)




# def detail(request, id):
#     film = FilmModel.objects.get(id=id)
#     context = {
#         "film": film,
#     }
#     if request.user.is_authenticated:
#         if not ViewsCountModel.objects.filter(user=request.user, film=film).exists():
#             ViewsCountModel.objects.create(
#                 user = request.user,
#                 film = film
#             )
#     if request.method == "POST":
#         choice = request.POST.get("choice")
        
#         if choice == "comment":
#             film_id = request.POST.get("film_id")
#             film = FilmModel.objects.get(id=film_id)
#             content = request.POST.get("content")

#             CommentModel.objects.create(
#                 user = request.user,
#                 film = film,
#                 content = content
#             )


#         elif choice == "like":
#             film_id = request.POST.get("film_id")
#             film = FilmModel.objects.get(id=film_id)


#             if not LikeModel.objects.filter(user=request.user, film=film).exists():
#                 LikeModel.objects.create(
#                     user = request.user,
#                     film = film
#                 )
#             else:
#                 like = LikeModel.objects.get(user=request.user, film=film)
#                 like.delete()

#         return redirect("detail", id=id)
#     return render(request,"detail.html", context)

class LikedFilmsView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404
        likes = LikeModel.objects.filter(
            user = request.user
        )
        films = []
        for like in likes:
            films.append(like.film)
        d_films = []
        for film in films:
            if film not in d_films:
                d_films.append(film)
        
        context = {
            "d_films": d_films,
        }
        return render(request, "like.html", context)




# def liked_films(request):
#     if not request.user.is_authenticated:
#         raise Http404
#     likes = LikeModel.objects.filter(
#         user = request.user
#     )
#     films = []
#     for like in likes:
#         films.append(like.film)
#     d_films = []
#     for film in films:
#         if film not in d_films:
#             d_films.append(film)
    
#     context = {
#         "d_films": d_films,
#     }
#     return render(request, "like.html", context)

class CommesFilmsView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404
        comments = CommentModel.objects.filter(
            user = request.user
        )
        films = []
        for comment in comments:
            films.append(comment.film)

        d_films = []
        for film in films:
            if film not in d_films:
                d_films.append(film)
        
        context = {
            "d_films": d_films,
        }

        return render(request, "comment.html", context)


# def comment_films(request):
#     if not request.user.is_authenticated:
#         raise Http404
#     comments = CommentModel.objects.filter(
#         user = request.user
#     )

#     # films = [comment.film for comment in comments]
#     films = []
#     for comment in comments:
#         films.append(comment.film)

#     d_films = []
#     for film in films:
#         if film not in d_films:
#             d_films.append(film)
    
#     context = {
#         "d_films": d_films,
#     }

#     return render(request, "comment.html", context)


class ViewsCountView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404
        viewscount = ViewsCountModel.objects.filter(
            user = request.user
        )
        films = []
        for views_count in viewscount:
            films.append(views_count.film)
        d_films = []
        for film in films:
            if film not in d_films:
                d_films.append(film)
        
        context = {
            "d_films": d_films,
        }
        
        return render(request, "viewscount.html", context)


# def views_count(request):
#     if not request.user.is_authenticated:
#         raise Http404
#     viewscount = ViewsCountModel.objects.filter(
#         user = request.user
#     )
#     films = []
#     for views_count in viewscount:
#         films.append(views_count.film)
#     d_films = []
#     for film in films:
#         if film not in d_films:
#             d_films.append(film)
    
#     context = {
#         "d_films": d_films,
#     }
    
#     return render(request, "viewscount.html", context)