# recetas/permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado que permite a los usuarios editar o eliminar sus propios objetos,
    pero solo permite lectura a otros usuarios.
    """
    def has_object_permission(self, request, view, obj):
        # Los métodos seguros (GET, HEAD, OPTIONS) están permitidos para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        # Para métodos no seguros (POST, PUT, DELETE), el usuario debe ser el propietario
        return obj.usuario == request.user