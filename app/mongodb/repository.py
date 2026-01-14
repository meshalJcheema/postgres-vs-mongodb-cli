from app.mongodb.connection import get_mongo_db

class MongoProjectRepository:

    def insert_project(self, data: dict):
        db = get_mongo_db()
        db.projects.insert_one(data)

    def get_project(self, project_name: str):
        db = get_mongo_db()
        return db.projects.find_one(
            {"name": project_name},
            {"_id": 0}   # hide Mongo internal ID
        )
