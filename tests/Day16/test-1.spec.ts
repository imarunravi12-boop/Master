import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://www.amazon.in/');
  await page.getByRole('searchbox', { name: 'Search Amazon.in' }).click();
  await page.getByRole('searchbox', { name: 'Search Amazon.in' }).fill('mob');
  await page.getByRole('searchbox', { name: 'Search Amazon.in' }).press('ArrowDown');
  await page.getByRole('button', { name: 'mobile phone under 20000' }).click();
  await page.getByLabel('REDMI 15C 5G Moonlight Blue').click();
  await page.goto('https://www.amazon.in/gp/aw/d/B0G2B39291/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=667778dc56f04aeb361fa471af2e51a0&hsa_cr_id=0&qid=1765783599&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&aref=BKdQBruqkY&ref_=sbx_s_sparkle_sbtcd_asin_0_img&pd_rd_w=NrgKz&content-id=amzn1.sym.6dfd6df7-44a2-4792-8c83-3ac8a4ba533a%3Aamzn1.sym.6dfd6df7-44a2-4792-8c83-3ac8a4ba533a&pf_rd_p=6dfd6df7-44a2-4792-8c83-3ac8a4ba533a&pf_rd_r=BWKQX8KBVT39EV00EZCP&pd_rd_wg=LJnDI&pd_rd_r=b292b0cd-92c6-44b0-a5e4-82a4fc6ba9f1&th=1');
  await page.getByRole('radio', { name: 'Midnight Black ₹12,499.00' }).click();
  await page.getByRole('link', { name: 'Report an issue with this' }).click();
  await page.getByRole('link', { name: 'log in to your account.' }).click();
  await page.locator('html').click();
});
