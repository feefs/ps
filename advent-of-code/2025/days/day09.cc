#include "day09.hh"

#include <boost/geometry.hpp>

#include "absl/log/log.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "absl/strings/str_cat.h"
#include "absl/strings/str_split.h"

namespace day09 {

struct Point {
  int i;
  int j;
};

absl::StatusOr<std::vector<Point>> ParsePoints(
    std::vector<std::string>& lines) {
  std::vector<Point> result = {};
  for (auto line : lines) {
    std::vector<std::string_view> split = absl::StrSplit(line, ",");
    if (split.size() != 2) {
      return absl::InvalidArgumentError(
          absl::StrCat("Split string doesn't have a length of 2: ", line));
    }
    int i, j;
    if (!absl::SimpleAtoi(split[0], &i)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse string into int: ", split[0]));
    }
    if (!absl::SimpleAtoi(split[1], &j)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse string into int: ", split[1]));
    }
    result.push_back(Point{.i = i, .j = j});
  }
  return result;
}

absl::Status PartOne(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<Point>> parse_points_result = ParsePoints(lines);
  if (!parse_points_result.ok()) {
    return parse_points_result.status();
  }
  std::vector<Point> points = *std::move(parse_points_result);

  int64_t result = 0;
  for (int i = 0; i < std::ssize(points); i++) {
    for (int j = i + 1; j < std::ssize(points); j++) {
      Point p1 = points[i];
      Point p2 = points[j];
      int64_t area =
          (std::labs(p1.i - p2.i) + 1) * (std::labs(p1.j - p2.j) + 1);
      if (area > result) {
        result = area;
      }
    }
  }

  // answer: 4758598740
  LOG(INFO) << result;

  return absl::OkStatus();
}

absl::Status PartTwo(std::vector<std::string> lines) {
  using point_t = boost::geometry::model::d2::point_xy<int64_t>;
  using polygon_t = boost::geometry::model::polygon<point_t>;

  absl::StatusOr<std::vector<Point>> parse_points_result = ParsePoints(lines);
  if (!parse_points_result.ok()) {
    return parse_points_result.status();
  }
  std::vector<Point> points = *std::move(parse_points_result);

  polygon_t polygon;
  for (const auto& point : points) {
    boost::geometry::append(polygon, point_t{point.i, point.j});
  }
  boost::geometry::correct(polygon);

  int64_t result = 0;
  int n = std::ssize(points);
  LOG(INFO) << absl::StrCat("Processing ", n, " points...");
  for (int i = 0; i < n; i++) {
    if (i % 10 == 0) {
      LOG(INFO) << absl::StrCat("i: ", i);
    }
    for (int j = i + 1; j < n; j++) {
      Point p1 = points[i];
      Point p2 = points[j];

      // A boost geometry box is described by a min corner and a max corner.
      boost::geometry::model::box<point_t> rect(
          point_t{std::min(p1.i, p2.i), std::min(p1.j, p2.j)},
          point_t{std::max(p1.i, p2.i), std::max(p1.j, p2.j)});

      if (boost::geometry::covered_by(rect, polygon)) {
        int64_t area =
            (std::labs(p1.i - p2.i) + 1) * (std::labs(p1.j - p2.j) + 1);
        if (area > result) {
          result = area;
        }
      }
    }
  }

  // answer: 1474699155
  LOG(INFO) << result;

  return absl::OkStatus();
}

}  // namespace day09
