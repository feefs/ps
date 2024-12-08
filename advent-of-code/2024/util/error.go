package util

import (
	"fmt"
	"path/filepath"
	"runtime"
	"strings"
)

type invalidStateErr struct {
	file string
	line int
	msg  string
}

func (e *invalidStateErr) Error() string {
	return fmt.Sprintf("%v:%v: invalid state error - %v", e.file, e.line, e.msg)
}

func InvalidStateError(format string, a ...any) error {
	_, file, line, _ := runtime.Caller(1)
	return &invalidStateErr{
		file: strings.TrimPrefix(file, filepath.Dir(file)+"/"),
		line: line,
		msg:  fmt.Sprintf(format, a...),
	}
}
