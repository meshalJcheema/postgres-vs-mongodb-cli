import typer

from app.benchmarking.benchmark_activity_logs import benchmark_activity_logs
from app.benchmarking.benchmark_project_reporting import benchmark_project_reporting
from app.benchmarking.benchmark_project_structure import benchmark_project_structure
from app.mongodb.activity_repository import MongoActivityRepository
from app.mongodb.reporting_repository import MongoReportingRepository
from app.postgres.activity_repository import PostgresActivityRepository
from app.postgres.reporting_repository import PostgresReportingRepository
from app.postgres.repository import PostgresProjectRepository
from app.mongodb.repository import MongoProjectRepository
from app.use_cases.activity_logs import run_activity_log_use_case
from app.use_cases.project_reporting import run_project_reporting_use_case
from app.use_cases.project_structure import run_project_structure

app = typer.Typer()

@app.command()
def project_structure(
    db: str = typer.Option(..., help="Database to use: postgres or mongo")
):
    if db == "postgres":
        repo = PostgresProjectRepository()
    elif db == "mongo":
        repo = MongoProjectRepository()
    else:
        raise typer.BadParameter("db must be 'postgres' or 'mongo'")

    result = run_project_structure(repo)
    print(result)

@app.command()
def activity_logs(
    db: str = typer.Option(..., help="Database to use: postgres or mongo")
):
    if db == "postgres":
        repo = PostgresActivityRepository()
    elif db == "mongo":
        repo = MongoActivityRepository()
    else:
        raise typer.BadParameter("db must be 'postgres' or 'mongo'")

    result = run_activity_log_use_case(repo)
    print(result)

@app.command()
def project_summary(
    db: str = typer.Option(..., help="Database to use: postgres or mongo")
):
    if db == "postgres":
        repo = PostgresReportingRepository()
    elif db == "mongo":
        repo = MongoReportingRepository()
    else:
        raise typer.BadParameter("db must be 'postgres' or 'mongo'")

    result = run_project_reporting_use_case(repo)
    print(result)

@app.command()
def benchmark(
    db: str = typer.Option(..., help="Database to benchmark: postgres or mongo")
):
    if db == "postgres":
        project_repo = PostgresProjectRepository()
        activity_repo = PostgresActivityRepository()
        reporting_repo = PostgresReportingRepository()
    elif db == "mongo":
        project_repo = MongoProjectRepository()
        activity_repo = MongoActivityRepository()
        reporting_repo = MongoReportingRepository()
    else:
        raise typer.BadParameter("db must be 'postgres' or 'mongo'")

    results = []

    results.extend(benchmark_project_structure(project_repo))
    results.extend(benchmark_activity_logs(activity_repo))
    results.extend(benchmark_project_reporting(reporting_repo))

    print("\nBenchmark Results:")
    for result in results:
        print(result)

if __name__ == "__main__":
    app()
