`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 12.03.2025 10:28:36
// Design Name: 
// Module Name: fsm
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module fsm(y,x,clk,rst);
input x,clk,rst;
output reg y;
reg [1:0] state,nextstate;
parameter s0=2'b00,s1=2'b01,s2=2'b10,s3=2'b11;
always @(posedge clk or posedge rst)
if (rst)
state<=s0;
else 
state<=nextstate;
always@(*)
case(state)
s0:if(x)begin nextstate<=s1;y=1'b0;end
   else begin nextstate<=s0;y=1'b0;end
s1:if(x)begin nextstate<=s3;y=1'b0;end
   else begin nextstate<=s0;y=1'b1;end
s2:if(x)begin nextstate<=s2;y=1'b0;end
   else begin nextstate<=s0;y=1'b1;end
s3:if(x)begin nextstate<=s2;y=1'b0;end
   else begin nextstate<=s0;y=1'b1;end
endcase

endmodule
