#include <iostream>
#include <utility>
#include <ranges>
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
    auto const t1 = std::ranges::views::iota(0LL, 1'000'000'000LL)
        | std::ranges::views::transform([](auto x) { return x + 1; });
    auto const t2 = t1 | std::ranges::views::transform([](auto x) { return x * 2; });
    use_size(t2);
}
