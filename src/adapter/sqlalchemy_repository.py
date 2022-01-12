from typing import List, Optional
from src.common.abstracts.repository import T, AbstractRepository


class SqlAlchemyRepository(AbstractRepository[T]):
    model: T

    def __init__(self, session):
        self.session = session

    def add(self, model: T):
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)

        return model

    def get(self, **kwargs) -> Optional[T]:
        pass

    def all(self) -> List[T]:
        pass