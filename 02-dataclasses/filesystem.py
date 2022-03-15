from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class File:
    name: str
    last_modified: datetime
    readonly: bool = False


@dataclass
class Directory:
    name: str
    files: list[File] = field(default_factory=list)
    subdirectories: list['Directory'] = field(default_factory=list)


project = Directory('PythonFromAltUniverses',
    subdirectories=[
        Directory('02-dataclasses',
            files=[
                File('filesystem.py', datetime(2022, 3, 15, 18, 9, 40)),
                File('address.py', datetime(2022, 3, 15, 17, 50, 0), readonly=True)
            ]
        )
    ]
)

print(project.subdirectories[0].files[0].name)
print(project)
