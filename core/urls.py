from django.urls import path
from .views import TextGenerationView, ImageGenerationView, FlowView

urlpatterns = [
    path('generate/text/', TextGenerationView.as_view(), name='text-generation'),
    path('generate/image/', ImageGenerationView.as_view(), name='image-generation'),
    path('generate/flow/', FlowView.as_view(), name='flow-generation'),
]
