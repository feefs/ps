#include "parts.hh"

#include <fstream>

#include "absl/status/status.h"
#include "absl/strings/str_cat.h"

namespace util {

absl::Status RunPart(Part part) {
  std::ifstream file{"input.txt"};
  if (!file.is_open()) {
    return absl::UnavailableError(
        absl::StrCat("Error opening input.txt: ", strerror(errno)));
  }

  std::vector<std::string> lines{};
  std::string line{};
  while (std::getline(file, line)) {
    lines.push_back(std::move(line));
  }

  return part(lines);
}

}  // namespace util
