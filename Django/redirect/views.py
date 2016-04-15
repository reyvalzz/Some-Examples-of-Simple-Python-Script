from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse

def pool(request, pk):
    return HttpResponse("You're looking at question %s." % pk)

def pool_fix(request, pk):
    return HttpResponse("You're looking at question %s." % pk)

class UserRedirectView(RedirectView):
    permanent = False
    def get_redirect_url(self, pk):
        pk = ''.join(str(pk).split('/'))
        return reverse('pool_fix', kwargs={'pk': pk})