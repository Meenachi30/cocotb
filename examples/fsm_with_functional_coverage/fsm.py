# SPDX-License-Identifier: CC0-1.0
# Cocotb testbench for FSM with functional coverage using VSC

import cocotb
from cocotb.triggers import RisingEdge, FallingEdge, Timer
import random
import vsc

# VSC functional coverage setup
@vsc.covergroup
class fsm_covergroup(object):
    def __init__(self):
        self.with_sample(
            x_val=vsc.bit_t(1),
        )
        self.X_COV = vsc.coverpoint(self.x_val)

cov = fsm_covergroup()

# Clock generator
async def clock_gen(clk):
    while True:
        clk.value = 0
        await Timer(5, units="ns")
        clk.value = 1
        await Timer(5, units="ns")

@cocotb.test()
async def fsm_basic_test(dut):
    """Basic FSM test with reset and a simple input sequence."""

    cocotb.start_soon(clock_gen(dut.clk))

    dut.rst.value = 1
    dut.x.value = 0
    await RisingEdge(dut.clk)
    dut.rst.value = 0

    # Apply a fixed input sequence: [1,0,1,1,0]
    sequence = [1, 0, 1, 1, 0]
    for x_val in sequence:
        dut.x.value = x_val
        await RisingEdge(dut.clk)
        cov.sample(x_val)
        dut._log.info(f"x={x_val}, y={int(dut.y.value)}")

@cocotb.test()
async def fsm_random_test(dut):
    """Randomized FSM test with coverage tracking."""

    cocotb.start_soon(clock_gen(dut.clk))

    dut.rst.value = 1
    dut.x.value = 0
    await RisingEdge(dut.clk)
    dut.rst.value = 0

    for _ in range(20):
        x_val = random.randint(0, 1)
        dut.x.value = x_val
        await RisingEdge(dut.clk)
        cov.sample(x_val)
        dut._log.info(f"x={x_val}, y={int(dut.y.value)}")

    vsc.write_coverage_db("fsm_cov.xml")

