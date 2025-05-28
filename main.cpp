#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>

bool validsolution(char inchar) {
  char alphabet[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                     'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
                     'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                     's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
  for (char a : alphabet) {
    if (inchar == a) {
      return true;
    }
  }
  return false;
}

// C++ bruteforcer to test python
int asciibruteforecer(std::string targetfile) {
  int sol = 0, holder;
  bool solved = false;
  char checkchar, constchar;
  std::ifstream file;
  file.open(targetfile);
  std::string line;
  std::getline(file, line);
  constchar = validsolution(line[0]);
  while (solved == false) {
    solved = validsolution(checkchar);
    sol++;
    holder = int(constchar);
    checkchar = char(holder - sol);
  }
  std::cout << sol << "\n";

  file.close();
  return sol;
}
void completedecryption(std::string targetfile) {
  int tractor = asciibruteforecer(targetfile);
  std::ifstream file;
  int holder;
  file.open(targetfile);
  std::string line, convline;
  while (std::getline(file, line)) {
    for (char a : line) {
      holder = int(a) - tractor;
      std::cout << char(holder);
    }
  }

  file.close();
}

void readfile(std::string targetfile) {
  std::ifstream file;
  file.open(targetfile);
  std::string line;
  while (std::getline(file, line)) {
    std::cout << line << '\n';
  }
  file.close();
}
int main() {
  // give number back
  completedecryption("blackout");
}
