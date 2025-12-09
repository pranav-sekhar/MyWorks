from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm #for user reg process
from django.contrib.auth.forms import AuthenticationForm #for user login process
from django.contrib.auth import login 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required #req to view movie site
from . models import Category,Movie
from . forms import MovieForm
from . forms import ProfileEditForm

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) #form for user reg,auto provides fields for reg
        if form.is_valid():
            form.save() #save new user to db
            return redirect("reg_success") #goto reg success
    else:
        form = UserCreationForm() #else show empty reg form(GET)
    return render(request,"register.html",{"form":form})

def reg_success(request):
    return render(request,'reg_success.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST) #form to login,takes entered data
        if form.is_valid():
            user = form.get_user() #get user obj
            login(request,user) #logins the user
            return redirect("movie_list")
    else:
        form = AuthenticationForm() #else show empty login form(GET)
    return render(request,"login.html",{"form":form})

def logout_view(request):
    logout(request) #logouts the user
    return redirect("login")

@login_required
def movie_list(request):
    movies = Movie.objects.all() #get all movies from db
    categories = Category.objects.all() #get all categories from db
    #to search movie
    query = request.GET.get("q") #gets whatever user entered in searchbox,q is key of searchbox
    if query:  
        movies = movies.filter(title__icontains=query) #filter movies with that words in title
    #to categorize movie
    category_sel = request.GET.get('category') #gets category selected by user from dropdown(name given in models)
    if category_sel :
        movies = movies.filter(category_id=category_sel) #filter movies based on matching category id selected(category_id is id in db)
    return render(request,'movie_list.html',{"movies":movies,"categories":categories,"query":query,"category_sel":category_sel}) #pass these to html pg to show details

@login_required
def movie_detail(request,id):
    movie = get_object_or_404(Movie,id=id) #fetches movie with that id from db or shows error(id in db n id we gave)
    return render(request,"movie_detail.html",{"movie":movie})

@login_required
def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST,request.FILES) #create form obj to enter values(import MovieForm),request.FILES to upload imgs
        if form.is_valid():  #checks all fields filled crctly
            movie = form.save(commit=False) #create movie obj,commit false means dont add to db yet since we need to include added_by
            movie.added_by = request.user  #link with logged in user to show who added
            movie.save() #now save form to db
            return redirect('movie_list')
    else:
        form = MovieForm()  #else show empty form
    return render(request,'add_movie.html',{"form":form})

@login_required
def edit_movie(request,movieid):
    movie = get_object_or_404(Movie,id=movieid) #get movie with that id or error
    if movie.added_by != request.user:  #if movie not added by this user,redirect(only who added can edit)
        return redirect('movie_list') 
    if request.method == "POST":  #else owner can edit 
        form = MovieForm(request.POST,request.FILES,instance=movie) #form instance to update existing movie data instead of create
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie) #else show existing movie data(instance shows existing data prefilled)
    return render(request,'edit_movie.html',{"form":form, "movie":movie}) #pass movie also so that movie detail will show while edit

@login_required
def delete_movie(request,movieid):
    movie = get_object_or_404(Movie,id=movieid) 
    if movie.added_by != request.user: #if movie not added by this user,redirect
        return redirect('movie_list')
    if request.method == "POST": #else owner can delete
        movie.delete()  #delete movie
        return redirect('movie_list')
    return render(request,'delete_movie.html',{"movie":movie}) #pass movie to show movie detail when delete(no need to pass form since its delete process,form fields no need to show)

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = ProfileEditForm(request.POST,instance=request.user) #get from forms py to edit fields,instance to update existing userdata
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = ProfileEditForm(instance=request.user) #instance to show existing data
    return render(request,'edit_profile.html',{"form":form})



