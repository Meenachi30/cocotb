SIM ?= verilator



TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD):$(PYTHONPATH) # Reference model



VERILOG_SOURCES = $(PWD)/fsm.v

TOPLEVEL := fsm
MODULE   := fsm
ifeq ($(SIM), verilator)
	EXTRA_ARGS += --trace-fst --trace-structs --coverage
endif

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml coverage_*.yml *.fst *.vcd coverage.dat sim_build
