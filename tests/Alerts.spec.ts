// playwright handle the alerts - Auto dismiss, accept, prompt and confirm
// Cancel the alert pop up

import {test} from '@playwright/test';
test (' Alerts handling', async ({page})=> {

    await page.goto("https://www.leafground.com/alert.xhtml")
    // Handle the alert - Auto accept
    await page.locator("text=Show").nth(0).click();
    console.log(await page.title())
    await page.waitForTimeout(2000);

});


