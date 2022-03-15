#include <iomanip>
#include <iostream>
#include <random>
#include <string>


std::random_device random_engine{};


struct Item {
    unsigned id;
    std::string name;
    float value;
};


void display_item(Item const& item) {
    std::cout << "Item " << item.id << ":\n";
    std::cout << "  Name: \"" << item.name << "\"\n";
    std::cout << "  Value: $" << std::fixed << std::setprecision(2) << item.value << '\n';
}


std::string random_name() {
    auto const length = std::uniform_int_distribution<unsigned>{3, 10}(random_engine);
    auto const alphabet = "abcdefghijklmnopqrstuvwxyz";
    std::string name;
    for (unsigned i = 0; i < length; ++i) {
        name += alphabet[random_engine() % 26];
    }
    return name;
}


float random_value() {
    return std::uniform_real_distribution<float>{0, 1000}(random_engine);
}


std::vector<Item> create_items(unsigned count) {
    std::vector<Item> items;
    for (unsigned i = 0; i < count; ++i) {
        auto const id = i + 1;
        auto const name = random_name();
        auto const value = random_value();
        items.push_back(Item{id, name, value});
    }
    return items;
}


int main() {
    unsigned item_count;
    std::cout << "How many items? ";
    std::cin >> item_count;
    auto const items = create_items(item_count);
    for (auto const& item : items) {
        display_item(item);
        std::cout << '\n';
    }
}
