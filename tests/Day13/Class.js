"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Browser = void 0;
var Browser = /** @class */ (function () {
    // constructor
    // constructor() {
    //     console.log("This is constructor");
    // }
    function Browser(bName, browserVersion) {
        // properties
        this.browserName = "Chrome";
        this.browserVersion = 12;
        // log the passed name (no need to assign properties here)
        console.log(bName);
        // access the current class properties using 'this' keyword
        console.log(this.browserVersion = browserVersion);
    }
    // methods
    Browser.prototype.launchbrowser = function () {
        console.log("Launching the browser");
    };
    return Browser;
}());
exports.Browser = Browser;
var obj = new Browser("Arun", 10);
// accessing properties and methods using object
console.log(obj.browserName);
// method call
obj.launchbrowser();
