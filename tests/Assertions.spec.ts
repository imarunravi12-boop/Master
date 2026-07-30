import {test,expect} from "@playwright/test";  

test('Verify disabled input field', async ({page})=> {

    await page.goto ("https://www.leafground.com/input.xhtml");
    // Assertion - expect (element is enabled on the page)
    await expect(page.getByPlaceholder('Babu Manickam')).toBeEnabled();

});


