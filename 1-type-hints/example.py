class Car:
    def __init__(self, brand: str, model: str, year: int, value: float | None = None) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.value = value
    
    def __str__(self) -> str:
        s = f'{self.year} {self.brand} {self.model}'
        if self.value is not None:
            s += f' valued at ${self.value:.2f}'
        return s


cars: list[Car] = []
cars.append(Car('Hyundai', 'i30', 2008))
cars.append(Car('Tesla', 'Model S', 2021, 110000))
for car in cars:
    print(car)
