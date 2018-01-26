"""定义learning_logs的URL模式"""

from django.conf.urls import url

from . import views

#指定app的名字，否则报错
app_name = 'learning_logs'


urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),

    #显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),

    #特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
    #正则表达式含义：/(?P<topic_id>\d+)/与包含在两个斜杠内的整数匹配，不管这个数字为多少位；
    # 将这个整数存储在一个名为topic_id的实参中，并传递给对应的视图函数

]