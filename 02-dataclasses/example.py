from dataclasses import dataclass, field


@dataclass
class Vector:
    x: float = field(default=0.0)
    y: float = field(default=0.0)
    z: float = field(default=0.0)


def v_add(v1: Vector, v2: Vector) -> Vector:
    return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)


def v_mul(s: float, v: Vector) -> Vector:
    return Vector(s * v.x, s * v.y, s * v.z)
