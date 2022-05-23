from rest_framework import serializers

from api.models import Post, Comment, Category, Tag


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializerSub(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'update_dt']


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        exclude = ['like']


class PostListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'like', 'category']


class PostRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        exclude = ['create_dt']


class PostSerializerSub(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class PostSerializerDetail(serializers.Serializer):
    post = PostRetrieveSerializer()
    prevPost = PostSerializerSub()
    nextPost = PostSerializerSub()
    commentList = CommentSerializerSub(many=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class CateTagSerializer(serializers.Serializer):
    cateList = serializers.ListField(child=serializers.CharField())
    tagList = serializers.ListField(child=serializers.CharField())