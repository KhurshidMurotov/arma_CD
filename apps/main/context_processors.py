from apps.about.models import *


def get_company_data(request):

    context = {
        'company': About.objects.first()
    }

    return context