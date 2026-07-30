import test from '@playwright/test';
test ("Frame with index", async ({ page }) => {
    await page.goto ("https://leafground.com/frame.xhtml");

// count of frames in the page
const totalFrames = await page.frames();
console.log("Total frames in the page: " + totalFrames.length);
 
});