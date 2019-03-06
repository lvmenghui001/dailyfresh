from django.http import HttpResponseRedirect
# 如果没登录转到登录页面

def login(func):
    def login_fun(request,*args,**kwargs):
        if request.session.has_key("user_id"):
            return func(request,*args,**kwargs)
        else:
            ret = HttpResponseRedirect("/user/login/")
            ret.set_cookie("url",request.get_full_path())
            return ret
    return login_fun