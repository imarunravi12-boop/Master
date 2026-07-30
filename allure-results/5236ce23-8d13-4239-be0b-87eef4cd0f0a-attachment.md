# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: demo-todo-app.spec.ts >> Persistence >> should persist its data
- Location: tests\demo-todo-app.spec.ts:306:7

# Error details

```
Test timeout of 30000ms exceeded.
```

```
Error: locator.check: Test timeout of 30000ms exceeded.
Call log:
  - waiting for getByTestId('todo-item').first().getByRole('checkbox')
    - locator resolved to <input class="toggle" type="checkbox" aria-label="Toggle Todo"/>
  - attempting click action
    - waiting for element to be visible, enabled and stable
    - element is visible, enabled and stable
    - scrolling into view if needed
    - done scrolling
    - performing click action

```

# Page snapshot

```yaml
- generic [ref=e1]:
  - generic [ref=e2]:
    - text: This is just a demo of TodoMVC for testing, not the
    - link "real TodoMVC app." [ref=e3] [cursor=pointer]:
      - /url: https://todomvc.com/
  - generic [ref=e5]:
    - generic [ref=e6]:
      - heading "todos" [level=1] [ref=e7]
      - textbox "What needs to be done?" [ref=e8]
    - generic [ref=e9]:
      - checkbox "❯Mark all as complete" [ref=e10]
      - generic [ref=e11]: ❯Mark all as complete
      - list [ref=e12]:
        - listitem [ref=e13]:
          - generic [ref=e14]:
            - checkbox "Toggle Todo" [active] [ref=e15]
            - generic [ref=e16]: buy some cheese
            - button "Delete" [ref=e17]: ×
        - listitem [ref=e18]:
          - generic [ref=e19]:
            - checkbox "Toggle Todo" [ref=e20]
            - generic [ref=e21]: feed the cat
            - text: ×
    - generic [ref=e22]:
      - generic [ref=e23]:
        - strong [ref=e24]: "2"
        - text: items left
      - list [ref=e25]:
        - listitem [ref=e26]:
          - link "All" [ref=e27] [cursor=pointer]:
            - /url: "#/"
        - listitem [ref=e28]:
          - link "Active" [ref=e29] [cursor=pointer]:
            - /url: "#/active"
        - listitem [ref=e30]:
          - link "Completed" [ref=e31] [cursor=pointer]:
            - /url: "#/completed"
  - contentinfo [ref=e32]:
    - paragraph [ref=e33]: Double-click to edit a todo
    - paragraph [ref=e34]:
      - text: Created by
      - link "Remo H. Jansen" [ref=e35] [cursor=pointer]:
        - /url: http://github.com/remojansen/
    - paragraph [ref=e36]:
      - text: Part of
      - link "TodoMVC" [ref=e37] [cursor=pointer]:
        - /url: http://todomvc.com
```

# Test source

```ts
  217 |       TODO_ITEMS[0],
  218 |       'buy some sausages',
  219 |       TODO_ITEMS[2],
  220 |     ]);
  221 |     await checkTodosInLocalStorage(page, 'buy some sausages');
  222 |   });
  223 | 
  224 |   test('should trim entered text', async ({ page }) => {
  225 |     const todoItems = page.getByTestId('todo-item');
  226 |     await todoItems.nth(1).dblclick();
  227 |     await todoItems.nth(1).getByRole('textbox', { name: 'Edit' }).fill('    buy some sausages    ');
  228 |     await todoItems.nth(1).getByRole('textbox', { name: 'Edit' }).press('Enter');
  229 | 
  230 |     await expect(todoItems).toHaveText([
  231 |       TODO_ITEMS[0],
  232 |       'buy some sausages',
  233 |       TODO_ITEMS[2],
  234 |     ]);
  235 |     await checkTodosInLocalStorage(page, 'buy some sausages');
  236 |   });
  237 | 
  238 |   test('should remove the item if an empty text string was entered', async ({ page }) => {
  239 |     const todoItems = page.getByTestId('todo-item');
  240 |     await todoItems.nth(1).dblclick();
  241 |     await todoItems.nth(1).getByRole('textbox', { name: 'Edit' }).fill('');
  242 |     await todoItems.nth(1).getByRole('textbox', { name: 'Edit' }).press('Enter');
  243 | 
  244 |     await expect(todoItems).toHaveText([
  245 |       TODO_ITEMS[0],
  246 |       TODO_ITEMS[2],
  247 |     ]);
  248 |   });
  249 | 
  250 |   test('should cancel edits on escape', async ({ page }) => {
  251 |     const todoItems = page.getByTestId('todo-item');
  252 |     await todoItems.nth(1).dblclick();
  253 |     await todoItems.nth(1).getByRole('textbox', { name: 'Edit' }).fill('buy some sausages');
  254 |     await todoItems.nth(1).getByRole('textbox', { name: 'Edit' }).press('Escape');
  255 |     await expect(todoItems).toHaveText(TODO_ITEMS);
  256 |   });
  257 | });
  258 | 
  259 | test.describe('Counter', () => {
  260 |   test('should display the current number of todo items', async ({ page }) => {
  261 |     // create a new todo locator
  262 |     const newTodo = page.getByPlaceholder('What needs to be done?');
  263 |     
  264 |     // create a todo count locator
  265 |     const todoCount = page.getByTestId('todo-count')
  266 | 
  267 |     await newTodo.fill(TODO_ITEMS[0]);
  268 |     await newTodo.press('Enter');
  269 | 
  270 |     await expect(todoCount).toContainText('1');
  271 | 
  272 |     await newTodo.fill(TODO_ITEMS[1]);
  273 |     await newTodo.press('Enter');
  274 |     await expect(todoCount).toContainText('2');
  275 | 
  276 |     await checkNumberOfTodosInLocalStorage(page, 2);
  277 |   });
  278 | });
  279 | 
  280 | test.describe('Clear completed button', () => {
  281 |   test.beforeEach(async ({ page }) => {
  282 |     await createDefaultTodos(page);
  283 |   });
  284 | 
  285 |   test('should display the correct text', async ({ page }) => {
  286 |     await page.locator('.todo-list li .toggle').first().check();
  287 |     await expect(page.getByRole('button', { name: 'Clear completed' })).toBeVisible();
  288 |   });
  289 | 
  290 |   test('should remove completed items when clicked', async ({ page }) => {
  291 |     const todoItems = page.getByTestId('todo-item');
  292 |     await todoItems.nth(1).getByRole('checkbox').check();
  293 |     await page.getByRole('button', { name: 'Clear completed' }).click();
  294 |     await expect(todoItems).toHaveCount(2);
  295 |     await expect(todoItems).toHaveText([TODO_ITEMS[0], TODO_ITEMS[2]]);
  296 |   });
  297 | 
  298 |   test('should be hidden when there are no items that are completed', async ({ page }) => {
  299 |     await page.locator('.todo-list li .toggle').first().check();
  300 |     await page.getByRole('button', { name: 'Clear completed' }).click();
  301 |     await expect(page.getByRole('button', { name: 'Clear completed' })).toBeHidden();
  302 |   });
  303 | });
  304 | 
  305 | test.describe('Persistence', () => {
  306 |   test('should persist its data', async ({ page }) => {
  307 |     // create a new todo locator
  308 |     const newTodo = page.getByPlaceholder('What needs to be done?');
  309 | 
  310 |     for (const item of TODO_ITEMS.slice(0, 2)) {
  311 |       await newTodo.fill(item);
  312 |       await newTodo.press('Enter');
  313 |     }
  314 | 
  315 |     const todoItems = page.getByTestId('todo-item');
  316 |     const firstTodoCheck = todoItems.nth(0).getByRole('checkbox');
> 317 |     await firstTodoCheck.check();
      |                          ^ Error: locator.check: Test timeout of 30000ms exceeded.
  318 |     await expect(todoItems).toHaveText([TODO_ITEMS[0], TODO_ITEMS[1]]);
  319 |     await expect(firstTodoCheck).toBeChecked();
  320 |     await expect(todoItems).toHaveClass(['completed', '']);
  321 | 
  322 |     // Ensure there is 1 completed item.
  323 |     await checkNumberOfCompletedTodosInLocalStorage(page, 1);
  324 | 
  325 |     // Now reload.
  326 |     await page.reload();
  327 |     await expect(todoItems).toHaveText([TODO_ITEMS[0], TODO_ITEMS[1]]);
  328 |     await expect(firstTodoCheck).toBeChecked();
  329 |     await expect(todoItems).toHaveClass(['completed', '']);
  330 |   });
  331 | });
  332 | 
  333 | test.describe('Routing', () => {
  334 |   test.beforeEach(async ({ page }) => {
  335 |     await createDefaultTodos(page);
  336 |     // make sure the app had a chance to save updated todos in storage
  337 |     // before navigating to a new view, otherwise the items can get lost :(
  338 |     // in some frameworks like Durandal
  339 |     await checkTodosInLocalStorage(page, TODO_ITEMS[0]);
  340 |   });
  341 | 
  342 |   test('should allow me to display active items', async ({ page }) => {
  343 |     const todoItem = page.getByTestId('todo-item');
  344 |     await page.getByTestId('todo-item').nth(1).getByRole('checkbox').check();
  345 | 
  346 |     await checkNumberOfCompletedTodosInLocalStorage(page, 1);
  347 |     await page.getByRole('link', { name: 'Active' }).click();
  348 |     await expect(todoItem).toHaveCount(2);
  349 |     await expect(todoItem).toHaveText([TODO_ITEMS[0], TODO_ITEMS[2]]);
  350 |   });
  351 | 
  352 |   test('should respect the back button', async ({ page }) => {
  353 |     const todoItem = page.getByTestId('todo-item'); 
  354 |     await page.getByTestId('todo-item').nth(1).getByRole('checkbox').check();
  355 | 
  356 |     await checkNumberOfCompletedTodosInLocalStorage(page, 1);
  357 | 
  358 |     await test.step('Showing all items', async () => {
  359 |       await page.getByRole('link', { name: 'All' }).click();
  360 |       await expect(todoItem).toHaveCount(3);
  361 |     });
  362 | 
  363 |     await test.step('Showing active items', async () => {
  364 |       await page.getByRole('link', { name: 'Active' }).click();
  365 |     });
  366 | 
  367 |     await test.step('Showing completed items', async () => {
  368 |       await page.getByRole('link', { name: 'Completed' }).click();
  369 |     });
  370 | 
  371 |     await expect(todoItem).toHaveCount(1);
  372 |     await page.goBack();
  373 |     await expect(todoItem).toHaveCount(2);
  374 |     await page.goBack();
  375 |     await expect(todoItem).toHaveCount(3);
  376 |   });
  377 | 
  378 |   test('should allow me to display completed items', async ({ page }) => {
  379 |     await page.getByTestId('todo-item').nth(1).getByRole('checkbox').check();
  380 |     await checkNumberOfCompletedTodosInLocalStorage(page, 1);
  381 |     await page.getByRole('link', { name: 'Completed' }).click();
  382 |     await expect(page.getByTestId('todo-item')).toHaveCount(1);
  383 |   });
  384 | 
  385 |   test('should allow me to display all items', async ({ page }) => {
  386 |     await page.getByTestId('todo-item').nth(1).getByRole('checkbox').check();
  387 |     await checkNumberOfCompletedTodosInLocalStorage(page, 1);
  388 |     await page.getByRole('link', { name: 'Active' }).click();
  389 |     await page.getByRole('link', { name: 'Completed' }).click();
  390 |     await page.getByRole('link', { name: 'All' }).click();
  391 |     await expect(page.getByTestId('todo-item')).toHaveCount(3);
  392 |   });
  393 | 
  394 |   test('should highlight the currently applied filter', async ({ page }) => {
  395 |     await expect(page.getByRole('link', { name: 'All' })).toHaveClass('selected');
  396 |     
  397 |     //create locators for active and completed links
  398 |     const activeLink = page.getByRole('link', { name: 'Active' });
  399 |     const completedLink = page.getByRole('link', { name: 'Completed' });
  400 |     await activeLink.click();
  401 | 
  402 |     // Page change - active items.
  403 |     await expect(activeLink).toHaveClass('selected');
  404 |     await completedLink.click();
  405 | 
  406 |     // Page change - completed items.
  407 |     await expect(completedLink).toHaveClass('selected');
  408 |   });
  409 | });
  410 | 
  411 | async function createDefaultTodos(page: Page) {
  412 |   // create a new todo locator
  413 |   const newTodo = page.getByPlaceholder('What needs to be done?');
  414 | 
  415 |   for (const item of TODO_ITEMS) {
  416 |     await newTodo.fill(item);
  417 |     await newTodo.press('Enter');
```