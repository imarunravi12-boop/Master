import { wrappermethod } from "./Playwright";


export class LoginPage extends wrappermethod{

    async loadurl(url:string){
        await this.LaunchApp(url)

    }

    async logindata(username:string,password:string){
        await this.type("#username", username)    
        await this.type("#password", password)    
    }

    async LoginClick(){
        await this.click(".decorativeSubmit")
    }


}