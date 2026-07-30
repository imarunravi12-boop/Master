// download the file even listener
import test from '@playwright/test';

test('Download the file with event listener', async ({ page }) => {
  
    await page.goto("https://www.leafground.com/file.xhtml");

// create promise
const down=page.waitForEvent('download');

// do the action
await page.locator("//span[normalize-space()='Download']").click();

// resolve the promise
const fileDownload = await down;

// set the path where should you download
await fileDownload.saveAs('downloads/'+fileDownload.suggestedFilename());

});