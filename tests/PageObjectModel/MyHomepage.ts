import { wecomePage } from "./Welocome";


export class myhomePage extends wecomePage{

async clickLeads(){
    await this.page.click("//a[text()='Leads']")

} 

async clickContacts(){
    await this.page.click("//a[text()='Contacts']")

} 







}