#include "day03.hh"

#include "absl/log/check.h"
#include "absl/log/log.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "absl/strings/numbers.h"
#include "absl/strings/str_cat.h"

namespace day03 {

absl::StatusOr<std::vector<std::vector<int>>> ParseBatteries(
    std::vector<std::string> lines) {
  std::vector<std::vector<int>> batteries = {};
  for (size_t i = 0; i < lines.size(); i++) {
    std::vector<int> row = {};
    for (auto digit_char : lines[i]) {
      int digit;
      if (!absl::SimpleAtoi(std::string{digit_char}, &digit)) {
        return absl::InvalidArgumentError(absl::StrCat(
            "Failed to parse char to int: ", std::string{digit_char}));
      }
      row.push_back(digit);
    }
    batteries.push_back(row);
  }
  return batteries;
}

int64_t LargestJoltage(std::vector<int> row, int digits) {
  CHECK(digits > 0);
  CHECK(row.size() > 0);
  int64_t m = digits;
  int64_t n = row.size();

  // dp[i][j] = largest joltage that can be formed from exactly (i + 1) digits
  // using digits from row[j:n].
  auto dp = std::vector(m, std::vector<int64_t>(n, 0));
  int64_t power_of_ten = 1;
  for (int64_t i = 0; i < m; i++) {
    // j starts at (n - 1) - i since it's impossible to form a joltage with
    // exactly (i + 1) digits if there are less than (i + 1) digits to the
    // right of it.
    for (int64_t j = (n - 1) - i; j >= 0; j--) {
      dp[i][j] = std::max(
          // Joltage using only digits from row[j+1:n].
          j < n - 1 ? dp[i][j + 1] : 0,
          // Joltage using the digit row[j] as the most significant digit.
          (row[j] * power_of_ten) +
              ((i > 0 && j < n - 1) ? dp[i - 1][j + 1] : 0));
    }
    power_of_ten *= 10;
  }

  return dp[m - 1][0];
}

absl::Status PartOne(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<std::vector<int>>> parse_batteries_result =
      ParseBatteries(lines);
  if (!parse_batteries_result.ok()) {
    return parse_batteries_result.status();
  }

  int64_t result = 0;
  for (auto row : *parse_batteries_result) {
    result += LargestJoltage(row, 2);
  }

  // answer: 17113
  LOG(INFO) << result;

  return absl::OkStatus();
}

absl::Status PartTwo(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<std::vector<int>>> parse_batteries_result =
      ParseBatteries(lines);
  if (!parse_batteries_result.ok()) {
    return parse_batteries_result.status();
  }

  int64_t result = 0;
  for (auto row : *parse_batteries_result) {
    result += LargestJoltage(row, 12);
  }

  // answer: 169709990062889
  LOG(INFO) << result;

  return absl::OkStatus();
}

}  // namespace day03
