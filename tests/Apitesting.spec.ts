import {test,expect} from '@playwright/test';

test("Api testing", async ({request}) => {
    await request.get("https://jsonplaceholder.typicode.com/posts/1")


});