import json

from django.contrib.auth.decorators import user_passes_test
from django.http.response import HttpResponse

# def group_required(*group_names):
#     """Requires user membership in at least one of the groups passed in."""
#     def in_groups(u):
#         if u.is_authenticated:
#             if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
#                 return True
        
#         return  False
#     return user_passes_test(in_groups)

def group_required(group_names):
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs) :
            if request.user.is_authenticated:
                if not bool(request.user.groups.filter(name__in=group_names)) | request.user.is_superuser:
                    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
                        response_data = {}
                        response_data['status'] = 'false'
                        response_data['stable'] = 'true'
                        response_data['title'] = 'Permission Denied'
                        response_data['message'] = "You have no permission to do this action."
                        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
                    else:
                        context = {
                            "title" : "Permission Denied"
                        }
                        return HttpResponse('<h1>Permission Denied</h1>')

            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper