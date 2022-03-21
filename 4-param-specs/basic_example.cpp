#include <concepts>
#include <iostream>
#include <string>
#include <utility>


template<typename C>
auto wrapper(C func) {
    auto inner = [func = std::move(func)]
            <typename... Args> requires std::invocable<C, Args...> (Args&&... args) -> decltype(auto) {
        return func(std::forward<Args>(args)...);
    };

    return inner;
}


float func(int i, std::string s) {
    std::cout << i << std::endl;
    std::cout << s << std::endl;
    return 3.14;
}


int main() {
    auto const wrapped_func = wrapper(func);
    auto const ret = wrapped_func(42, "foo");
}
