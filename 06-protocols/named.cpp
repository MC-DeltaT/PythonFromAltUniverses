#include <chrono>
#include <concepts>
#include <iostream>
#include <string>


namespace chrono = std::chrono;


template<typename T>
concept Named = requires (T const& t) {
    { t.name } -> std::same_as<std::string const&>;
};


struct Person {
    std::string name;
    chrono::year_month_day dob;
};


void print_name(Named auto const& named) {
    std::cout << named.name << std::endl;
}


int main() {
    Person const person{"Foo Bar", {chrono::year{2022}, chrono::month{3}, chrono::day{16}}};
    print_name(person);
}
