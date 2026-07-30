# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: demo-todo-app.spec.ts >> Mark all as completed >> complete all checkbox should update state when items are completed / cleared
- Location: tests\demo-todo-app.spec.ts:101:7

# Error details

```
Test timeout of 30000ms exceeded.
```

```
Error: locator.check: Test timeout of 30000ms exceeded.
Call log:
  - waiting for getByLabel('Mark all as complete')
    - locator resolved to <input id="toggle-all" type="checkbox" class="toggle-all"/>
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
      - textbox "What needs to be done?" [active] [ref=e8]
    - generic [ref=e9]:
      - checkbox "❯Mark all as complete" [ref=e10]
      - generic [ref=e11]: ❯Mark all as complete
      - list [ref=e12]:
        - listitem [ref=e13]:
          - generic [ref=e14]:
            - checkbox "Toggle Todo" [ref=e15]
            - generic [ref=e16]: buy some cheese
            - text: ×
        - listitem [ref=e17]:
          - generic [ref=e18]:
            - checkbox "Toggle Todo" [ref=e19]
            - generic [ref=e20]: feed the cat
            - text: ×
        - listitem [ref=e21]:
          - generic [ref=e22]:
            - checkbox "Toggle Todo" [ref=e23]
            - generic [ref=e24]: book a doctors appointment
            - text: ×
    - generic [ref=e25]:
      - generic [ref=e26]:
        - strong [ref=e27]: "3"
        - text: items left
      - list [ref=e28]:
        - listitem [ref=e29]:
          - link "All" [ref=e30] [cursor=pointer]:
            - /url: "#/"
        - listitem [ref=e31]:
          - link "Active" [ref=e32] [cursor=pointer]:
            - /url: "#/active"
        - listitem [ref=e33]:
          - link "Completed" [ref=e34] [cursor=pointer]:
            - /url: "#/completed"
  - contentinfo [ref=e35]:
    - paragraph [ref=e36]: Double-click to edit a todo
    - paragraph [ref=e37]:
      - text: Created by
      - link "Remo H. Jansen" [ref=e38] [cursor=pointer]:
        - /url: http://github.com/remojansen/
    - paragraph [ref=e39]:
      - text: Part of
      - link "TodoMVC" [ref=e40] [cursor=pointer]:
        - /url: http://todomvc.com
```

# Test source

```ts
  3   | test.beforeEach(async ({ page }) => {
  4   |   await page.goto('https://demo.playwright.dev/todomvc');
  5   | });
  6   | 
  7   | const TODO_ITEMS = [
  8   |   'buy some cheese',
  9   |   'feed the cat',
  10  |   'book a doctors appointment'
  11  | ] as const;
  12  | 
  13  | test.describe('New Todo', () => {
  14  |   test('should allow me to add todo items', async ({ page }) => {
  15  |     // create a new todo locator
  16  |     const newTodo = page.getByPlaceholder('What needs to be done?');
  17  | 
  18  |     // Create 1st todo.
  19  |     await newTodo.fill(TODO_ITEMS[0]);
  20  |     await newTodo.press('Enter');
  21  | 
  22  |     // Make sure the list only has one todo item.
  23  |     await expect(page.getByTestId('todo-title')).toHaveText([
  24  |       TODO_ITEMS[0]
  25  |     ]);
  26  | 
  27  |     // Create 2nd todo.
  28  |     await newTodo.fill(TODO_ITEMS[1]);
  29  |     await newTodo.press('Enter');
  30  | 
  31  |     // Make sure the list now has two todo items.
  32  |     await expect(page.getByTestId('todo-title')).toHaveText([
  33  |       TODO_ITEMS[0],
  34  |       TODO_ITEMS[1]
  35  |     ]);
  36  | 
  37  |     await checkNumberOfTodosInLocalStorage(page, 2);
  38  |   });
  39  | 
  40  |   test('should clear text input field when an item is added', async ({ page }) => {
  41  |     // create a new todo locator
  42  |     const newTodo = page.getByPlaceholder('What needs to be done?');
  43  | 
  44  |     // Create one todo item.
  45  |     await newTodo.fill(TODO_ITEMS[0]);
  46  |     await newTodo.press('Enter');
  47  | 
  48  |     // Check that input is empty.
  49  |     await expect(newTodo).toBeEmpty();
  50  |     await checkNumberOfTodosInLocalStorage(page, 1);
  51  |   });
  52  | 
  53  |   test('should append new items to the bottom of the list', async ({ page }) => {
  54  |     // Create 3 items.
  55  |     await createDefaultTodos(page);
  56  | 
  57  |     // create a todo count locator
  58  |     const todoCount = page.getByTestId('todo-count')
  59  |   
  60  |     // Check test using different methods.
  61  |     await expect(page.getByText('3 items left')).toBeVisible();
  62  |     await expect(todoCount).toHaveText('3 items left');
  63  |     await expect(todoCount).toContainText('3');
  64  |     await expect(todoCount).toHaveText(/3/);
  65  | 
  66  |     // Check all items in one call.
  67  |     await expect(page.getByTestId('todo-title')).toHaveText(TODO_ITEMS);
  68  |     await checkNumberOfTodosInLocalStorage(page, 3);
  69  |   });
  70  | });
  71  | 
  72  | test.describe('Mark all as completed', () => {
  73  |   test.beforeEach(async ({ page }) => {
  74  |     await createDefaultTodos(page);
  75  |     await checkNumberOfTodosInLocalStorage(page, 3);
  76  |   });
  77  | 
  78  |   test.afterEach(async ({ page }) => {
  79  |     await checkNumberOfTodosInLocalStorage(page, 3);
  80  |   });
  81  | 
  82  |   test('should allow me to mark all items as completed', async ({ page }) => {
  83  |     // Complete all todos.
  84  |     await page.getByLabel('Mark all as complete').check();
  85  | 
  86  |     // Ensure all todos have 'completed' class.
  87  |     await expect(page.getByTestId('todo-item')).toHaveClass(['completed', 'completed', 'completed']);
  88  |     await checkNumberOfCompletedTodosInLocalStorage(page, 3);
  89  |   });
  90  | 
  91  |   test('should allow me to clear the complete state of all items', async ({ page }) => {
  92  |     const toggleAll = page.getByLabel('Mark all as complete');
  93  |     // Check and then immediately uncheck.
  94  |     await toggleAll.check();
  95  |     await toggleAll.uncheck();
  96  | 
  97  |     // Should be no completed classes.
  98  |     await expect(page.getByTestId('todo-item')).toHaveClass(['', '', '']);
  99  |   });
  100 | 
  101 |   test('complete all checkbox should update state when items are completed / cleared', async ({ page }) => {
  102 |     const toggleAll = page.getByLabel('Mark all as complete');
> 103 |     await toggleAll.check();
      |                     ^ Error: locator.check: Test timeout of 30000ms exceeded.
  104 |     await expect(toggleAll).toBeChecked();
  105 |     await checkNumberOfCompletedTodosInLocalStorage(page, 3);
  106 | 
  107 |     // Uncheck first todo.
  108 |     const firstTodo = page.getByTestId('todo-item').nth(0);
  109 |     await firstTodo.getByRole('checkbox').uncheck();
  110 | 
  111 |     // Reuse toggleAll locator and make sure its not checked.
  112 |     await expect(toggleAll).not.toBeChecked();
  113 | 
  114 |     await firstTodo.getByRole('checkbox').check();
  115 |     await checkNumberOfCompletedTodosInLocalStorage(page, 3);
  116 | 
  117 |     // Assert the toggle all is checked again.
  118 |     await expect(toggleAll).toBeChecked();
  119 |   });
  120 | });
  121 | 
  122 | test.describe('Item', () => {
  123 | 
  124 |   test('should allow me to mark items as complete', async ({ page }) => {
  125 |     // create a new todo locator
  126 |     const newTodo = page.getByPlaceholder('What needs to be done?');
  127 | 
  128 |     // Create two items.
  129 |     for (const item of TODO_ITEMS.slice(0, 2)) {
  130 |       await newTodo.fill(item);
  131 |       await newTodo.press('Enter');
  132 |     }
  133 | 
  134 |     // Check first item.
  135 |     const firstTodo = page.getByTestId('todo-item').nth(0);
  136 |     await firstTodo.getByRole('checkbox').check();
  137 |     await expect(firstTodo).toHaveClass('completed');
  138 | 
  139 |     // Check second item.
  140 |     const secondTodo = page.getByTestId('todo-item').nth(1);
  141 |     await expect(secondTodo).not.toHaveClass('completed');
  142 |     await secondTodo.getByRole('checkbox').check();
  143 | 
  144 |     // Assert completed class.
  145 |     await expect(firstTodo).toHaveClass('completed');
  146 |     await expect(secondTodo).toHaveClass('completed');
  147 |   });
  148 | 
  149 |   test('should allow me to un-mark items as complete', async ({ page }) => {
  150 |     // create a new todo locator
  151 |     const newTodo = page.getByPlaceholder('What needs to be done?');
  152 | 
  153 |     // Create two items.
  154 |     for (const item of TODO_ITEMS.slice(0, 2)) {
  155 |       await newTodo.fill(item);
  156 |       await newTodo.press('Enter');
  157 |     }
  158 | 
  159 |     const firstTodo = page.getByTestId('todo-item').nth(0);
  160 |     const secondTodo = page.getByTestId('todo-item').nth(1);
  161 |     const firstTodoCheckbox = firstTodo.getByRole('checkbox');
  162 | 
  163 |     await firstTodoCheckbox.check();
  164 |     await expect(firstTodo).toHaveClass('completed');
  165 |     await expect(secondTodo).not.toHaveClass('completed');
  166 |     await checkNumberOfCompletedTodosInLocalStorage(page, 1);
  167 | 
  168 |     await firstTodoCheckbox.uncheck();
  169 |     await expect(firstTodo).not.toHaveClass('completed');
  170 |     await expect(secondTodo).not.toHaveClass('completed');
  171 |     await checkNumberOfCompletedTodosInLocalStorage(page, 0);
  172 |   });
  173 | 
  174 |   test('should allow me to edit an item', async ({ page }) => {
  175 |     await createDefaultTodos(page);
  176 | 
  177 |     const todoItems = page.getByTestId('todo-item');
  178 |     const secondTodo = todoItems.nth(1);
  179 |     await secondTodo.dblclick();
  180 |     await expect(secondTodo.getByRole('textbox', { name: 'Edit' })).toHaveValue(TODO_ITEMS[1]);
  181 |     await secondTodo.getByRole('textbox', { name: 'Edit' }).fill('buy some sausages');
  182 |     await secondTodo.getByRole('textbox', { name: 'Edit' }).press('Enter');
  183 | 
  184 |     // Explicitly assert the new text value.
  185 |     await expect(todoItems).toHaveText([
  186 |       TODO_ITEMS[0],
  187 |       'buy some sausages',
  188 |       TODO_ITEMS[2]
  189 |     ]);
  190 |     await checkTodosInLocalStorage(page, 'buy some sausages');
  191 |   });
  192 | });
  193 | 
  194 | test.describe('Editing', () => {
  195 |   test.beforeEach(async ({ page }) => {
  196 |     await createDefaultTodos(page);
  197 |     await checkNumberOfTodosInLocalStorage(page, 3);
  198 |   });
  199 | 
  200 |   test('should hide other controls when editing', async ({ page }) => {
  201 |     const todoItem = page.getByTestId('todo-item').nth(1);
  202 |     await todoItem.dblclick();
  203 |     await expect(todoItem.getByRole('checkbox')).not.toBeVisible();
```