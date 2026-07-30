import { test } from '@playwright/test';

test('upload the file with Input tag and Type is file', async ({ page }) => {

await page.goto("https://www.leafground.com/file.xhtml");
await page.locator("//span[text()='Choose']/following::input[1]").first()
.setInputFiles("utils/Selenium Bdd Interview Qa.pdf");

await page.waitForTimeout(3000);

});

// Handle with event listener (for non input tag)

test('upload the file with non input tag', async ({ page }) => {
await page.goto("https://www.leafground.com/file.xhtml");

// create promise
const fileup = page.waitForEvent('filechooser');
// do the action
await page.locator("//span[text()='Choose']/following-sibling::input").first().click();

// resolve the promise
const Upload = await fileup;
await Upload.setFiles("utils/Selenium Bdd Interview Qa.pdf");

});