class Browser {
    // properties
    browserName: string = "Chrome";
    browserVersion: number = 12;

    // methods
    launchbrowser() {
        console.log("Launching the browser");
    }
    // constructor
    // constructor() {
    //     console.log("This is constructor");
    // }
    constructor(bName: string, browserVersion: number) {
        // log the passed name (no need to assign properties here)
        console.log(bName);
        // access the current class properties using 'this' keyword
        console.log(this.browserVersion=browserVersion);
    }

}

export { Browser };
let obj = new Browser("Arun", 10);

// accessing properties and methods using object
console.log(obj.browserName);
// method call
obj.launchbrowser();

