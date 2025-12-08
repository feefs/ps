#include "day07.hh"

#include "absl/container/flat_hash_map.h"
#include "absl/container/flat_hash_set.h"
#include "absl/log/log.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "util/grid.hh"

namespace day07 {

struct Point {
  int i;
  int j;

  friend bool operator==(const Point& lhs, const Point& rhs) {
    return lhs.i == rhs.i && lhs.j == rhs.j;
  }

  template <typename H>
  friend H AbslHashValue(H h, const Point& p) {
    return H::combine(std::move(h), p.i, p.j);
  }
};

struct Grid {
  std::unique_ptr<util::Grid> g;
  Point start;
};

absl::StatusOr<Grid> ParseGrid(std::vector<std::string> lines) {
  absl::StatusOr<std::unique_ptr<util::Grid>> create_grid_result =
      util::Grid::Create(lines);
  if (!create_grid_result.ok()) {
    return create_grid_result.status();
  }
  std::unique_ptr<util::Grid> grid = *std::move(create_grid_result);
  for (int i = 0; i < grid->m; i++) {
    for (int j = 0; j < grid->n; j++) {
      if (grid->rows[i][j] == 'S') {
        return Grid{.g = std::move(grid), .start = Point{i, j}};
      }
    }
  }
  return absl::InvalidArgumentError("Unable to find start 'S' in util::Grid");
}

int64_t ComputeSplits(Grid& grid) {
  absl::flat_hash_set<Point> visited;
  std::function<int64_t(int, int)> f = [&f, &grid, visited](int i,
                                                            int j) mutable {
    Point p{i, j};
    if (visited.contains(p)) {
      return int64_t(0);
    }
    visited.insert(p);
    int64_t result = 0;
    if (grid.g->rows[i][j] == '^') {
      result += 1;
      if (grid.g->inBounds(i, j - 1)) {
        result += f(i, j - 1);
      }
      if (grid.g->inBounds(i, j + 1)) {
        result += f(i, j + 1);
      }
    } else {
      if (grid.g->inBounds(i + 1, j)) {
        result += f(i + 1, j);
      }
    }
    return result;
  };
  return f(grid.start.i, grid.start.j);
}

int64_t ComputeTimelines(Grid& grid) {
  absl::flat_hash_map<Point, int64_t> cache;
  std::function<int64_t(int, int)> f = [&f, &grid, cache](int i,
                                                          int j) mutable {
    Point p{i, j};
    if (cache.contains(p)) {
      return cache.at(p);
    }
    int64_t result = 0;
    if (grid.g->rows[i][j] == '^') {
      if (grid.g->inBounds(i, j - 1)) {
        result += f(i, j - 1);
      }
      if (grid.g->inBounds(i, j + 1)) {
        result += f(i, j + 1);
      }
    } else {
      result = grid.g->inBounds(i + 1, j) ? f(i + 1, j) : 1;
    }
    cache.insert_or_assign(p, result);
    return cache.at(p);
  };
  return f(grid.start.i, grid.start.j);
}

absl::Status PartOne(std::vector<std::string> lines) {
  absl::StatusOr<Grid> parse_grid_result = ParseGrid(lines);
  if (!parse_grid_result.ok()) {
    return parse_grid_result.status();
  }

  int64_t result = ComputeSplits(*parse_grid_result);

  // answer: 1570
  LOG(INFO) << result;

  return absl::OkStatus();
}

absl::Status PartTwo(std::vector<std::string> lines) {
  absl::StatusOr<Grid> parse_grid_result = ParseGrid(lines);
  if (!parse_grid_result.ok()) {
    return parse_grid_result.status();
  }

  int64_t result = ComputeTimelines(*parse_grid_result);

  // answer: 15118009521693
  LOG(INFO) << result;

  return absl::OkStatus();
}

}  // namespace day07
