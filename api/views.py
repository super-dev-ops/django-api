from django.shortcuts import render
from api.models import Post
from api.serializers import PostSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json

def get_post_details(pk):
    try:
        post = Post.objects.get(id = pk)
        serializer = PostSerializer(post)
        json_data = JSONRenderer().render(serializer.data)
        return {"data": json_data, "response_code": 200}
    except ObjectDoesNotExist:
        print(f"Exception occured data not found for id {pk}")
        return {"caused_by": f"Post with id {pk} not found", "response_code": 404}
    except Exception as e:
        return {"caused_by": f"Error: Exception occured {e}", "response_code": 500}
    
# Model Object - Single post data - without pretty in JSON format
def post_detail(request,pk):
    response = get_post_details(pk)
    if response.get('response_code') == 200:
        return HttpResponse(response.get('data'), content_type='application/json', status = 200)
    else:
        return HttpResponse(response.get('caused_by','unknown error'), status=response.get('response_code'))


# Model Object - Single post data - JSON pretty format
def post_detail_pretty(request,pk):
    response = get_post_details(pk)
    if response.get('response_code') == 200:
        json_pretty = json.loads(response.get('data'))
        #return HttpResponse(json_pretty, content_type='application/json', status = 200)
        return JsonResponse(json_pretty, json_dumps_params={'indent': 2}, status=200)
    else:
        return HttpResponse(response.get('caused_by','unknown error'), status=response.get('response_code'))
    
def get_list_posts():
    try:
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return {"data": json_data, "response_code": 200}
    except ObjectDoesNotExist:
        print(f"Exception occured data not found for id {pk}")
        return {"caused_by": f"Post with id {pk} not found", "response_code": 404}
    except Exception as e:
        return {"caused_by": f"Error: Exception occured {e}", "response_code": 500}

def list_posts(request):
    response = get_list_posts()
    if response.get('response_code') == 200:
        return HttpResponse(response.get('data'), content_type='application/json', status = 200)
    else:
        return HttpResponse(response.get('caused_by','unknown error'), status=response.get('response_code'))
    
def list_posts_pretty(request):
    response = get_list_posts()
    if response.get('response_code') == 200:
        json_pretty = json.loads(response.get('data'))
        #return HttpResponse(json_pretty, content_type='application/json', status = 200)
        return JsonResponse(json_pretty, json_dumps_params={'indent': 2}, safe=False, status=200)
    else:
        return HttpResponse(response.get('caused_by','unknown error'), status=response.get('response_code'))
    