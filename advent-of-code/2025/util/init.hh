#pragma once

namespace util {

struct DayFlag {
  explicit DayFlag(int d = 1) : day{d} {};
  int day;
};

struct PartFlag {
  explicit PartFlag(int p = 1) : part{p} {};
  int part;
};

struct RunOptions {
  int day;
  int part;
};

[[nodiscard]] RunOptions InitAndParse(int argc, char* argv[]);

}  // namespace util
