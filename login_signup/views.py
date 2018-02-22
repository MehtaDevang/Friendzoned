from django.shortcuts import render
from django.http import HttpResponse
from .models import OurUsers, Friend_Requests, Message, Post, Comment
import datetime
from django.contrib.auth.hashers import make_password


# Create your views here.


def login(request):

    return render(request, 'loginSignup.html')

def signup(request):

    return render(request, 'signup.html')

def homepage(request):
    global post_id
    post_id = 0
    alluser = OurUsers.objects.all()
    friend_requests = Friend_Requests.objects.all()
    messages = Message.objects.order_by('-message_time').all()
    posts = Post.objects.order_by('-post_time').all()
    comments = Comment.objects.order_by('-comment_time').all()
    if 'active_user' in request.session:
        active_user = request.session['active_user']
        user = OurUsers.objects.get(username = active_user)
    context = {
        'alluser' : alluser,
        'friend_requests' : friend_requests,
        'messages' : messages,
        'user' : user,
        'posts' : posts,
        'comments' : comments,
    }
    return render(request, 'homepage.html', context)

def add_user(request):
    name = request.POST['name']
    dob = request.POST['dob']
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if not OurUsers.objects.filter(username = username).exists():
        db = OurUsers()
        db.name = name
        db.dob = dob
        db.username = username
        if(password1 == password2):
            db.password = password1
        else:
            return HttpResponse("Passwords do not match")
        db.save()
        return render(request, 'loginSignup.html')

    else:
        return render(request, 'signup.html')

def check_login(request):
        username = request.POST['username']
        password = request.POST['password']

        if OurUsers.objects.get(username = username, password = password):
            user = OurUsers.objects.get(username = username)
            request.session['active_user'] = user.username
            return homepage(request)

        else:
            return HttpResponse("Problem with username or password...Unable to log you in")


def send_request(request):
    data = request.POST['button_data'].split("-")
    request_from = data[0]
    request_to = data[1]
    db = Friend_Requests()
    db.request_from = OurUsers.objects.get(username = request_from)
    db.request_to = request_to
    db.save()
    alluser = OurUsers.objects.all()
    friend_requests = Friend_Requests.objects.all()
    user = OurUsers.objects.filter(username = request_to)
    messages = Message.objects.all()
    context = {
        'alluser': alluser,
        'friend_requests': friend_requests,
        'user' : user,
        'messages' : messages,
    }
    return homepage(request)

def accept_request(request):
    data = request.POST['button_data'].split("-")
    request_from = data[0]
    request_to = data[1]

    user1 = OurUsers.objects.get(username = request_from)
    user2 = OurUsers.objects.get(username = request_to)

    user1.friends.add(request_to)
    user2.friends.add(request_from)
    user1.save()
    user2.save()

    obj = Friend_Requests.objects.get(request_to = request_to, request_from = request_from)
    obj.delete()

    alluser = OurUsers.objects.all()
    friend_requests = Friend_Requests.objects.all()
    user = OurUsers.objects.filter(username=request_to)
    messages = Message.objects.all()
    # context = {
    #     'alluser': alluser,
    #     'friend_requests': friend_requests,
    #     'user': user,
    #     'messages': messages,
    # }
    return homepage(request)


def send_message(request):
    message_to = request.POST['message_to']
    message = request.POST['message']
    data = request.POST['button_data']
    message_from = OurUsers.objects.get(username = data)
    db = Message()
    db.message_to = message_to
    db.message_from = message_from
    db.message = message
    db.message_time = datetime.datetime.now()
    db.save()
    return homepage(request)

def add_post(request):
    global post_id
    username = request.POST['button_submit']
    post_id = request.POST['post_id']
    posted_by = OurUsers.objects.get(username = username)
    post = request.POST['post']
    post_time = datetime.datetime.now()
    db = Post()
    db.post_id = post_id
    db.posted_by = posted_by
    db.post = post
    db.post_time = post_time
    db.save()
    return homepage(request)

def add_comment(request):
    comment = request.POST['comment']
    commented_by = request.POST['button_submit']
    comment_id = request.POST['comment_id']
    comment_time = datetime.datetime.now()
    db = Comment()
    db.comment_id = comment_id
    db.comment_by = commented_by
    db.comment = comment
    db.comment_time = comment_time
    db.save()
    return homepage(request)

def logout(request):
    active_user = 0
    logged_user = ''
    return render(request, 'loginSignup.html')