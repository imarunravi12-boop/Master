import { Page } from "@playwright/test";

export abstract class wrappermethod{

page:Page

constructor(page:Page){
    this.page=page
}


async type(locators:string,value:string){
    const data= this.page.locator(locators)
    await data.fill(value)

}


async click(locators:string){
    const clc= this.page.locator(locators)
    await clc.click()

}

async LaunchApp(url:string){
    await this.page.goto(url)

}








}