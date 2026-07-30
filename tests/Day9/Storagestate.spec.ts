import test from '@playwright/test';

test('Storage State example', async ({page}) => {

await page.goto('https://login.salesforce.com/?locale=in');
await page.locator('#username').fill('dilipkumar.rajendran@testleaf.com');  
await page.locator('#password').fill('Testleaf@2025');
await page.locator('#Login').click();
await page.waitForTimeout(5000);



// storage state -> json file format
await page.context().storageState({ path: "utils/storageState.json" });

});


