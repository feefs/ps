#include "day02.hh"

#include "absl/container/flat_hash_set.h"
#include "absl/log/check.h"
#include "absl/log/log.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "absl/strings/numbers.h"
#include "absl/strings/str_cat.h"
#include "absl/strings/str_split.h"

namespace day02 {

struct Range {
  int64_t start;
  int64_t end;
  std::string start_str;
  std::string end_str;
};

absl::StatusOr<std::vector<Range>> ParseRanges(std::vector<std::string> lines) {
  std::vector<Range> ranges = {};
  for (auto line : lines) {
    std::vector<std::string_view> range_strings =
        absl::StrSplit(line, ",", absl::SkipEmpty());
    for (auto range_string : range_strings) {
      std::vector<std::string_view> ids = absl::StrSplit(range_string, "-");
      CHECK(ids.size() == 2);
      int64_t start;
      int64_t end;
      if (!absl::SimpleAtoi(ids[0], &start)) {
        return absl::InvalidArgumentError(
            absl::StrCat("Failed to parse string into int: ", ids[0]));
      }
      if (!absl::SimpleAtoi(ids[1], &end)) {
        return absl::InvalidArgumentError(
            absl::StrCat("Failed to parse string into int: ", ids[1]));
      }
      ranges.push_back(Range{.start = start,
                             .end = end,
                             .start_str = std::string(ids[0]),
                             .end_str = std::string(ids[1])});
    }
  }
  return ranges;
}

// Generates all invalid IDs in a `range` that are constructed by repeating
// sequences exactly `digits` long. If `unlimited_repetitions` is false, then
// the sequences can only be repeated once.
absl::StatusOr<std::vector<int64_t>> GenerateInvalidIds(
    Range range, int digits, bool unlimited_repetitions) {
  std::vector<int64_t> result = {};
  int total_digits = range.start_str.size();
  CHECK(digits <= total_digits);

  for (int64_t sequence = std::pow(10, digits - 1);
       sequence < std::pow(10, digits); sequence++) {
    std::string sequence_string = absl::StrCat(sequence);
    std::string invalid_id_string = sequence_string;
    while (true) {
      absl::StrAppend(&invalid_id_string, sequence_string);
      int64_t invalid_id;
      if (!absl::SimpleAtoi(invalid_id_string, &invalid_id)) {
        return absl::InternalError(absl::StrCat(
            "Failed to convert string into int64_t: ", invalid_id_string));
      }
      if (invalid_id > range.end) {
        break;
      }
      if (invalid_id >= range.start) {
        result.push_back(invalid_id);
      }
      if (!unlimited_repetitions) {
        break;
      }
    }
  }

  return result;
}

absl::StatusOr<std::vector<int64_t>> InvalidIds(Range range,
                                                bool unlimited_repetitions) {
  // Some IDs can be constructed multiple ways (such as 3333 - 3 repeated 4
  // times, or 33 repeated twice), so we must use a set.
  absl::flat_hash_set<int64_t> invalid_ids = {};
  int num_digits = range.start_str.size();
  for (int digits = 1; digits <= std::ceil(float(num_digits) / 2); digits++) {
    absl::StatusOr<std::vector<int64_t>> generate_invalid_ids_result =
        GenerateInvalidIds(range, digits, unlimited_repetitions);
    if (!generate_invalid_ids_result.ok()) {
      return generate_invalid_ids_result.status();
    }
    std::vector<int64_t> generated_invalid_ids = *generate_invalid_ids_result;
    invalid_ids.insert(generated_invalid_ids.begin(),
                       generated_invalid_ids.end());
  }
  return std::vector<int64_t>(invalid_ids.begin(), invalid_ids.end());
}

absl::Status PartOne(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<Range>> parse_ranges_result = ParseRanges(lines);
  if (!parse_ranges_result.ok()) {
    return parse_ranges_result.status();
  }

  int64_t result = 0;
  for (auto range : *parse_ranges_result) {
    absl::StatusOr<std::vector<int64_t>> invalid_ids_result =
        InvalidIds(range, false);
    if (!invalid_ids_result.ok()) {
      return invalid_ids_result.status();
    }
    for (auto invalid_id : *invalid_ids_result) {
      result += invalid_id;
    }
  }

  // answer: 23534117921
  LOG(INFO) << result;

  return absl::OkStatus();
}

absl::Status PartTwo(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<Range>> parse_ranges_result = ParseRanges(lines);
  if (!parse_ranges_result.ok()) {
    return parse_ranges_result.status();
  }

  int64_t result = 0;
  for (auto range : *parse_ranges_result) {
    absl::StatusOr<std::vector<int64_t>> invalid_ids_result =
        InvalidIds(range, true);
    if (!invalid_ids_result.ok()) {
      return invalid_ids_result.status();
    }
    for (auto invalid_id : *invalid_ids_result) {
      result += invalid_id;
    }
  }

  // answer: 31755323497
  LOG(INFO) << result;

  return absl::OkStatus();
}

}  // namespace day02
