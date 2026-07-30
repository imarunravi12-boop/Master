import path from "path";
import {parse} from 'csv-parse/sync'
import fs from 'fs'
import { test } from '@playwright/test';



//read value from CSV file-> set path where file present
const readValue=parse(fs.readFileSync(path.join(__dirname,"../../utils/Salesforce.csv")),
{columns:true, skip_empty_lines:true}
)

// for ..of 
for(let read of readValue){

test(`Read Value from CSV file ${read.username}`,async({page})=>{
    console.log (read.username);

    await page.goto('https://login.salesforce.com/?locale=in');
    await page.locator('#username').fill(read.username);  
    await page.locator('#password').fill(read.password);
    await page.locator('#Login').click();
    await page.waitForTimeout(5000);

})

}