# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from social_core.exceptions import AuthForbidden
from social_django.middleware import SocialAuthExceptionMiddleware
from django.contrib import messages


class CustomSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if isinstance(exception, AuthForbidden):
            messages.add_message(
                request, messages.ERROR, self.get_message(request, exception)
            )
            print(exception)
            return redirect("home")

        return super().process_exception(request, exception)