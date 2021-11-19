from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='blog:detail_post',
        lookup_field='slug')
    # username = serializers.SerializerMethodField()
    class Meta:
       model = Post
       fields = [
           'author',
           'title',
           'description',
           'image',
           'url',
           'created_at',
           'updated_at',
           "is_active"
       ]

    # def get_author(self, obj):
    #     # print(obj)
    #     return str(obj.user.username)

       
  
class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'is_active'
        ] 
    


