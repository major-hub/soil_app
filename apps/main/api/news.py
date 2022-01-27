from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from main.serializers.news import NewsSerializer
from main.models import News


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    ordering_fields = ('created_date', 'view_count', )
    search_fields = ['title', 'title_uz', 'title_ru', 'title_en', 'short_description', 'short_description_uz',
                     'short_description_ru', 'short_description_en', ]

    @action(detail=True, methods=['POST'])
    def views_count(self, request, pk=None):
        news = self.get_object()
        news.view_count += 1
        news.save()
        return Response({'success': True}, status=status.HTTP_200_OK)
