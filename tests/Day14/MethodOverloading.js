var Resuablemethods = /** @class */ (function () {
    function Resuablemethods() {
    }
    Resuablemethods.prototype.ElementClick = function (Locator, timeout) {
        if (timeout) {
            console.log('Add time');
        }
        else {
            console.log('Enter the username');
        }
    };
    return Resuablemethods;
}());
var rm = new Resuablemethods();
rm.ElementClick("#username");
rm.ElementClick("#username", 5000);
