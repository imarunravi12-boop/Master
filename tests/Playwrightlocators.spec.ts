import test from '@playwright/test';

test (' Playwright locators', async ({page})=> {
    await page.goto ("https://parabank.parasoft.com/parabank/index.htm")

// get By Text Locator    
    await page.getByText('Admin Page').click()
    await page.waitForTimeout(2000);

});

