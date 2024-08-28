def current_user_processor(request):
    return {
        'current_user': request.user
    }
