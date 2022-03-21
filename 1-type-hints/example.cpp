#include <iostream>
#include <optional>
#include <string>
#include <vector>


struct Car {
    std::string brand;
    std::string model;
    unsigned year;
    std::optional<float> value = std::nullopt;
};


template<class OStream>
OStream& operator<<(OStream& stream, Car const& car) {
    stream << car.year << ' ' << car.brand << ' ' << car.model;
    if (car.value.has_value()) {
        stream << " valued at $" << car.value.value();
    }
    return stream;
}


int main() {
    std::vector<Car> cars;
    cars.push_back({"Hyundai", "i30", 2008});
    cars.push_back({"Tesla", "Model S", 2021, 110000});
    for (auto const& car : cars) {
        std::cout << car << std::endl;
    }
}
