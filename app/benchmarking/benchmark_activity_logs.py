from app.use_cases.activity_logs import run_activity_log_use_case
from app.benchmarking.benchmarking_runner import measure_time

def benchmark_activity_logs(repo):
    insert_result = measure_time(
        "Insert Activity Logs",
        run_activity_log_use_case,
        repo
    )

    read_result = measure_time(
        "Read Activity Logs",
        repo.get_activities_for_project,
        "AIexpert"
    )

    return [
        insert_result.to_dict(),
        read_result.to_dict()
    ]
