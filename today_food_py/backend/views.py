import hashlib
import random

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def test(request):
    return JsonResponse({'msg': '添加成功', 'code': 200}, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def get_cookie(request):
    print(request.GET.get('msg'))
    hashed_string = hashlib.md5('2243431891C15502593610C'.encode()).hexdigest()
    print(hashed_string)
    response = HttpResponse("Cookie has been set!")
    cookie_value = request.COOKIES.get('data')
    print(cookie_value)
    response.set_cookie('cookie_name', 'cookie_value', max_age=3600)  # 设置 cookie
    print(response)
    return response


@csrf_exempt
def home(request):
    data=request.body.decode('utf-8')
    column=eval(data)['params']['column']
    data1=[{1:[{ 'title': 'Div 1', 'content': '这是第一个div。' },
            { 'title': 'Div 2', 'content': '这是第二个div。' },
            { 'title': 'Div 3', 'content': '这是第三个div。' },
            { 'title': 'Div 4', 'content': '这是第四个div。' }],
        2:[{ 'title': 'Div 1', 'content': '这是第五个div。' },
            { 'title': 'Div 2', 'content': '这是第六个div。' },
            { 'title': 'Div 3', 'content': '这是第七个div。' },
            { 'title': 'Div 4', 'content': '这是第八个div。' }],

           3:[{'title': 'Div 1', 'content': '这是第9个div。'},
              {'title': 'Div 2', 'content': '这是第10个div。'},
              {'title': 'Div 3', 'content': '这是第11个div。'},
              {'title': 'Div 4', 'content': '这是第12个div。'}],
    4: [{'title': 'Div 1', 'content': '这是第13个div。'},
        {'title': 'Div 2', 'content': '这是第14个div。'},
        {'title': 'Div 3', 'content': '这是第15个div。'},
        {'title': 'Div 4', 'content': '这是第16个div。'}],
    5: [{'title': 'Div 1', 'content': '这是第17个div。'},
    {'title': 'Div 2', 'content': '这是第18个div。'},
    {'title': 'Div 3', 'content': '这是第19个div。'},
    {'title': 'Div 4', 'content': '这是第20个div。'}],
    },
       ]
    print(column)
    # 壬午 戊申 己未 丙淹
    # 水火土金木土火木
    return_data={column:data1[0][column]}
    print(return_data)
    return  JsonResponse(return_data,safe=False)