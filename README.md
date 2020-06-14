简介: 用django搭建了一个简易的web平台，来集成自动化测试，适合初学者使用

运行环境 linux python2.7 
1、修改数据库配置 vim mysite_login/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_login',        
        'USER': 'root',          
        'PASSWORD': 'youpasswd',      #you mysql passwd
        'HOST': 'xxx',    #you mysql server ip
        'PORT': '3306',                   #
        }
2、pip install django 
3、pip install django-simple-captcha
4、pip install django-tinymce==2.4.0
5、pip install django-pure-pagination
6、pip install django-contrib-comments
7、pip install fields
8、Django 1.11兼容性问题-无法导入名称Flatatt  解决：修改源码  报错的那一行导入改为:from django.forms.utils import flatatt 
9、数据库 mysite_login 需要为utf-8 
 或者：alter database mysite_login character set utf8;
10、pip install pymysql
11、python manage.py makemigrations     
12、python manage.py migrate
13、运行
 python mange.py runserver 0.0.0.0:8000  
14、访问
 http://ip:8000/index/
