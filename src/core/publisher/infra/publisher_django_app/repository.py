from core.publisher.domain.interfaces import PublisherRepository
from core.publisher.domain.entities import Publisher
from core.publisher.infra.publisher_django_app.models import Publisher as PublisherModel

class DjangoORMPublisherRepository(PublisherRepository):
    def __init__(self, models):
        self.models = PublisherModel
    
    def create(self, publisher: Publisher):
        created_publisher = self.models.objects.create(
            id = publisher.id,
            name=publisher.name,
            description=publisher.description,
            is_active=publisher.is_active 
        )
        return Publisher(
            id=created_publisher.id,
            name=created_publisher.name,
            description=created_publisher.description,
            is_active=created_publisher.is_active
        )
    
    def list(self) -> list[Publisher]:
        publishers = self.models.objects.all()
        return [
            Publisher(
                id=publisher.id,
                name=publisher.name,
                description=publisher.description,
                is_active=publisher.is_active
            ) for publisher in publishers
        ]