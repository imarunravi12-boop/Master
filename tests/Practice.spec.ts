import {test} from "@playwright/test";

test("Search the google login page",async ({page})=>{
    await page.goto("https://google.com")
    await page.locator('textarea[name="q"]').fill("Automation testing");
    await page.waitForTimeout(2000)
});