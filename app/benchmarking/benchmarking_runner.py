import time

class BenchmarkResult:
    def __init__(self, operation_name: str, duration_ms: float):
        self.operation_name = operation_name
        self.duration_ms = duration_ms

    def to_dict(self):
        return {
            "operation": self.operation_name,
            "duration_ms": round(self.duration_ms, 3)
        }


def measure_time(operation_name: str, func, *args, **kwargs):
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()

    duration_ms = (end - start) * 1000
    return BenchmarkResult(operation_name, duration_ms)
