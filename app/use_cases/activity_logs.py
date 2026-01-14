def run_activity_log_use_case(repo):
    activities = [
        {
            "project_name": "AIexpert",
            "actor_name": "Saad",
            "action_type": "ADD_MEMBER",
            "action_description": "Saad added Meshal to the backend team"
        },
        {
            "project_name": "AIexpert",
            "actor_name": "Wisam",
            "action_type": "ASSIGN_TASK",
            "action_description": "Wisam assigned API testing task to Arshamah"
        },
        {
            "project_name": "AIexpert",
            "actor_name": "Sameer",
            "action_type": "REVIEW",
            "action_description": "Sameer reviewed the weekly project progress"
        }
    ]

    for activity in activities:
        repo.insert_activity(activity)

    return repo.get_activities_for_project("AIexpert")
