var msg1 = { payload: 0 };
var msg2 = { payload: 0 };
var msg3 = { payload: 0 };
var msg4 = { payload: 0 };
var msg5 = { payload: 0 };
var msg6 = { payload: 0 };
if (msg.payload === "forward") {
   msg1.payload = 1;
   msg2.payload = 1;
   msg4.payload = 1;
   msg5.payload = 1;
}
else if (msg.payload === "left") {
   msg1.payload = 1;
   msg2.payload = 1;
}
else if (msg.payload === "right") {
   msg4.payload = 1;
   msg5.payload = 1;
}
else if (msg.payload === "reverse") {
   msg1.payload = 1;
   msg3.payload = 1;
   msg4.payload = 1;
   msg6.payload = 1;
}
return [msg1, msg2, msg3, msg4, msg5, msg6];
