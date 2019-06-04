from django.shortcuts import render
from django.http import JsonResponse
from api.models import *
from api.lib import namespace_handle
from api.lib.error import Create_Error



# Create your views here.

# 获取namespaces列表
def namespaces(request):
    if request.method == "GET":
        list_namespaces = namespace_handle.get_namespaces()
        print(list_namespaces)
        return JsonResponse({"msg":"success",
                             "code": 200,
                             "data": list_namespaces})
    else:
        return JsonResponse({"msg": "请求方式不正确",
                             "code": 500})

def namespace(request):
    #创建namespace
    if request.method == "POST":
        try:
           namespace_handle.create_namespace(request.body)
        except Create_Error as e:
            return JsonResponse({"msg": "创建namesapce失败: {}".format(e.msg),
                                 "code": e.code})
        return JsonResponse({"msg": "创建namesapce成功",
                             "code": 200})
    else:
        return JsonResponse({"msg": "请求方式不正确",
                             "code": 500})

