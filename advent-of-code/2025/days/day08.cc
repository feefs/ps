#include "day08.hh"

#include <numeric>

#include "absl/log/log.h"
#include "absl/status/status.h"
#include "absl/status/statusor.h"
#include "absl/strings/str_cat.h"
#include "absl/strings/str_split.h"

namespace day08 {

struct Point {
  int64_t x;
  int64_t y;
  int64_t z;
};

struct UnionFind {
  std::vector<int64_t> parent;
  std::vector<int64_t> size;
  int64_t num_components;
  explicit UnionFind(int64_t n) : num_components(n) {
    parent.resize(n);
    std::iota(parent.begin(), parent.end(), 0);
    size.assign(n, 1);
  }
  int64_t Root(int64_t id) {
    if (parent[id] == id) {
      return id;
    }
    // Path compression.
    parent[id] = Root(parent[id]);
    return parent[id];
  };
  void Union(int64_t a, int64_t b) {
    int64_t r1 = Root(a);
    int64_t r2 = Root(b);
    if (r1 == r2) {
      return;
    }
    if (size[r1] < size[r2]) {
      std::swap(r1, r2);
    }
    parent[r2] = r1;
    size[r1] += size[r2];
    num_components -= 1;
  };
};

struct Edge {
  double distance;
  int64_t u;
  int64_t v;
};

absl::StatusOr<std::vector<Point>> ParsePoints(
    const std::vector<std::string>& lines) {
  std::vector<Point> result = {};
  for (const std::string_view line : lines) {
    std::vector<std::string_view> split = absl::StrSplit(line, ",");
    if (split.size() != 3) {
      return absl::InvalidArgumentError(
          absl::StrCat("Split string doesn't have a length of 3: ", line));
    }
    int64_t x, y, z;
    if (!absl::SimpleAtoi(split[0], &x)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse string into int: ", split[0]));
    }
    if (!absl::SimpleAtoi(split[1], &y)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse string into int: ", split[1]));
    }
    if (!absl::SimpleAtoi(split[2], &z)) {
      return absl::InvalidArgumentError(
          absl::StrCat("Failed to parse string into int: ", split[2]));
    }
    result.push_back(Point{.x = x, .y = y, .z = z});
  }
  return result;
}

// Returns the results sorted by ascending distance.
std::vector<Edge> ComputeEdges(const std::vector<Point>& points) {
  std::vector<Edge> result = {};
  for (int i = 0; i < std::ssize(points); i++) {
    for (int j = i + 1; j < std::ssize(points); j++) {
      Point p1 = points[i];
      Point p2 = points[j];
      double dx = p1.x - p2.x;
      double dy = p1.y - p2.y;
      double dz = p1.z - p2.z;
      double distance = std::sqrt(dx * dx + dy * dy + dz * dz);
      result.push_back(Edge{.distance = distance, .u = i, .v = j});
    }
  }
  std::sort(result.begin(), result.end(), [](const Edge& a, const Edge& b) {
    return a.distance < b.distance;
  });
  return result;
}

absl::Status PartOne(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<Point>> parse_points_result = ParsePoints(lines);
  if (!parse_points_result.ok()) {
    return parse_points_result.status();
  }
  std::vector<Point> points = *std::move(parse_points_result);
  std::vector<Edge> edges = ComputeEdges(points);
  UnionFind uf = UnionFind(points.size());

  for (int i = 0; i < 1000; i++) {
    Edge e = edges[i];
    uf.Union(e.u, e.v);
  }
  std::vector<int64_t> sizes;
  for (int64_t id = 0; id < std::ssize(points); id++) {
    if (uf.Root(id) == id) {
      sizes.push_back(uf.size[id]);
    }
  }
  std::sort(sizes.begin(), sizes.end(), std::greater<>{});

  int64_t result = sizes[0] * sizes[1] * sizes[2];

  // answer: 80446
  LOG(INFO) << result;

  return absl::OkStatus();
}

absl::Status PartTwo(std::vector<std::string> lines) {
  absl::StatusOr<std::vector<Point>> parse_points_result = ParsePoints(lines);
  if (!parse_points_result.ok()) {
    return parse_points_result.status();
  }
  std::vector<Point> points = *std::move(parse_points_result);
  std::vector<Edge> edges = ComputeEdges(points);
  UnionFind uf = UnionFind(points.size());

  int64_t result;
  for (const auto& e : edges) {
    uf.Union(e.u, e.v);
    if (uf.num_components == 1) {
      result = points[e.u].x * points[e.v].x;
      break;
    }
  }

  // answer: 51294528
  LOG(INFO) << result;

  return absl::OkStatus();
}

}  // namespace day08
