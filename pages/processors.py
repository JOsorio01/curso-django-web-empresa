from .models import Page

def ctx_dict(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return context