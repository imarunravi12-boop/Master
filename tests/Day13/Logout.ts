import { Loginpage } from "./Login";

class Logoutpage extends Loginpage{

clickonLogout(){
    console.log("click the logout link")

}

}

let lop=new Logoutpage()
lop.clickOnLogin()
lop.clickonLogout()
lop.enterpassword()
lop.enterusername()
lop.loadurl()