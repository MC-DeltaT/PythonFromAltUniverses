#include <chrono>
#include <iostream>
#include <string_view>


class ScopeTimer {
public:
    using Clock = std::chrono::steady_clock;
    static_assert(Clock::is_steady);

    std::string_view name;
    Clock::time_point start_time;
    Clock::time_point end_time;

    ScopeTimer(std::string_view name) :
        name{name},
        start_time{Clock::now()},
        end_time{}
    {}

    ~ScopeTimer() {
        end_time = Clock::now();
        _process_time();
    }

private:
    void _process_time() const {
        auto const elapsed_time_ns = std::chrono::duration_cast<std::chrono::nanoseconds>(end_time - start_time);
        std::cout << "ScopeTimer \"" << name << "\" took " << elapsed_time_ns.count() << "ns\n";
    }
};


void database_query() {
    // ...
    {
        ScopeTimer const timer{"database query"};
        // Send query to database
    }
    // ...
}


int main() {
    database_query();
}
