from core.publisher.domain.entities import Publisher
from core.publisher.domain.interfaces import PublisherRepository
from dataclasses import dataclass
from uuid import UUID

@dataclass
class ListItemPublisherInput:
    id : UUID
    name: str
    description: str 
    is_active: bool 

@dataclass
class ListPublisherOutput:
    id: UUID
    name: str
    description: str
    is_active: bool

    

class ListPublisherUseCase:
    def __init__(self, repository: PublisherRepository):
        self.repository = repository

    def execute(self) -> list[ListPublisherOutput]:
        publishers = self.repository.list()
        return [
            ListPublisherOutput(
                id=publisher.id,
                description=publisher.description,
                name=publisher.name,
                is_active=publisher.is_active
            ) for publisher in publishers
        ]

        