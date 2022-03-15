#include <iostream>
#include <string>


template<class Derived>
class Printer {
public:
    Derived const& print_line(std::string const& message) const {
        auto const& derived = static_cast<Derived const&>(*this);
        derived._write(message + "\n");
        return derived;
    }
};


class StdoutPrinter : public Printer<StdoutPrinter> {
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
    printer.print_line("hello world").print_fancy("CRTP works!");
}
