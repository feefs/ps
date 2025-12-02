#include "day01.hh"

#include "absl/log/log.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "absl/strings/numbers.h"
#include "absl/strings/str_cat.h"

namespace day01 {

struct Rotation {
  enum Direction { Left, Right };
  Direction dir;
  int clicks;
};

absl::StatusOr<std::vector<Rotation>> ParseRotations(
    std::vector<std::string> lines) {
  std::vector<Rotation> rotations = {};
  for (auto line : lines) {
    Rotation::Direction dir;
    char c = line[0];
    if (c == 'L') {
      dir = Rotation::Direction::Left;
    } else if (c == 'R') {
      dir = Rotation::Direction::Right;
    } else {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse character into Rotation::Direction: ",
                       std::string{c}));
    }

    std::string_view clicks_string = std::string_view(line).substr(1);
    int clicks;
    if (!absl::SimpleAtoi(clicks_string, &clicks)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse substring into int: ", clicks_string));
    };

    rotations.push_back(Rotation{.dir = dir, .clicks = clicks});
  }

  return rotations;
}

int Modulo(int a, int b) { return (a % b + b) % b; };

int Rotate(int start, Rotation rotation) {
  switch (rotation.dir) {
    case Rotation::Left: {
      return Modulo(start - rotation.clicks, 100);
    }
    case Rotation::Right: {
      return Modulo(start + rotation.clicks, 100);
    }
  }
}

// Computes the number of times that the dial points to 0.
// This includes if the dial ends at 0, but not if it starts at 0.
int TimesPointingAtZero(int start, Rotation rotation) {
  switch (rotation.dir) {
    case Rotation::Left: {
      // Use symmetry.
      return (Modulo(100 - start, 100) + rotation.clicks) / 100;
    }
    case Rotation::Right: {
      return (start + rotation.clicks) / 100;
    }
  }
}

absl::Status PartOne(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<Rotation>> parse_rotations_result =
      ParseRotations(lines);
  if (!parse_rotations_result.ok()) {
    return parse_rotations_result.status();
  }

  std::vector<Rotation> rotations = *parse_rotations_result;
  int pointing_at = 50;
  int result = 0;
  for (auto rotation : rotations) {
    pointing_at = Rotate(pointing_at, rotation);
    if (pointing_at == 0) {
      result += 1;
    }
  }

  // answer: 1123
  LOG(INFO) << result;

  return absl::OkStatus();
}

absl::Status PartTwo(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<Rotation>> parse_rotations_result =
      ParseRotations(lines);
  if (!parse_rotations_result.ok()) {
    return parse_rotations_result.status();
  }

  std::vector<Rotation> rotations = *parse_rotations_result;
  int pointing_at = 50;
  int result = 0;
  for (auto rotation : rotations) {
    result += TimesPointingAtZero(pointing_at, rotation);
    pointing_at = Rotate(pointing_at, rotation);
  }

  // answer: 6695
  LOG(INFO) << result;

  return absl::OkStatus();
}

}  // namespace day01
