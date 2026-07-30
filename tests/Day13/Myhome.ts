import { Loginpage } from './Login';


// login page is parent class
// home page is child class
export class myHomepage extends Loginpage{
clickOnCrmsfa(){
    console.log("Click on crmsfa link");
}    

}

let home = new myHomepage();
home.loadurl();
home.enterusername();
home.enterpassword();
home.clickOnLogin();
home.clickOnCrmsfa();