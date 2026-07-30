import test from '@playwright/test'


test("Handle Multiple Window",async({page,context})=>{


await page.goto("https://www.leafground.com/window.xhtml")


//create Promise
const [mulWindow]=await Promise.all([


    //action
    context.waitForEvent('page'),
 page.locator("//span[text()='Open Multiple']").click()
])


//[window -> parent ,c1,c2,c3,c4.....]
//count of windows is open
const count=mulWindow.context().pages()
console.log(count.length)


//title -> Best away to handle multiple window
let dashBroad:any
let webTable:any 


for(let i=0;i<count.length;i++){
const title=await count[i].title()
console.log(title)
await page.waitForTimeout(2000)


if(title==='Web Table'){
    //resolve the promise
  webTable=count[i]  
}else if(title==='Dashboard'){
    dashBroad=count[i]
}


}

// Fallback: if webTable not found by title, use the second window
if (!webTable && count.length > 1) {
    webTable = count[1];
}

// Use webTable only if it's defined
if (webTable) {
    // Wait for the page to load and locator to be ready
    await webTable.waitForLoadState('load');
    await webTable.locator("//input[@id='form:j_idt89:globalFilter']").fill("India", { timeout: 10000 })
}
//await dashBoard.locator("//input[@id='form:j_idt89:globalFilter']").fill("India")


//await page.bringToFront()

await page.bringToFront()
await page.waitForTimeout(2000)



})