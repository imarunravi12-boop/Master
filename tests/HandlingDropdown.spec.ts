import { test} from '@playwright/test'

test('handling dropdown', async ({ page }) => {

    await page.goto ("https://leafground.com/select.xhtml")

//SelectOption()

    await page.selectOption('.ui-selectonemenu', { label: 'Playwright' })
    await page.waitForTimeout(1000)


})

test('handling dropdown with non select option', async ({ page }) => {
    await page.goto('https://leafground.com/select.xhtml')

    await page.locator('#j_idt87\\:country_label').click()
    await page.locator('#j_idt87\\:country_3').click()
    await page.waitForTimeout(1000)

})