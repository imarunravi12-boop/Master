import test from '@playwright/test'

test ( 'login test', async ( { page } ) => {
    await page.goto ( 'http://leaftaps.com/opentaps/control/login' )
    await page.locator ( '#username').fill ('demosalesmanager' )

    //.frist().nth(0) .last()
    await page.locator(".inputLogin").last().fill('crmsfa')

    await page.locator ( '.decorativeSubmit' ).click ( )
    const title = await page.title ( )
    console.log ( title )

})