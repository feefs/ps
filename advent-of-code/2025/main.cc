#include "absl/container/flat_hash_map.h"
#include "absl/log/log.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "absl/strings/substitute.h"
#include "days/day01.hh"
#include "days/day02.hh"
#include "days/day03.hh"
#include "days/day04.hh"
// #include "days/day05.hh"
// #include "days/day06.hh"
// #include "days/day07.hh"
// #include "days/day08.hh"
// #include "days/day09.hh"
// #include "days/day10.hh"
// #include "days/day11.hh"
// #include "days/day12.hh"
#include "util/init.hh"
#include "util/parts.hh"

const absl::flat_hash_map<int, std::pair<util::Part, util::Part>> kParts{
    {1, {&day01::PartOne, &day01::PartTwo}},
    {2, {&day02::PartOne, &day02::PartTwo}},
    {3, {&day03::PartOne, &day03::PartTwo}},
    {4, {&day04::PartOne, &day04::PartTwo}},
    // {5, {&day05::PartOne, &day05::PartTwo}},
    // {6, {&day06::PartOne, &day06::PartTwo}},
    // {7, {&day07::PartOne, &day07::PartTwo}},
    // {8, {&day08::PartOne, &day08::PartTwo}},
    // {9, {&day09::PartOne, &day09::PartTwo}},
    // {10, {&day10::PartOne, &day10::PartTwo}},
    // {11, {&day11::PartOne, &day11::PartTwo}},
    // {12, {&day12::PartOne, &day12::PartTwo}},
};

absl::StatusOr<util::Part> GetPart(util::RunOptions run_opts) {
  auto it = kParts.find(run_opts.day);
  if (it == kParts.end()) {
    return absl::UnimplementedError(
        absl::Substitute("No function pointer found for day $0 part $1",
                         run_opts.day, run_opts.part));
  }
  std::pair<util::Part, util::Part> pair = it->second;
  return run_opts.part == 1 ? pair.first : pair.second;
}

int main(int argc, char* argv[]) {
  util::RunOptions run_opts = util::InitAndParse(argc, argv);
  LOG(INFO) << absl::Substitute("Running day $0 part $1...", run_opts.day,
                                run_opts.part);

  absl::StatusOr<util::Part> get_part_result = GetPart(run_opts);
  if (!get_part_result.ok()) {
    LOG(ERROR) << get_part_result.status();
    return EXIT_FAILURE;
  }

  if (absl::Status run_part_result = util::RunPart(*get_part_result);
      !run_part_result.ok()) {
    LOG(ERROR) << run_part_result;
    return EXIT_FAILURE;
  }

  return EXIT_SUCCESS;
}
