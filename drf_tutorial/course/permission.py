from rest_framework import permissions

class IsOwnerReadOnly(permissions.BasePermission):
    """ 自定义权限： only owner can crud"""

    def has_object_permission(self, request, view, obj):
        """
        所有的req都允许read, thus allow GET/HEAD/OPTIONS
        :param request:
        :param view:
        :param obj:
        :return: bool
        """
        if request.method in ("GET","HEAD", "OPTIONS"):
            return True
        else:
            return request.user == obj.teacher


