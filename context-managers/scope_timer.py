import time


class ScopeTimer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.start_time: float | None = None
        self.end_time: float | None = None

    def __enter__(self) -> 'ScopeTimer':
        self.start_time = time.perf_counter_ns()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.end_time = time.perf_counter_ns()
        self._process_time()
    
    def _process_time(self) -> None:
        assert self.start_time is not None
        assert self.end_time is not None
        elapsed_time = self.end_time - self.start_time
        print(f'ScopeTimer name={self.name} time={elapsed_time}ns')


def expensive_function():
    n = 1_000_000
    with ScopeTimer('expensive_function'):
        sum(x ** 3 for x in range(1, n))


expensive_function()