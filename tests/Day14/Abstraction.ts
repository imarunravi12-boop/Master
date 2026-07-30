export {}

abstract class method{

// 0 to 100 %  abstract method
// both abstract and non abstract method

// non abstract method and normal method 
loadUrl():void{
    console.log("Loading URL");
}

// abstract method
abstract loginInfo(): void;

}

class Testcase extends method{
    loginInfo(): void {
        console.log("Login info entered");
    }
    
lanuchBrowser(): void {
    console.log("Lanuching Browser")
}

}

let t1=new Testcase();
t1.lanuchBrowser();
t1.loadUrl();
t1.loginInfo()
