from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect


class AuthMiddleware(MiddlewareMixin):
    """中间商"""

    def process_request(self, request):
        if request.path_info == "/login/" or request.path_info == "/admin/login/":
            return

        info_dict = request.session.get("info")
        if info_dict:
            return

        return redirect('/login/')
