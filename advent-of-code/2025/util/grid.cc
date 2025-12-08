#include "grid.hh"

#include "absl/memory/memory.h"
#include "absl/status/statusor.h"
#include "absl/strings/substitute.h"

namespace util {

// Note that since Grid's constructor is private, we have to use new.
absl::StatusOr<std::unique_ptr<Grid>> Grid::Create(
    std::vector<std::string> lines) {
  std::vector<std::vector<char>> rows = {};
  if (lines.size() == 0) {
    return absl::WrapUnique(new Grid(0, 0, std::move(rows)));
  }
  int m = lines.size();
  int n = lines[0].size();
  for (int i = 0; i < m; i++) {
    std::string line = lines[i];
    auto row = std::vector<char>(line.begin(), line.end());
    if (std::ssize(row) != n) {
      return absl::InvalidArgumentError(
          absl::Substitute("Failed to create util::Grid. string at index $0 "
                           "doesn't have length $1: $2",
                           i, n, line));
    }
    rows.push_back(std::move(row));
  }
  return absl::WrapUnique(new Grid(m, n, std::move(rows)));
}

std::vector<Dir> CardinalDirs() { return {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; }

std::vector<Dir> IntercardinalDirs() {
  return {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}};
}

std::vector<Dir> AllDirs() {
  std::vector<Dir> result = CardinalDirs();
  std::vector<Dir> intercardinal_directions = IntercardinalDirs();
  result.insert(result.end(), intercardinal_directions.begin(),
                intercardinal_directions.end());
  return result;
}

}  // namespace util
