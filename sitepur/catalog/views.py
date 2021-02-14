from django.shortcuts import render, get_object_or_404
from .models import Articles, ArticlesImage
from django.views.generic import DetailView

def catalog_home(request):
    catalog = Articles.objects.all()
    return render(request, 'catalog/catalog_home.html', {'catalog': catalog})

class ShoesDetailView(DetailView):
    model = Articles
    template_name = 'catalog/details_view.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ShoesDetailView, self).get_context_data(**kwargs)
        # Add extra context from another model
        context['articleimg'] = ArticlesImage.objects.filter(post=self.object)
        return context

