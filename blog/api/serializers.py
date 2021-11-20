from rest_framework import serializers

from blog.models import Post

# Base Serializer oluşturulacak.


class PostSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="blog:detail_post", lookup_field="pk")
    # username = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "description",
            "slug",
            "image",
            "created_at",
            "updated_at",
            "is_active",
        ]

    # def get_author(self, obj):
    #     # print(obj)
    #     return str(obj.user.username)


class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "content", "is_active"]


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "image", "is_active", "created_at", "updated_at"]
