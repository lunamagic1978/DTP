from api.lib import  project_handle
from django.http import JsonResponse
from api.lib.error import Create_Error

def projects(request, namespace):
    if request.method == "GET":
        list_projects = project_handle.get_projects(namespace)
        return JsonResponse({"msg":"success",
                             "code": 200,
                             "data": list_projects})
    else:
        return JsonResponse({"msg": "请求方式不正确",
                             "code": 500})

def project(request, namespace):
    if request.method == "POST":
        try:
            project_handle.create_project(namespace, request.body)
        except Create_Error as e:
            return JsonResponse({"msg": "创建project失败: {}".format(e.msg),
                                 "code": e.code})
        return JsonResponse({"msg": "创建project成功",
                             "code": 200})
    else:
        return JsonResponse({"msg": "请求方式不正确",
                             "code": 500})