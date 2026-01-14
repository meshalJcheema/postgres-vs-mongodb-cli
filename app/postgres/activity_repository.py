from app.postgres.connection import get_pg_connection

class PostgresActivityRepository:

    def insert_activity(self, activity: dict):
        conn = get_pg_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO project_activity_logs
            (project_name, actor_name, action_type, action_description)
            VALUES (%s, %s, %s, %s)
            """,
            (
                activity["project_name"],
                activity["actor_name"],
                activity["action_type"],
                activity["action_description"]
            )
        )

        conn.commit()
        cur.close()
        conn.close()

    def get_activities_for_project(self, project_name: str):
        conn = get_pg_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT actor_name, action_type, action_description, created_at
            FROM project_activity_logs
            WHERE project_name = %s
            ORDER BY created_at DESC
            """,
            (project_name,)
        )

        rows = cur.fetchall()
        cur.close()
        conn.close()

        return [
            {
                "actor": row[0],
                "action_type": row[1],
                "description": row[2],
                "timestamp": row[3].isoformat()
            }
            for row in rows
        ]
