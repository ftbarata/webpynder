from django.shortcuts import render
from .models import User as UserDb
from .engine import session


def save_photo_list_into_db(photo_list_string, user_id):
    p_list = convert_str_to_list(photo_list_string)
    db = UserDb(photo_list=p_list, user_id=user_id)
    db.save()


def convert_str_to_list(photo_list_string):
    p_list = []
    word = ''
    for char in photo_list_string:
        if char != ',':
            word = word + char.replace('[', '').replace('\'', '').replace(']', '')
        else:
            p_list.append(word)
            word = ''
    return p_list


def get_photo_list_from_db(user_id):
    s = UserDb.objects.all().filter(user_id=user_id).values('photo_list')
    p_list = convert_str_to_list(s[0]['photo_list'])
    UserDb.objects.all().delete()
    return p_list


class Control:
    @staticmethod
    def get_new_user():
        users = session.nearby_users()
        for i in users:
            Control.user = i
            break


def burst_like(request):
    users = session.nearby_users()
    try:
        for i in users:
            print(i.like())
            print(session.likes_remaining)
    except KeyError:
        pass
    return render(request, 'core/base.html')


def MainView(request):
    template_name = 'core/main.html'
    Control.get_new_user()
    user = Control.user
    try:
        profile_photo = ''
        for p in user.photos:
            profile_photo = p
            break
        save_photo_list_into_db(str(user.photos), user.id)
        return render(request, template_name,{'name':user.name, 'age':user.age, 'bio':user.bio, 'profile_photo':profile_photo, 'user_id':user.id})
    except KeyError:
        pass


def DetailView(request, user_id):
    template_name = 'core/details.html'
    uid = user_id
    photo_list = get_photo_list_from_db(uid)
    context = {'photo_list': photo_list,'user_id':uid}
    return render(request,template_name,context)


def LikeView(request, user_id):
    template_name = 'core/main.html'
    likes_count = session.likes_remaining
    if likes_count > 0:
        curr_user = Control.user
        like = curr_user.like()
        Control.get_new_user()
        user = Control.user
    else:
        like = False
        user = Control.user
    try:
        profile_photo = ''
        for p in user.photos:
            profile_photo = p
            break
        save_photo_list_into_db(str(user.photos), user.id)
        if like:
            return render(request, template_name,{'name':user.name, 'age':user.age, 'bio':user.bio, 'profile_photo':profile_photo, 'user_id':user.id, 'match_message': 'Match com {} !'.format(user.name)})
        else:
            if likes_count == 0:
                return render(request, template_name,{'name': user.name, 'age': user.age, 'bio': user.bio, 'profile_photo': profile_photo,'user_id': user.id, 'likes_out': 'True'})
            else:
                return render(request, template_name,{'name': user.name, 'age': user.age, 'bio': user.bio, 'profile_photo': profile_photo,'user_id': user.id})
    except KeyError:
        pass

def super_like_view(request, user_id):
    template_name = 'core/main.html'
    likes_count = session.likes_remaining
    if likes_count > 0:
        curr_user = Control.user
        print(curr_user.superlike())
        like = curr_user.like()
        Control.get_new_user()
        user = Control.user
    else:
        like = False
        user = Control.user
    try:
        profile_photo = ''
        for p in user.photos:
            profile_photo = p
            break
        save_photo_list_into_db(str(user.photos), user.id)
        if like:
            return render(request, template_name,{'name':user.name, 'age':user.age, 'bio':user.bio, 'profile_photo':profile_photo, 'user_id':user.id, 'match_message': 'Match com {} !'.format(user.name)})
        else:
            if likes_count == 0:
                return render(request, template_name,{'name': user.name, 'age': user.age, 'bio': user.bio, 'profile_photo': profile_photo,'user_id': user.id, 'likes_out': 'True'})
            else:
                return render(request, template_name,{'name': user.name, 'age': user.age, 'bio': user.bio, 'profile_photo': profile_photo,'user_id': user.id})
    except KeyError:
        pass

def NopeView(request, user_id):
    template_name = 'core/main.html'
    curr_user = Control.user
    print('Dislike em {} - {}'.format(curr_user.id, curr_user.name))
    print(curr_user.dislike())
    Control.get_new_user()
    user = Control.user
    try:
        profile_photo = ''
        for p in user.photos:
            profile_photo = p
            break
        save_photo_list_into_db(str(user.photos), user.id)
        return render(request, template_name,{'name':user.name, 'age':user.age, 'bio':user.bio, 'profile_photo':profile_photo, 'user_id':user.id})
    except KeyError:
        pass