from typing import TypeVar


T = TypeVar('T')


def rotate_array_left(array: list[T], rotation: int) -> list[T]:
    result: list[T] = []
    for i in range(len(array)):
        new_index = (i + rotation) % len(array)
        result.append(array[new_index])
    return result


strings = ['is', 'cool', 'hello', 'world!', 'python']
strings_rotated = rotate_array_left(strings, 2)
for s in strings_rotated:
    print(s)
