"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var method = /** @class */ (function () {
    function method() {
    }
    // 0 to 100 %  abstract method
    // both abstract and non abstract method
    // non abstract method and normal method 
    method.prototype.loadUrl = function () {
        console.log("Loading URL");
    };
    return method;
}());
var Testcase = /** @class */ (function (_super) {
    __extends(Testcase, _super);
    function Testcase() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Testcase.prototype.loginInfo = function () {
        console.log("Login info entered");
    };
    Testcase.prototype.lanuchBrowser = function () {
        console.log("Lanuching Browser");
    };
    return Testcase;
}(method));
var t1 = new Testcase();
t1.lanuchBrowser();
t1.loadUrl();
t1.loginInfo();
