import test from '@playwright/test';

test.describe('Run smoke tests', () => {
    // test.describe.configure({ mode: 'parallel' });

    // test.describe.configure({ mode: 'serial' });
    
    test.describe.configure({ mode: 'default' });

  test("Load Url", async ({ page }) => {
      await page.goto("https://www.amazon.in/")    
      await page.waitForTimeout(2000);
  });
  
  // Skipped Test
  test("Skipped Test", async ({ page }) => {
      await page.goto("https://www.flipkart.com/")
      await page.waitForTimeout(2000);
  });
  
  // Failing Test
  test("Expected to Fail Test", async ({ page }) => {
      await page.goto("https://www.meesho.com/")
      await page.waitForTimeout(2000);
  });

});