from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

class UserIsObjectOwnerMixin:
    """
    A mixin that checks if the current user is the owner of the object.
    Raises PermissionDenied if the user is not the owner.
    """
    def dispatch(self, request, *args, **kwargs):
        obj = get_object_or_404(self.get_queryset(), pk=kwargs['pk'])
        if obj.owner != request.user:
            raise PermissionDenied("You do not have permission to edit or delete this object.")
        return super().dispatch(request, *args, **kwargs)