import {test} from "@playwright/test";

test("saucelabs login",async ({page}) =>{

  await page.goto("https://support.saucelabs.com/s/login/?language=en_US")
  await page.locator('//input[@placeholder="Email"]').fill("imarunravi12@gmail.com")
  await page.locator('//input[@placeholder="Password"]').fill("admin@123")
  await page.getByRole("button",{name:"login"}).click()

});