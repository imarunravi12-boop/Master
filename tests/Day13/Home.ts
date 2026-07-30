import { myHomepage } from "./Myhome";

//grantparent - login page
//parent - Myhome page
//child - Home page
class HomePage extends myHomepage{

clickOnLeads(){
    console.log("Clicked on Leads");
}    

}
let home = new HomePage();
home.loadurl();
home.enterusername();
home.enterpassword();
home.clickOnLogin();
home.clickOnCrmsfa();
home.clickOnLeads();