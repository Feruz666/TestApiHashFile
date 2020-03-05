from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
import json
import hashlib

from .models import Files
from .serializers import FileSerializer




def index(self, request):
    response = json.dump([{}])
    return HttpResponse(response, content_type='text/json')

def get_file(request, file_name):
    if request.method == 'GET':
        try:
            file = Files.objects.get(name=file_name)
            response = json.dumps([{'File': file.name, 'code_md5': file.code_md5, 'code_sha256': file.code_sha256}])
        except:
            response = json.dumps([{'Error': 'no file with that name'}])
    return HttpResponse(response, content_type='text/json')


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


class FileView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request):
        file_obj = request.data['file']
        lines = file_obj.readlines()
       

        # content = file_obj.read()
        str1 = ""
        for item in lines:
            str1 += str(item, 'utf-8')


        md_5 = hashlib.md5(str1.encode()).hexdigest()
        sha_256 = hashlib.sha256(str1.encode()).hexdigest()

        new_file = Files(name=file_obj.name, code_md5=md_5, code_sha256=sha_256)

        # print(file_obj.read())
        # print(file_obj.name)
        # if file_obj:
        #     return Response({"Message": "its ok"}, status = 200)
        # else:
        #     return Response({"Message": "file missing"}, status = 400)

        try:
            new_file.save()
            response = json.dumps([{'Success': 'File added'}])
        except:
            response = json.dumps([{'Error': 'File could not be added'}])
        return HttpResponse(response, content_type='text/json')

# @csrf_exempt
# def add_file(request):
#     if request.method == "POST":
#         uploaded_file = request.FILES['document']

#         content = uploaded_file.read()
#         str_content = content.decode("utf-8")

#         md_5 = hashlib.md5(str_content.encode()).hexdigest()
#         sha_256 = hashlib.sha256(str_content.encode()).hexdigest()
#         new_file = Files(name=uploaded_file.name, code_md5=md_5, code_sha256=sha_256)
#         try:
#             new_file.save()
#             response = json.dumps([{'Success': 'File added'}])
#         except:
#             response = json.dumps([{'Error': 'File could not be added'}])
#     return render(request, 'index.html')
    #return HttpResponse(response, content_type='text/json')

    #     payload = json.loads(request.body)
    #     f = open(payload['docfile'], 'r')
    #     if f.mode == "r":
    #         content = f.read()

    #         md_5 = hashlib.md5(content.encode()).hexdigest()
    #         sha_256 = hashlib.sha256(content.encode()).hexdigest()

    #         new_file = Files(name=f.name, docfile=f, code_md5=md_5, code_sha256=sha_256)
    #         try:
    #             new_file.save()
    #             response = json.dumps([{'Success': 'File added'}])
    #         except:
    #             response = json.dumps([{'Error': 'File could not be added'}])
    # return HttpResponse(response, content_type='text/json')




# text = "slonsukatvar"
# result = hashlib.md5(text.encode())

# result2 = hashlib.sha256(text.encode())

# print(result.hexdigest())
# print(result2.hexdigest())



