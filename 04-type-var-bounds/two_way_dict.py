from typing import Generic, Hashable, TypeVar


THashable1 = TypeVar('THashable1', bound=Hashable)
THashable2 = TypeVar('THashable2', bound=Hashable)


class TwoWayDict(Generic[THashable1, THashable2]):
    def __init__(self) -> None:
        self.map1: dict[THashable1, THashable2] = {}
        self.map2: dict[THashable2, THashable1] = {}

    def insert(self, key1: THashable1, key2: THashable2) -> None:
        self.map1[key1] = key2
        self.map2[key2] = key1
    
    def get_by_key1(self, key1: THashable1) -> THashable2:
        return self.map1[key1]
    
    def get_by_key2(self, key2: THashable2) -> THashable1:
        return self.map2[key2]


two_way_dict: TwoWayDict[int, str] = TwoWayDict()
two_way_dict.insert(42, 'foo')
v1 = two_way_dict.get_by_key1(42)
print(v1)
v2 = two_way_dict.get_by_key2('foo')
print(v2)
