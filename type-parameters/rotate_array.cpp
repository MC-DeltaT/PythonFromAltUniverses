#include <cstddef>
#include <iostream>
#include <string>
#include <vector>


template<typename T>
std::vector<T> rotate_array_left(std::vector<T> const& array, unsigned rotation) {
    std::vector<T> result;
    for (std::size_t i = 0; i < array.size(); ++i) {
        auto const new_index = (i + rotation) % array.size();
        result.push_back(array[new_index]);
    }
    return result;
}


int main() {
    std::vector<std::string> const strings{"is", "cool", "hello", "world!", "C++"};
    auto const strings_rotated = rotate_array_left(strings, 2);
    for (auto const& s : strings_rotated) {
        std::cout << s << std::endl;
    }
}
