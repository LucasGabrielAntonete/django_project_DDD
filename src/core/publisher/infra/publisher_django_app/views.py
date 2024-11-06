from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from core.publisher.infra.publisher_django_app.models import Publisher
from core.publisher.infra.publisher_django_app.serializers import CreatePublisherSerializer, CreatePublisherResponseSerializer, ListPublisherSerializer

from core.publisher.infra.publisher_django_app.repository import DjangoORMPublisherRepository
from core.publisher.application.use_cases.create_publisher import CreatePublisherInput
from core.publisher.application.use_cases.create_publisher import CreatePublisherUseCase
from core.publisher.application.use_cases.list_publisher import ListPublisherUseCase


class PublisherViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = CreatePublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        request_input = CreatePublisherInput(**serializer.data)
        use_case = CreatePublisherUseCase(repository = DjangoORMPublisherRepository(models=Publisher))

        output = use_case.execute(request_input)
        return Response(status=status.HTTP_201_CREATED, data=CreatePublisherResponseSerializer(output).data)
    

    def list(self, request):
        use_case = ListPublisherUseCase(repository = DjangoORMPublisherRepository(models=Publisher))
        output = use_case.execute()
        return Response(
            status=status.HTTP_200_OK,
            data=ListPublisherSerializer(output, many=True).data
        )