#include "day06.hh"

#include <numeric>

#include "absl/log/check.h"
#include "absl/log/log.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "absl/strings/numbers.h"
#include "absl/strings/str_cat.h"
#include "absl/strings/str_split.h"

namespace day06 {

absl::StatusOr<std::vector<std::vector<int64_t>>> ParseNumbers(
    std::vector<std::string> lines) {
  std::vector<std::vector<int64_t>> result = {};
  for (int i = 0; i < std::ssize(lines) - 1; i++) {
    std::vector<std::string_view> split =
        absl::StrSplit(lines[i], absl::ByAsciiWhitespace(), absl::SkipEmpty());
    std::vector<int64_t> row = {};
    int64_t num;
    for (auto s : split) {
      if (!absl::SimpleAtoi(s, &num)) {
        return absl::InvalidArgumentError(
            absl::StrCat("Failed to parse string into int: ", s));
      }
      row.push_back(num);
    }
    result.push_back(row);
  }
  return result;
}

enum Operator { Add, Mul };

absl::StatusOr<std::vector<Operator>> ParseOperators(
    std::vector<std::string> lines) {
  std::vector<Operator> result = {};
  std::vector<std::string> split = absl::StrSplit(
      lines[lines.size() - 1], absl::ByAsciiWhitespace(), absl::SkipEmpty());
  for (auto op : split) {
    if (op == "+") {
      result.push_back(Operator::Add);
    } else if (op == "*") {
      result.push_back(Operator::Mul);
    } else {
      return absl::InvalidArgumentError(
          absl::StrCat("Unrecgonized operator string: ", op));
    }
  }
  return result;
}

absl::StatusOr<std::vector<std::vector<int64_t>>> ParseCephalopodNumbers(
    std::vector<std::string> lines) {
  int m = lines.size();
  int n = lines[0].size();
  std::vector<std::vector<char>> chars = {};
  for (int i = 0; i < m; i++) {
    std::string line = lines[i];
    chars.push_back(std::vector<char>(line.begin(), line.end()));
  }

  auto transposed_chars = std::vector(n, std::vector(m, char{}));
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      transposed_chars[j][i] = chars[i][j];
    }
  }

  std::vector<std::string> transposed_strings = {};
  for (int j = 0; j < n; j++) {
    std::vector<char> transposed_char_row = transposed_chars[j];
    transposed_strings.push_back(
        std::string(transposed_char_row.begin(), transposed_char_row.end()));
  }

  std::vector<std::vector<int64_t>> result = {};
  std::vector<int64_t> curr = {};
  for (int i = 0; i < std::ssize(transposed_strings); i++) {
    std::string_view line = transposed_strings[i];
    std::string_view stripped =
        // Exclude the column that has the operator character.
        absl::StripAsciiWhitespace(line.substr(0, line.length() - 1));
    if (stripped.length() == 0) {
      result.push_back(curr);
      curr = std::vector<int64_t>{};
      continue;
    }
    int64_t num;
    if (!absl::SimpleAtoi(stripped, &num)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse string into int: ", stripped));
    }
    curr.push_back(num);
  }
  result.push_back(curr);

  return result;
}

absl::Status PartOne(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<std::vector<int64_t>>> parse_numbers_result =
      ParseNumbers(lines);
  if (!parse_numbers_result.ok()) {
    return parse_numbers_result.status();
  }
  absl::StatusOr<std::vector<Operator>> parse_operators_result =
      ParseOperators(lines);
  if (!parse_operators_result.ok()) {
    return parse_operators_result.status();
  }
  std::vector<std::vector<int64_t>> numbers = *parse_numbers_result;
  std::vector<Operator> operators = *parse_operators_result;

  int64_t result = 0;
  int m = numbers.size();
  int n = numbers[0].size();
  for (int j = 0; j < n; j++) {
    std::vector<int64_t> operands = {};
    for (int i = 0; i < m; i++) {
      operands.push_back(numbers[i][j]);
    }
    switch (operators[j]) {
      case Operator::Add: {
        result += std::accumulate(operands.begin(), operands.end(), int64_t(0),
                                  std::plus<>{});
        break;
      }
      case Operator::Mul: {
        result += std::accumulate(operands.begin(), operands.end(), int64_t(1),
                                  std::multiplies<>{});
        break;
      }
    }
  }

  // answer: 4878670269096
  LOG(INFO) << result;

  return absl::OkStatus();
}

absl::Status PartTwo(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<std::vector<int64_t>>>
      parse_cephalopod_numbers_result = ParseCephalopodNumbers(lines);
  if (!parse_cephalopod_numbers_result.ok()) {
    return parse_cephalopod_numbers_result.status();
  }
  absl::StatusOr<std::vector<Operator>> parse_operators_result =
      ParseOperators(lines);
  if (!parse_operators_result.ok()) {
    return parse_operators_result.status();
  }
  std::vector<std::vector<int64_t>> numbers = *parse_cephalopod_numbers_result;
  std::vector<Operator> operators = *parse_operators_result;

  CHECK(numbers.size() == operators.size());

  int64_t result = 0;
  for (int i = 0; i < std::ssize(numbers); i++) {
    std::vector<int64_t> operands = numbers[i];
    switch (operators[i]) {
      case Operator::Add: {
        result += std::accumulate(operands.begin(), operands.end(), int64_t(0),
                                  std::plus<>{});
        break;
      }
      case Operator::Mul: {
        result += std::accumulate(operands.begin(), operands.end(), int64_t(1),
                                  std::multiplies<>{});
        break;
      }
    }
  }

  // answer: 8674740488592
  LOG(INFO) << result;

  return absl::OkStatus();
}

}  // namespace day06
