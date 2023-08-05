from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Permite ao usuário editar seu próprio profile
    """

    def has_object_permission(self, request, view, obj):
        """ Checa se o usuário esta tentando alterar o próprio profile.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
