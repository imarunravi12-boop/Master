import { Page }  from '@playwright/test';


export class LoginPage{

    page:Page
    //empty user define variable which of the type page{PW}
    //Variable:Interface{PW}
    constructor(page:Page){
        this.page=page
    }

async Loadurl(){
    await this.page.goto("http://leaftaps.com/opentaps/control/login")
}

async enterUsername(){
    await this.page.fill("#username", "Demosalesmanager");
}

async enterPassword(){
    await this.page.fill("#password", "crmsfa");  
}

async clickLoginButton(){                      
    await this.page.click(".decorativeSubmit"); 
}

}

