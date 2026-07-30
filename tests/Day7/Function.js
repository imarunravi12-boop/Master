"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function goto(url, timeout, wait) {
    console.log("".concat(url, ", ").concat(timeout, ", ").concat(wait));
}
// Example calls to the `goto` function (invoke after the function to avoid recursion)
goto("google", 5000, "load");
goto("facebook", 5000, "networkidle");
