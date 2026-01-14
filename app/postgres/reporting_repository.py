from app.postgres.connection import get_pg_connection

class PostgresReportingRepository:

    def get_project_summary(self, project_name: str):
        conn = get_pg_connection()
        cur = conn.cursor()

        # Total teams
        cur.execute(
            """
            SELECT COUNT(*)
            FROM teams t
            JOIN projects p ON p.id = t.project_id
            WHERE p.name = %s
            """,
            (project_name,)
        )
        total_teams = cur.fetchone()[0]

        # Total members
        cur.execute(
            """
            SELECT COUNT(*)
            FROM members m
            JOIN teams t ON t.id = m.team_id
            JOIN projects p ON p.id = t.project_id
            WHERE p.name = %s
            """,
            (project_name,)
        )
        total_members = cur.fetchone()[0]

        # Team-wise member count
        cur.execute(
            """
            SELECT t.lead_name, COUNT(m.id)
            FROM teams t
            JOIN members m ON m.team_id = t.id
            JOIN projects p ON p.id = t.project_id
            WHERE p.name = %s
            GROUP BY t.lead_name
            ORDER BY t.lead_name
            """,
            (project_name,)
        )

        teams = [
            {"lead": row[0], "member_count": row[1]}
            for row in cur.fetchall()
        ]

        cur.close()
        conn.close()

        return {
            "project_name": project_name,
            "total_teams": total_teams,
            "total_members": total_members,
            "teams": teams
        }
