#include <iostream>
#include <ranges>
#include <utility>
#include <vector>


template<std::ranges::range R>
void use_size(R&& range) {
    if constexpr(std::ranges::sized_range<R>) {
        std::cout << std::ranges::size(range) << std::endl;
    }
    else {
        std::vector<std::ranges::range_value_t<R>> buffer;
        for (auto&& e : range) {
            buffer.push_back(std::move(e));
        }
        std::cout << buffer.size() << std::endl;
    }
}


int main() {
    use_size(std::ranges::views::iota(0LL, 1'000'000'000LL));
}
