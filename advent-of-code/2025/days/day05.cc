#include "day05.hh"

#include "absl/log/check.h"
#include "absl/log/log.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "absl/strings/numbers.h"
#include "absl/strings/str_cat.h"
#include "absl/strings/str_split.h"

namespace day05 {

struct Range {
  int64_t start;
  int64_t end;
};

absl::StatusOr<std::pair<std::vector<Range>, std::vector<int64_t>>> Parse(
    std::vector<std::string> lines) {
  int i = 0;

  std::vector<Range> ranges = {};
  for (; i < std::ssize(lines); i++) {
    if (lines[i] == "") {
      i += 1;
      break;
    };
    std::vector<std::string_view> split = absl::StrSplit(lines[i], "-");
    CHECK(split.size() == 2);
    int64_t start;
    int64_t end;
    if (!absl::SimpleAtoi(split[0], &start)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse string into int: ", split[0]));
    }
    if (!absl::SimpleAtoi(split[1], &end)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse string into int: ", split[1]));
    }
    ranges.push_back(Range{.start = start, .end = end});
  }

  std::vector<int64_t> ids = {};
  for (; i < std::ssize(lines); i++) {
    int64_t id;
    if (!absl::SimpleAtoi(lines[i], &id)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse string into int: ", lines[i]));
    }
    ids.push_back(id);
  }

  return std::pair{ranges, ids};
}

// Output ranges are sorted by start.
std::vector<Range> MergeRanges(std::vector<Range> ranges) {
  std::vector<Range> result = {};
  if (ranges.size() == 0) {
    return result;
  }
  std::sort(ranges.begin(), ranges.end(),
            [](const Range& a, const Range& b) { return a.start < b.start; });
  Range curr = ranges[0];
  for (int i = 1; i < std::ssize(ranges); i++) {
    Range& range = ranges[i];
    if (curr.end >= range.start) {
      // range.end might be < curr.end, so take the max.
      curr.end = std::max(curr.end, range.end);
    } else {
      result.push_back(curr);
      curr = range;
    }
  }
  result.push_back(curr);
  return result;
}

absl::Status PartOne(std::vector<std::string> lines) {
  absl::StatusOr<std::pair<std::vector<Range>, std::vector<int64_t>>>
      parse_result = Parse(lines);
  if (!parse_result.ok()) {
    return parse_result.status();
  }

  auto [ranges, ids] = *parse_result;
  std::vector<Range> merged = MergeRanges(ranges);

  int result = 0;
  for (auto id : ids) {
    // Find the first Range with an endpoint greater than id.
    auto it =
        std::lower_bound(merged.begin(), merged.end(), id,
                         [](const Range& a, int64_t id) { return a.end < id; });
    if (it == merged.end()) {
      continue;
    }
    if (it->start <= id && id <= it->end) {
      result += 1;
    }
  }

  // answer: 798
  LOG(INFO) << result;

  return absl::OkStatus();
}

absl::Status PartTwo(std::vector<std::string> lines) {
  absl::StatusOr<std::pair<std::vector<Range>, std::vector<int64_t>>>
      parse_result = Parse(lines);
  if (!parse_result.ok()) {
    return parse_result.status();
  }

  auto [ranges, unused] = *parse_result;
  std::vector<Range> merged = MergeRanges(ranges);

  int64_t result = 0;
  for (auto range : merged) {
    result += range.end - range.start + 1;
  }

  // answer: 366181852921027
  LOG(INFO) << result;

  return absl::OkStatus();
}

}  // namespace day05
