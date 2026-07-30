import test from '@playwright/test';

test ("Handle Alerts with page,on", async ({ page }) => {

    page.on('dialog', async (alertType) => {
        const type = alertType.type();
        console.log(type);

        if (type === 'alert') {
            await alertType.accept();
        } else if (type === 'confirm') {
            await alertType.accept();
        } else {
            await alertType.dismiss();
        }
    });
        await page.goto("https://www.leafground.com/alert.xhtml")
    // Handle the alert - Auto accept
    await page.locator("text=Show").nth(0).click();
});


