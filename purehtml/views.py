from django.views import generic


class IndexView(generic.ListView):
    template_name = 'purehtml/index.html'