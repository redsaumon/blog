from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(111231231231231231231231)
        if request.method in SAFE_METHODS:
            return True
        print('====',obj['post'].user)
        print(request.user)

        return obj.user == request.user

    # dir(request.user)
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    #  '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__',
    #  '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
    #  '__str__', '__subclasshook__', '__weakref__', '_groups', '_user_permissions', 'check_password', 'delete',
    #  'get_all_permissions', 'get_group_permissions', 'get_user_permissions', 'get_username', 'groups',
    #  'has_module_perms', 'has_perm', 'has_perms', 'id', 'is_active', 'is_anonymous', 'is_authenticated', 'is_staff',
    #  'is_superuser', 'pk', 'save', 'set_password', 'user_permissions', 'username']
