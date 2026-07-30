import {test} from '@playwright/test';

test("alert handling",async ({page})=>{
    await page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.on("dialog",async(dialog) =>{
        console.log(dialog.message())
        dialog.accept()
    });

    await page.getByRole("button",{name:"Click for JS Alert"}).click();

});


test("dropdown handling",async({page})=>{
    await page.goto("https://the-internet.herokuapp.com/dropdown")
    await page.locator('//select[@id="dropdown"]').selectOption("1")
    await page.waitForTimeout(2000);

});


