#include "init.hh"

#include "absl/flags/flag.h"
#include "absl/flags/parse.h"
#include "absl/flags/usage.h"
#include "absl/log/globals.h"
#include "absl/log/initialize.h"
#include "absl/log/log.h"
#include "absl/strings/substitute.h"

ABSL_FLAG(std::optional<util::DayFlag>, day, std::nullopt,
          "[0-12] to run the solution for that day");
ABSL_FLAG(std::optional<util::PartFlag>, part, std::nullopt,
          "[1|2] to run part 1 or 2 respectively");

namespace util {

bool AbslParseFlag(absl::string_view text, DayFlag* d, std::string* error) {
  // Convert from text to int using the int-flag parser.
  if (!absl::ParseFlag(text, &d->day, error)) {
    return false;
  }
  if (!(1 <= d->day && d->day <= 12)) {
    *error = "not in range [1-12]";
    return false;
  }
  return true;
}

std::string AbslUnparseFlag(DayFlag d) { return absl::UnparseFlag(d.day); }

bool AbslParseFlag(absl::string_view text, PartFlag* p, std::string* error) {
  // Convert from text to int using the int-flag parser.
  if (!absl::ParseFlag(text, &p->part, error)) {
    return false;
  }
  if (p->part != 1 && p->part != 2) {
    *error = "not [1|2]";
    return false;
  }
  return true;
}

std::string AbslUnparseFlag(PartFlag p) { return absl::UnparseFlag(p.part); }

RunOptions InitAndParse(int argc, char* argv[]) {
  absl::InitializeLog();
  absl::SetStderrThreshold(absl::LogSeverity::kInfo);
  absl::SetProgramUsageMessage(absl::Substitute(
      "Advent of Code 2025. Usage:\n  $0 --day=[1-12] --part=[1|2]", argv[0]));
  absl::ParseCommandLine(argc, argv);

  std::optional<util::DayFlag> day_option = absl::GetFlag(FLAGS_day);
  std::optional<util::PartFlag> part_option = absl::GetFlag(FLAGS_part);
  if (!day_option.has_value()) {
    LOG(QFATAL) << "--day=[1-12] not provided";
  }
  if (!part_option.has_value()) {
    LOG(QFATAL) << "--part=[1|2] not provided";
  }

  return RunOptions{.day = day_option->day, .part = part_option->part};
}

}  // namespace util
