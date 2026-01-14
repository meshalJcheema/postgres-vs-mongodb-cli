from app.benchmarking.benchmarking_runner import measure_time
from app.use_cases.project_structure import run_project_structure

def benchmark_project_structure(repo):
    insert_result = measure_time(
        "Insert Project Structure",
        run_project_structure,
        repo
    )

    read_result = measure_time(
        "Read Project Structure",
        repo.get_project,
        "AIexpert"
    )

    return [
        insert_result.to_dict(),
        read_result.to_dict()
    ]
