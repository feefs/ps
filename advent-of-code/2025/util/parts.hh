#pragma once

#include "absl/status/status.h"

namespace util {

using Part = absl::Status (*)(std::vector<std::string> lines);

absl::Status RunPart(Part p);

}  // namespace util
