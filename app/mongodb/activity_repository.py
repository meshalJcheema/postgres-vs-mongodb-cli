from app.mongodb.connection import get_mongo_db
from datetime import datetime

class MongoActivityRepository:

    def insert_activity(self, activity: dict):
        db = get_mongo_db()
        activity["created_at"] = datetime.utcnow()
        db.project_activity_logs.insert_one(activity)

    def get_activities_for_project(self, project_name: str):
        db = get_mongo_db()

        activities = db.project_activity_logs.find(
            {"project_name": project_name},
            {"_id": 0}
        ).sort("created_at", -1)

        return list(activities)
