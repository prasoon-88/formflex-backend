from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .models import Form

@csrf_exempt
def create_form(request):
    if not (request.user.is_authenticated):
        return JsonResponse({'error': 'User not authenticated'}, status=401)
    if(request.method == 'POST'):
        body = json.loads(request.body)
        user = request.user

        title = body.get('title',None)
        description = body.get('description',None)

        if title and description:
            form = Form.objects.create(
                user=user,
                title=title,
                description=description
            )
            return JsonResponse({
            'message': 'Form created successfully',
            'form_id': str(form.id)
            }, status=201)
        return JsonResponse({
            'message': 'title or description is missing',
            }, status=404)

    return JsonResponse({
        'message':'method not allowed'
    },status=405)
