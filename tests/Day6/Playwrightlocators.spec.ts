import test from '@playwright/test';

test (' Playwright locators', async ({page})=> {
    await page.goto ("https://parabank.parasoft.com/parabank/index.htm")

    await page.getByText('username').click()
    await page.getByLabel('Username:').fill('arunkumar')
    await page.getByLabel('Password:').fill('arun1234') 
    await page.getByRole('button', { name: 'Log In' }).click()




})