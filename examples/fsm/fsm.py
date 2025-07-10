import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock

@cocotb.test()
async def fsm_test_basic(dut):
    """Test FSM with a simple sequence"""

    # Start clock
    clock = Clock(dut.clk, 10, units="ns")  # 100 MHz
    cocotb.start_soon(clock.start())

    # Reset
    dut.rst.value = 1
    dut.x.value = 0
    await RisingEdge(dut.clk)
    dut.rst.value = 0

    # Define a sequence of inputs
    inputs = [0, 1, 0, 1, 1, 0, 0, 1, 0]
    for val in inputs:
        dut.x.value = val
        await RisingEdge(dut.clk)
        await Timer(1, units="ns")
        dut._log.info(f"x={val} -> y={dut.y.value} state={dut.state.value.binstr}")
