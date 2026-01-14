def run_project_structure(repo):
    project = {
        "name": "AIexpert",
        "manager": "Sameer",
        "teams": [
            {"lead": "Saad", "members": ["Meshal", "Saira", "Umar","Saleha"]},
            {"lead": "Wisam", "members": ["Arshamah", "Matiullah","Usman"]},
            {"lead": "Mahak", "members": ["Aamna", "Rafay", "Usman","Danial"]},
            {"lead": "Shereyar", "members": ["Talha", "Vajiha", "Wajahat", "Faizan"]},
        ]
    }

    repo.insert_project(project)
    return repo.get_project("AIexpert")
