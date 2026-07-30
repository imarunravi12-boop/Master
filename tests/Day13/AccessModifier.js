var Access = /** @class */ (function () {
    function Access() {
    }
    // public access modifier - default access modifier
    // private access modifier - can be accessed only within the class
    // protected access modifier - can be accessed within the class and its subclasses
    Access.prototype.loadurl = function () {
        console.log("Loading URL");
    };
    Access.prototype.Loadusername = function () {
        console.log("Loading Username");
    };
    Access.prototype.Loadpassword = function () {
        console.log("Loading Password");
    };
    return Access;
}());
var access = new Access();
access.loadurl();
// acc.Loadusername(); // Error: Property 'Loadusername' is private and only accessible within class 'Access'.
// acc.Loadpassword(); // Error: Property 'Loadpassword' is protected and only accessible within class 'Access'.
