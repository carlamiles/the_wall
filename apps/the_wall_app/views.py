from django.shortcuts import render, HttpResponse, redirect
from apps.login_app_the_wall.models import User
from .models import Message, Comment
# Create your views here.
def index(request):
    all_messages = Message.objects.all()
    user = User.objects.get(id=request.session['new_user_id'])
    context = {
        'all_messages': all_messages,
        'user': user
    }
    return render(request, 'the_wall_app/index.html', context)

def post_message(request):
    print('*'*50, 'the post message method is running')
    this_user = User.objects.get(id=request.session['new_user_id'])
    new_message = Message.objects.create(message=request.POST['post_message'], user=this_user)
    return redirect('/wall')

def post_comment(request):
    print('*'*50, 'the post comment method is running')
    this_user = User.objects.get(id=request.session['new_user_id'])
    Comment.objects.create(comment=request.POST['post_comment'], user=this_user, message=Message.objects.get(id=request.POST['message_id_for_comment']))
    return redirect('/wall')

def delete_message(request):
    print('*'*50, 'the delete message method is running')
    this_user = User.objects.get(id=request.session['new_user_id'])
    message = request.POST['message_id_to_delete']
    message_to_delete = Message.objects.get(id=request.POST['message_id_to_delete'])
    message_to_delete.delete()
    return redirect('/wall')

# def like_post(request, id):
#     print('*'*50, 'the like button is running')
#     this_user = User.objects.get(id=request.session['new_user_id'])
#     message_to_like = Message.objects.get(id=request.POST['message_id_to_like'])
#     if message_to_like.mess_likes.filter(id=this_user.id).exists():
#         is_liked = True
#         message_to_like.mess_likes.remove(this_user)
#         print('*'*50, 'Like_post method: message already liked, dislike button displayed')
#     else:
#         is_liked =False
#         message_to_like.mess_likes.add(this_user)
#         print('*'*50, 'Like_post method: message not liked, like button displayed')
#     return redirect('/wall')

def like_mess(request, id):
    print('*'*50, 'the like message method is running!')
    this_message = Message.objects.get(id=id)
    this_user = User.objects.get(id=request.session['new_user_id'])
    this_message.mess_likes.add(this_user)
    return redirect('/wall')

def unlike_mess(request, id):
    print('*'*50, 'the unlike message method is running!')
    this_message = Message.objects.get(id=id)
    this_user = User.objects.get(id=request.session['new_user_id'])
    this_message.mess_likes.remove(this_user)
    return redirect('/wall')