#include <concepts>
#include <cstddef>
#include <functional>
#include <iostream>
#include <ranges>
#include <vector>


template<typename T>
concept Hashable = requires (T const& t) {
    { std::hash<T>{}(t) } -> std::same_as<std::size_t>;
};


template<std::ranges::forward_range R, typename T = std::ranges::range_value_t<R>> requires Hashable<T>
std::size_t array_hash(R&& array) {
    // Hash function by Daniel J. Bernstein
    std::size_t result = 5381;
    for (auto const& element : array) {
        result = result * 33 + std::hash<T>{}(element);
    }
    return result;
}


int main() {
    std::vector<int> const array{1, 4, 67, 5346, 23};
    auto const h = array_hash(array);
    std::cout << h << std::endl;
}
