#include <codecvt>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <locale>
#include <string>

bool validsolution(char32_t inchar) {
  char32_t alphabet[] = {U'A', U'B', U'C', U'D', U'E', U'F', U'G', U'H', U'I',
                         U'J', U'K', U'L', U'M', U'N', U'O', U'P', U'Q', U'R',
                         U'S', U'T', U'U', U'V', U'W', U'X', U'Y', U'Z', U'a',
                         U'b', U'c', U'd', U'e', U'f', U'g', U'h', U'i', U'j',
                         U'k', U'l', U'm', U'n', U'o', U'p', U'q', U'r', U's',
                         U't', U'u', U'v', U'w', U'x', U'y', U'z'};

  for (char32_t a : alphabet) {
    if (inchar == a) {
      return true;
    }
  }
  return false;
  std::cout << inchar << " didn't wasn't working";
}

// C++ bruteforcer to test python
int asciibruteforecer(std::string targetfile) {
  int sol = 0, holder;
  bool solved = false;
  char32_t checkchar, constchar;
  std::ifstream file;
  file.open(targetfile);
  std::string line;
  std::getline(file, line);
  constchar = char32_t(line[0]);
  while (solved == false) {
    solved = validsolution(checkchar);
    sol++;
    holder = int(constchar);
    checkchar = char32_t(holder - sol);
  }
  std::cout << sol << "\n";

  file.close();
  return sol;
}
void completedecryption(std::string targetfile) {
  int tractor;
  char32_t nicehold;
  // tractor = asciibruteforecer(targetfile);
  tractor = 216;
  std::ifstream file;
  int holder;
  file.open(targetfile);
  std::string line, convline;
  while (std::getline(file, line)) {
    for (char32_t a : line) {
      holder = int(a) - tractor;
      nicehold = static_cast<char32_t>(holder);
      std::cout << char(nicehold);
    }
    std::cout << "\n";
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
