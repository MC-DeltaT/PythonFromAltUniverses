#include <iostream>
#include <string>
#include <vector>


struct File {
    std::string name;
    double last_modified;
    bool readonly = false;
};


struct Directory {
    std::string name;
    std::vector<File> files;
    std::vector<Directory> subdirectories;
};


int main() {
    Directory const project{"PythonFromAltUniverses",
        {},
        {
            Directory{"5-dataclasses",
                {
                    File{"filesystem.py", 1647339391.0},
                    File{"address.py", 1647339402.0, true}
                }
            }
        }
    };

    std::cout << project.subdirectories[0].files[0].name << std::endl;
}
