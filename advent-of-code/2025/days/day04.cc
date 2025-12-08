#include "day04.hh"

#include "absl/log/log.h"
#include "absl/status/status.h"
#include "util/grid.hh"

namespace day04 {

absl::Status PartOne(std::vector<std::string> lines) {
  absl::StatusOr<std::unique_ptr<util::Grid>> create_grid_result =
      util::Grid::Create(lines);
  if (!create_grid_result.ok()) {
    return create_grid_result.status();
  }
  std::unique_ptr<util::Grid> grid = *std::move(create_grid_result);

  int result = 0;
  for (int i = 0; i < grid->m; i++) {
    for (int j = 0; j < grid->n; j++) {
      if (grid->rows[i][j] != '@') {
        continue;
      }
      int adjacent = 0;
      for (auto dir : util::AllDirs()) {
        int ni = i + dir.dx;
        int nj = j + dir.dy;
        if (grid->inBounds(ni, nj) && grid->rows[ni][nj] == '@') {
          adjacent += 1;
        }
      }
      if (adjacent < 4) {
        result += 1;
      }
    }
  }

  // answer: 1587
  LOG(INFO) << result;

  return absl::OkStatus();
}

absl::Status PartTwo(std::vector<std::string> lines) {
  absl::StatusOr<std::unique_ptr<util::Grid>> create_grid_result =
      util::Grid::Create(lines);
  if (!create_grid_result.ok()) {
    return create_grid_result.status();
  }
  std::unique_ptr<util::Grid> grid = *std::move(create_grid_result);

  int result = 0;
  bool removed = false;
  do {
    removed = false;
    for (int i = 0; i < grid->m; i++) {
      for (int j = 0; j < grid->n; j++) {
        if (grid->rows[i][j] != '@') {
          continue;
        }
        int adjacent = 0;
        for (auto dir : util::AllDirs()) {
          int ni = i + dir.dx;
          int nj = j + dir.dy;
          if (grid->inBounds(ni, nj) && grid->rows[ni][nj] == '@') {
            adjacent += 1;
          }
        }
        if (adjacent < 4) {
          grid->rows[i][j] = '.';
          result += 1;
          removed = true;
        }
      }
    }
  } while (removed);

  // answer: 8946
  LOG(INFO) << result;

  return absl::OkStatus();
}

}  // namespace day04
