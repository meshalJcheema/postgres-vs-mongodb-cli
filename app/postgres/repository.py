from app.postgres.connection import get_pg_connection

class PostgresProjectRepository:

    def insert_project(self, data: dict):
        conn = get_pg_connection()
        cur = conn.cursor()

        # 1. Insert project INTO projects
        cur.execute(
            "INSERT INTO projects (name, manager) VALUES (%s, %s) RETURNING id",
            (data["name"], data["manager"])
        )
        project_id = cur.fetchone()[0]

        # 2. Insert teams
        for team in data.get("teams", []):
            cur.execute(
                "INSERT INTO teams (project_id, lead_name) VALUES (%s, %s) RETURNING id",
                (project_id, team["lead"])
            )
            team_id = cur.fetchone()[0]

            # 3. Insert members
            for member in team.get("members", []):
                cur.execute(
                    "INSERT INTO members (team_id, member_name) VALUES (%s, %s)",
                    (team_id, member)
                )

        conn.commit()
        cur.close()
        conn.close()

    def get_project(self, project_name: str):
        conn = get_pg_connection()
        cur = conn.cursor()

        # 1. Get project
        cur.execute(
            "SELECT id, name, manager FROM projects WHERE name = %s",
            (project_name,)
        )
        project = cur.fetchone()

        if not project:
            return None

        project_id, name, manager = project

        # 2. Get teams
        cur.execute(
            "SELECT id, lead_name FROM teams WHERE project_id = %s",
            (project_id,)
        )

        teams_data = []
        for team_id, lead in cur.fetchall():
            cur.execute(
                "SELECT member_name FROM members WHERE team_id = %s",
                (team_id,)
            )
            members = [row[0] for row in cur.fetchall()]

            teams_data.append({
                "lead": lead,
                "members": members
            })

        cur.close()
        conn.close()

        return {
            "name": name,
            "manager": manager,
            "teams": teams_data
        }
