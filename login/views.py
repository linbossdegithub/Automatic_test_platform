# coding=utf-8
# login/views.py
from django.shortcuts import render,redirect
from . import models
from .forms import UserForm,RegisterForm,BlogForm
import hashlib 
from django.conf import settings
from django.http import HttpResponse
from django.core.paginator import Paginator
from models import PicTest,GoodsInfo
import markdown
import os
from django.http import StreamingHttpResponse
from django.http import FileResponse
def auto_test(request):
    os.chdir("C:\\Users\\Administrator\\Desktop\\django\\mysite_login\\static\\Auto_Test\\src")
    os.system("python all_test.py 2")
    os.chdir("C:\\Users\\Administrator\\Desktop\\django\\mysite_login\\login\\templates\\login")
    file_dir = 'result'
    file_dict = {}
    lists = os.listdir(file_dir) #先获取文件夹内的所有文件
    print lists
    for i in lists: # 遍历所有文件

        ctime = os.stat(os.path.join(file_dir, i)).st_ctime
        file_dict[ctime] = i # 添加创建时间和文件名到字典
    max_ctime = max(file_dict.keys()) # 取值最大的时间
    result = 'login/result/'+file_dict[max_ctime]
    print result
    return render(request,result)


    return HttpResponse('OK')
def auto_testshow(request):
    pass
    return render(request,'login/auto_test.html')
def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()
def blog(request):
    if request.method == "POST":
        f = BlogForm(request.POST)
        #blog_id = request.POST.get('blog_id',None)
        if f.is_valid():                                #判断验证如果通过            
            blog_id = f.cleaned_data
            blog_id = int(blog_id.get('blog_id'))
            blogtext = models.GoodsInfo.objects.get(id=blog_id)
            hcontent = blogtext.gcontent
            return render(request,'login/blog.html', {'html':hcontent})        
        else:                                           #如果没通过
            print(f.errors)
            return render(request,'login/blog.html', {'html':"请输入正确ID"})

        #hcontent = blogtext
        #hcontent=markdown.markdown(hcontent)
    #blog_form = BlogForm()
    #return render(request,'login/blog.html', {'html':hcontent})

def blogshow(request):

    pass
    return render(request,'login/blogshow.html')
 
def index(request):
   # response = HttpResponse("读取Cookie，数据如下：<br>")
    #if request.COOKIES.has_key('h1'):
    #    response.write('<h1>' + request.COOKIES['h1'] + '</h1>')
   # return response
    pass
    return render(request,'login/editor.html')
    

#上传图片功能
#def pic_handle(request):
 #   f1=request.FILES.get('pic')
  #  fname='%s/login/%s'%(settings.MEDIA_ROOT,f1.name)
   # with open(fname,'w') as pic:
    #    for c in f1.chunks():
     #       pic.write(c)
def baidumap(request):
    pass
    return render(request,'login/baidumap.html')

def download_fileshow(request):
    pass
    return render(request,'login/download_file.html')

def download_file(request):   
    file=open('F://user.xls','rb')
    response =StreamingHttpResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="user.xls"'
    return response
def jietu(request):
    if request.method == "POST":
        print 'dsdfe'
        dict = request.POST

        tupian = dict.get('snapData')
        print 'dsv'
        print tupian
    return  HttpResponse("upload over!")

def upload(request):
    myFile =request.FILES.get("snapData", None)    # 获取上传的文件，如果没有文件，则默认为None  
    if not myFile:

        return HttpResponse("no files for upload!")

    destination = open(os.path.join("G:\\upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作  
    for chunk in myFile.chunks():      # 分块写入文件  
        destination.write(chunk)  
    destination.close()  
    return HttpResponse("upload over!") 

def do_add(request):

    hcontent = request.POST.get('hcontent')
    gcontent = GoodsInfo()
    gcontent.gcontent = hcontent
    gcontent.save()
    hcontent=markdown.markdown(hcontent)
    return render(request, 'login/show.html', {'html':hcontent})


def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name

                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())
 
    login_form = UserForm()
    return render(request, 'login/login.html', locals())
def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())
 
                # 当一切都OK的情况下，创建新用户
 
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    return redirect('/index/')

