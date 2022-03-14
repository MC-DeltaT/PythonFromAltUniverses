#include <concepts>
#include <iostream>
#include <string>


template<class Derived>
class BasePrinter {
public:
    Derived const& print(std::string const& message) const {
        auto const& derived = static_cast<Derived const&>(*this);
        derived._write(message);
        return derived;
    }

    Derived const& print_line(std::string const& message) const {
        return print(message + "\n");
    }
};


class StdoutPrinter : public BasePrinter<StdoutPrinter> {
public:
    void print_fancy(std::string const& message) const {
        print_line("~~~ " + message + " ~~~");
    }

    void _write(std::string const& message) const {
        std::cout << message;
    }
};


int main() {
    StdoutPrinter const printer;
    printer.print("hello").print_line(" world").print_fancy("CRTP works!");
}
