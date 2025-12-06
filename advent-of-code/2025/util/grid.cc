#include "grid.hh"

namespace util {

Grid Grid::Create(std::vector<std::string> lines) {
  int m = lines.size();
  int n = lines[0].size();
  auto rows = std::vector(m, std::vector(n, char{}));
  for (int i = 0; i < m; i++) {
    std::string line = lines[i];
    rows[i] = std::vector<char>(line.begin(), line.end());
  }
  return Grid(m, n, std::move(rows));
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
