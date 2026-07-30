import { test } from '@playwright/test';

test("Load Url", async ({ page }) => {
    await page.goto("https://www.amazon.in/")    
});

// Skipped Test
test.skip("Skipped Test", async ({ page }) => {
    await page.goto("https://www.flipkart.com/")
});

// Failing Test
test.fail("Expected to Fail Test", async ({ page }) => {
    await page.goto("https://www.meesho.com/")
});

// Test marked as Blocked
test.fixme("The testcase is blocked a bug", async ({ page }) => {
    await page.goto("https://www.snapdeal.com/")
    await page.locator("#inputValEnter").fill("Shoes")
    await page.locator("button").click()
});

// Test with additional info in the report
test.only("Adding some additional info to the test report", async ({ page }) => {
    test.info().annotations.push({ type: 'bug', description: 'Bug in the application' });
    
    // Capture screenshot and attach to report
    test.info().attach('screenshot', {
        body: await page.screenshot(),
        contentType: 'image/png',
    });
    
    // Navigate after capturing screenshot
    await page.goto("https://www.amazon.in/")
    await page.waitForTimeout(2000);
});