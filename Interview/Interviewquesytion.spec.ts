import { test, expect } from "@playwright/test";
import mysql from 'mysql2/promise';


// 1. How to count 20 matching elements?
test("Count Elements",async ({page}) =>{
  await page.goto("https://url.spec.whatwg.org/#absolute-url-string")
  const count = await page.locator('//a[@data-link-type="dfn"]').count()
  console.log(count)

});

// 2. How to handle Frames (iframes)?
test('Handle iframes', async ({ page }) => {
  // Navigate to a page with iframes
  await page.goto('https://example.com');  // Add your actual URL here
  
  // Handle iframe
  const Myframe = page.frameLocator('#iframe');
  await Myframe.locator("#some-input").fill("Arun");
  await Myframe.getByRole('button', { name: "login" }).click();
});

// 3. Hybrid Method: UI Login + API Data Entry
test('Hybrid Method: UI Login + API Data Entry', async ({ page, request }) => {
  // UI Login
  await page.goto('https://example.com/login');  // Add your actual URL here
  await page.locator('#username').fill('admin');  // Replace with actual username
  await page.locator('#password').fill('admin@123');  // Replace with actual password
  await page.locator('#login-button').click();  // Replace with actual login button selector
    // API Data Entry   
    const response = await request.post('https://example.com/api/data', {  // Replace with actual API endpoint
        data: { 
            name: 'Arun',  // Replace with actual data to be sent
            age: '27'  // Replace with actual data to be sent
        }
    });
  expect(response.status()).toBe(201);
  const responseBody = await response.json();
  console.log(responseBody);
});


// 4. API CRUD Operations (GET, POST, PUT, PATCH, DELETE)
test('API CRUD Operations', async ({ request }) => {
  const API_BASE = 'https://example.com/api/data';
  let dataId = '1'; // Replace with actual ID or use from previous test

  // --- POST (Create Data) ---
  const response = await request.post(API_BASE, {
    data: { 
        name: 'Arun',
        age: '27'
    }
  });
  expect(response.status()).toBe(201);
  const responseBody = await response.json();
  console.log(responseBody);
  
  // 🔹 2. GET (Read)
  const getResponse = await request.get(`${API_BASE}/${dataId}`);

  expect(getResponse.status()).toBe(200);
  const getBody = await getResponse.json()
  console.log('GET Response:', getBody);

  // 🔹 3. PUT (Update)
  const putResponse = await request.put(`${API_BASE}/${dataId}`, {
    data: {
      name: 'Arun Kumar',
      age: 28
    }
  });

  expect(putResponse.status()).toBe(200);
  const putBody = await putResponse.json();
  console.log('PUT Response:', putBody);

  // 🔹 4. DELETE (Remove)
  const deleteResponse = await request.delete(`${API_BASE}/${dataId}`);

  expect(deleteResponse.status()).toBe(204);
  console.log('DELETE Status:', deleteResponse.status());
});

// 5. How to handle Alerts (Auto dismiss, accept, prompt and confirm)?
test("Alert handling", async ({page}) => {
  await page.goto("https://example.com")

  page.on('dialog', async (dialog) => {
    console.log(dialog.message());
    await dialog.accept();
  });
  await page.locator("#alert-btn").click()
});

// 6. Handle multiple windows and switch between them
test("multiple windows handling", async ({browser}) => {
  
  const context = await browser.newContext();

  const page1 = await context.newPage();
  const page2 = await context.newPage();
  const page3 = await context.newPage();

  await page1.goto("https://example.com")
  await page2.goto("https://example.com/login")
  await page3.goto("https://example.com/login")

  const urlFromThree = page3.url();
  await page2.goto(urlFromThree);
});

// 7. Validate iPhone search results on Amazon
test('Validate iPhone search results', async ({ page }) => {

  await page.goto('https://www.amazon.in');

  // Search
  await page.fill('#twotabsearchtextbox', 'iPhone');
  await page.click('#nav-search-submit-button');

  // Wait for results
  await page.waitForSelector('div[data-component-type="s-search-result"]');

  // Get all product titles
  const titles = await page.locator('h2 span').allTextContents();

  // Validate
  for (const title of titles) {
    const text = title.toLowerCase();

    expect(text).toContain('iphone');
  }
});


// 8. Validate Amazon search suggestions

test("Validate Amazon search suggestions", async ({ page }) => {

  await page.goto("https://www.amazon.in/");

  const searchBox = page.locator('#twotabsearchtextbox');

  await searchBox.click();
  await searchBox.fill("iphone");

  // Wait for suggestions dropdown
  const suggestions = page.locator('div[role="listbox"] >> div');

  await expect(suggestions.first()).toBeVisible();

  // Get all suggestion texts
  const suggestionTexts = await suggestions.allTextContents();

  // Validate count
  expect(suggestionTexts.length).toBeGreaterThanOrEqual(5);

  // Validate each suggestion contains 'iphone'
  for (const text of suggestionTexts) {
    expect(text.toLowerCase()).toContain("iphone");
  }
});


// 9. Login Validation - Multiple Assertions (API + UI + Storage)

test('Login Validation - Multiple Assertions', async ({ page }) => {

  await page.goto('https://example.com/login');

  // 🔹 Fill login form
  await page.fill('#username', 'arun');
  await page.fill('#password', '1234');

  // 🔹 Capture API response
  const loginResponsePromise = page.waitForResponse(resp =>
    resp.url().includes('/login') && resp.status() === 200
  );

  await page.click('#loginBtn');


  // ================================
  // ✅ 1. API Validation
  // ================================
  const loginResponse = await loginResponsePromise;
  expect(loginResponse.status()).toBe(200);

  // ================================
  // ✅ 2. UI Validation (URL)
  // ================================
  await expect(page).toHaveURL('https://example.com/dashboard');

  // ================================
  // ✅ 3. UI Validation (Element)
  // ================================
  await expect(page.locator('#dashboard')).toBeVisible();

  // ================================
  // ✅ 4. Text Validation
  // ================================
  await expect(page.locator('#welcomeMsg'))
    .toHaveText('Welcome Arun');

  // ================================
  // ✅ 5. Token Validation (Storage)
  // ================================
  const token = await page.evaluate(() => localStorage.getItem('token'));
  expect(token).not.toBeNull();

});


// 10.You are given 5 potential environment URLs, but only one is active. Once logged in, you must test a dropdown with both valid and invalid IDs and then verify that the UI data matches the backend database. How do you automate this using Playwright and TypeScript?"

test('Login with valid URL and validate dropdown with DB', async ({ page }) => {

    // Multiple URLs
    const urls = [
        'https://wrong-url1.com',
        'https://wrong-url2.com',
        'https://wrong-url3.com',
        'https://wrong-url4.com',
        'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    ];

    let validUrl = '';

    // Find Valid URL
    for (const url of urls) {

        try {

            console.log(`Checking URL: ${url}`);

            const response = await page.goto(url, {
                waitUntil: 'domcontentloaded',
                timeout: 5000
            });

            // Check response status
            if (response && response.status() === 200) {

                console.log(`Valid URL Found: ${url}`);

                validUrl = url;

                break;
            }

        } catch (error) {

            console.log(`Invalid URL: ${url}`);

        }
    }

    // Assertion
    expect(validUrl).not.toBe('');

    // Login
    await page.locator('input[name="username"]').fill('Admin');

    await page.locator('input[name="password"]').fill('admin123');

    await page.locator('button[type="submit"]').click();

    console.log('Login Successful');

    // Wait for dashboard
    await page.waitForLoadState('networkidle');

    // Example Dropdown Locator
    const dropdown = page.locator('#employee-dropdown');

    const employeeValues = ['40', '13', '25', '99'];
    const validEmployees = ['40', '25', '99'];

    // Database Connection
    const connection = await mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'password',
        database: 'employee_db'
    });

    // Loop Employee Values
    for (const employee of employeeValues) {
        console.log(`Checking Employee ID: ${employee}`);

        if (validEmployees.includes(employee)) {
            console.log(`Valid Employee: ${employee}`);

            await dropdown.selectOption(employee);
            await expect(dropdown).toHaveValue(employee);
            console.log(`Dropdown Selected: ${employee}`);

            const query = `
                SELECT employee_id
                FROM employees
                WHERE employee_id = '${employee}'
            `;

            const [rows]: any = await connection.execute(query);
            expect(rows.length).toBeGreaterThan(0);
            console.log(`Database Validation Passed: ${employee}`);
        } else {
            console.log(`Invalid Employee: ${employee}`);
            await expect(page.locator('.error-msg')).toBeVisible();
        }
    }

    await connection.end();
});