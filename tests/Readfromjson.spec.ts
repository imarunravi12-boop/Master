import { test } from "@playwright/test";

import value from '../utils/login.json'

for (let data of value){
    test(`Read Value from JSON file ${data.Tcase}`,async({page})=>{

    await page.goto('https://login.salesforce.com/?locale=in');
    await page.locator('#username').fill(data.Username);  
    await page.locator('#password').fill(data.Password);
    await page.locator('#Login').click();
    await page.waitForTimeout(5000);

});
}