#pragma once

#include <vector>

#include "absl/status/statusor.h"

namespace util {

class Grid {
 public:
  int m;
  int n;
  std::vector<std::vector<char>> rows;
  bool inBounds(int i, int j) { return 0 <= i && i < m && 0 <= j && j <= n; }

  // Grid is not copyable.
  Grid(const Grid&) = delete;
  Grid& operator=(const Grid&) = delete;

  static absl::StatusOr<std::unique_ptr<Grid>> Create(
      std::vector<std::string> lines);

 private:
  // Clients can't invoke the constructor directly.
  Grid(int m, int n, std::vector<std::vector<char>> in_rows)
      : m(m), n(n), rows(std::move(in_rows)) {}
};

struct Dir {
  int dx;
  int dy;
};

std::vector<Dir> CardinalDirs();

std::vector<Dir> IntercardinalDirs();

std::vector<Dir> AllDirs();

}  // namespace util
