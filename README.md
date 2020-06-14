<<<<<<< HEAD
¼ò½é: ÓÃdjango´î½¨ÁËÒ»¸ö¼òÒ×µÄwebÆ½Ì¨£¬À´¼¯³É×Ô¶¯»¯²âÊÔ£¬ÊÊºÏ³õÑ§ÕßÊ¹ÓÃ

ÔËÐÐ»·¾³ linux python2.7 
1¡¢ÐÞ¸ÄÊý¾Ý¿âÅäÖÃ vim mysite_login/settings.py
=======
ç®€ä»‹: ç”¨djangoæ­å»ºäº†ä¸€ä¸ªç®€æ˜“çš„webå¹³å°ï¼Œæ¥é›†æˆè‡ªåŠ¨åŒ–æµ‹è¯•ï¼Œé€‚åˆåˆå­¦è€…ä½¿ç”¨

è¿è¡ŒçŽ¯å¢ƒ linux python2.7 
1ã€ä¿®æ”¹æ•°æ®åº“é…ç½® vim mysite_login/settings.py
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
2¡¢pip install django 
3¡¢pip install django-simple-captcha
4¡¢pip install django-tinymce==2.4.0
5¡¢pip install django-pure-pagination
6¡¢pip install django-contrib-comments
7¡¢pip install fields
8¡¢Django 1.11¼æÈÝÐÔÎÊÌâ-ÎÞ·¨µ¼ÈëÃû³ÆFlatatt  ½â¾ö£ºÐÞ¸ÄÔ´Âë  ±¨´íµÄÄÇÒ»ÐÐµ¼Èë¸ÄÎª:from django.forms.utils import flatatt 
9¡¢Êý¾Ý¿â mysite_login ÐèÒªÎªutf-8 
 »òÕß£ºalter database mysite_login character set utf8;
10¡¢pip install pymysql
11¡¢python manage.py makemigrations     
12¡¢python manage.py migrate
13¡¢ÔËÐÐ
 python mange.py runserver 0.0.0.0:8000  
14¡¢·ÃÎÊ
 http://ip:8000/index/
=======
2ã€pip install django 
3ã€pip install django-simple-captcha
4ã€pip install django-tinymce==2.4.0
5ã€pip install django-pure-pagination
6ã€pip install django-contrib-comments
7ã€pip install fields
8ã€Django 1.11å…¼å®¹æ€§é—®é¢˜-æ— æ³•å¯¼å…¥åç§°Flatatt  è§£å†³ï¼šä¿®æ”¹æºç   æŠ¥é”™çš„é‚£ä¸€è¡Œå¯¼å…¥æ”¹ä¸º:from django.forms.utils import flatatt 
9ã€æ•°æ®åº“ mysite_login éœ€è¦ä¸ºutf-8 
 æˆ–è€…ï¼šalter database mysite_login character set utf8;
10ã€pip install pymysql
11ã€python manage.py makemigrations     
12ã€python manage.py migrate
13ã€è¿è¡Œ
 python mange.py runserver 0.0.0.0:8000  
14ã€è®¿é—®
 http://ip:8000/index/
>>>>>>> c52bcca61ba4391bc3d1805c549fffdf574adc4e
