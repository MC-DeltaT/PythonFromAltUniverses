#include <chrono>
#include <concepts>
#include <iostream>
#include <string>


template<typename T>
concept Named = requires (T const& t) {
    { t.name } -> std::same_as<std::string const&>;
};


struct Person {
    std::string name;
    std::chrono::year_month_day dob;
};


void print_name(Named auto const& named) {
    std::cout << named.name << std::endl;
}


int main() {
    using namespace std::chrono;

    Person const person{"Foo Bar", 2022y/3/16};
    print_name(person);
}
