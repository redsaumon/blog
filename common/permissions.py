from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print('obj: ', obj)
        print('request.user: ', request.user)
        print('obj.user: ', obj.user)

        if request.method in SAFE_METHODS:
            return True
        return obj.user == reuqest.user

# obj:  Post object (20)
# request.user:  test1
# obj.user:  test1
#
# obj:  {'post': <Post: Post object (20)>, 'prevPost': <Post: Post object (19)>, 'nextPost': <Post: Post object (21)>, 'commentList': <QuerySet []>}
# request.user:  test1
# print('obj.user: ', obj.user) AttributeError: 'dict' object has no attribute 'user'
