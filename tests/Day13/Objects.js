"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var Class_1 = require("./Class");
var obj = new Class_1.Browser("firefox", 20);
console.log(obj.browserVersion);
obj.launchbrowser();
