from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    blog_image = serializers.ImageField()
    contents = serializers.CharField(source='content') #Takes source from content field but returns it with key contents
    created_on = serializers.DateTimeField()
    status = serializers.BooleanField()
    author_name = serializers.ReadOnlyField(source='author.username') #https://blog.logrocket.com/use-django-rest-framework-to-build-a-blog/
    published = serializers.BooleanField(source='status')