<<<<<<< HEAD
简介: 用django搭建了一个简易的web平台，来集成自动化测试，适合初学者使用

运行环境 linux python2.7 
1、修改数据库配置 vim mysite_login/settings.py
=======
绠�浠�: 鐢╠jango鎼缓浜嗕竴涓畝鏄撶殑web骞冲彴锛屾潵闆嗘垚鑷姩鍖栨祴璇曪紝閫傚悎鍒濆鑰呬娇鐢�

杩愯鐜 linux python2.7 
1銆佷慨鏀规暟鎹簱閰嶇疆 vim mysite_login/settings.py
>>>>>>> c52bcca61ba4391bc3d1805c549fffdf574adc4e

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_login',        
        'USER': 'root',          
        'PASSWORD': 'youpasswd',      #you mysql passwd
        'HOST': 'xxx',    #you mysql server ip
        'PORT': '3306',                   #
        }
<<<<<<< HEAD
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
=======
2銆乸ip install django 
3銆乸ip install django-simple-captcha
4銆乸ip install django-tinymce==2.4.0
5銆乸ip install django-pure-pagination
6銆乸ip install django-contrib-comments
7銆乸ip install fields
8銆丏jango 1.11鍏煎鎬ч棶棰�-鏃犳硶瀵煎叆鍚嶇ОFlatatt  瑙ｅ喅锛氫慨鏀规簮鐮�  鎶ラ敊鐨勯偅涓�琛屽鍏ユ敼涓�:from django.forms.utils import flatatt 
9銆佹暟鎹簱 mysite_login 闇�瑕佷负utf-8 
 鎴栬�咃細alter database mysite_login character set utf8;
10銆乸ip install pymysql
11銆乸ython manage.py makemigrations     
12銆乸ython manage.py migrate
13銆佽繍琛�
 python mange.py runserver 0.0.0.0:8000  
14銆佽闂�
 http://ip:8000/index/
>>>>>>> c52bcca61ba4391bc3d1805c549fffdf574adc4e
