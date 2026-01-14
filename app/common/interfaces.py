from abc import ABC, abstractmethod

class ProjectRepository(ABC):

    @abstractmethod
    def insert_project(self, data: dict):
        pass

    @abstractmethod
    def get_project(self, project_name: str):
        pass
