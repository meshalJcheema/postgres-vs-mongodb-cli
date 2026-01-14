from app.mongodb.connection import get_mongo_db

class MongoReportingRepository:

    def get_project_summary(self, project_name: str):
        db = get_mongo_db()

        project = db.projects.find_one(
            {"name": project_name},
            {"_id": 0}
        )

        if not project:
            return None

        teams = project.get("teams", [])

        team_summaries = []
        total_members = 0

        for team in teams:
            member_count = len(team.get("members", []))
            total_members += member_count

            team_summaries.append({
                "lead": team.get("lead"),
                "member_count": member_count
            })

        return {
            "project_name": project_name,
            "total_teams": len(teams),
            "total_members": total_members,
            "teams": team_summaries
        }
