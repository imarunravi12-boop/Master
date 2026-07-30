import test from '@playwright/test'
import { myhomePage } from './MyHomepage';

test("Click on Leads",async({page})=>{

const mhp=new myhomePage(page)
await mhp.Loadurl()
await mhp.enterUsername()
await mhp.enterPassword()
await mhp.clickCRMFA()
await mhp.clickLeads()
await mhp.clickContacts()
await mhp.logout()


})



