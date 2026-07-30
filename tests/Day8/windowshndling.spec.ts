import { test, chromium } from '@playwright/test';

test("multiple context single browser", async () => {

  const browser = await chromium.launch({ channel: 'chromium' });
  const context = await browser.newContext();

  const page = await context.newPage();
  const page1 = await context.newPage();

  await page.goto("https://google.com");
  console.log(await page.title());
  await page.waitForTimeout(3000);

  await page1.goto("https://facebook.com");
  console.log(await page1.title());
  await page.waitForTimeout(3000);

  await browser.close();
});


test("handle single window", async ({ page,context }) => {
    await page.goto ("https://www.amazon.in/");
    const data = page.locator('#twotabsearchtextbox')
    await data.fill("phones");
    await data.press('Enter');


    await page.locator('//span[text()="Apple iPhone 14 Pro Max (256 GB) - Gold"]').first().click();

// create promise
// perform action
// resolve promise

// step1
  const promise = context.waitForEvent('page');
  // step2
    await page.locator('//span[text()="Apple iPhone 14 Pro Max (256 GB) - Gold"]').first().click();
    // step3
    const childPage = await promise;

    await page.waitForTimeout(3000);
    console.log(await childPage.title());
});
