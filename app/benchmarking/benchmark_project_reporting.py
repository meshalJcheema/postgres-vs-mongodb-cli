from app.use_cases.project_reporting import run_project_reporting_use_case
from app.benchmarking.benchmarking_runner import measure_time

def benchmark_project_reporting(repo):
    report_result = measure_time(
        "Generate Project Summary",
        run_project_reporting_use_case,
        repo
    )

    return [report_result.to_dict()]
