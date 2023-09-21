from functools import wraps
from django.http import HttpResponseForbidden

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Access denied.")
    return _wrapped_view

def dealer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_dealer:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Access denied.")
    return _wrapped_view

def agent_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_agent:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Access denied.")
    return _wrapped_view