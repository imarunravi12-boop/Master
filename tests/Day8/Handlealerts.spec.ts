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

});

