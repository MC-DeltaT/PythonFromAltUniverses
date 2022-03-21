from os import PathLike
from pathlib import Path


class AssertFilesystemUnmodified:
    def __init__(self, *paths: str | PathLike[str]) -> None:
        self.paths = tuple(map(Path, paths))

    def __enter__(self) -> 'AssertFilesystemUnmodified':
        self.hashes_before = tuple(map(compute_filesystem_hash, self.paths))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.hashes_after = tuple(map(compute_filesystem_hash, self.paths))
        assert self.hashes_after == self.hashes_before


def compute_filesystem_hash(path: Path, /) -> bytes:
    ...


def test_perform_backup(tmpdir: Path) -> None:
    source_dir = tmpdir / 'source'
    # Populate source_dir with test data
    ...

    target_dir = tmpdir / 'source'

    with AssertFilesystemUnmodified(source_dir):
        results = perform_backup(source_dir, target_dir)

    ...
