import test from "@playwright/test";


test.beforeAll("Read the value from json",() => {
  console.log("Read the value from json")
});

test.beforeEach("Use storage state",() => {
  console.log("Use storage state")
});

test.afterAll("Take Screehshot",() => {
  console.log("Take Screehshot")
});


test.afterEach("Close DB connection",() => {
  console.log("Close DB Connection")
});


test("Login Page ",() => {
  console.log("Login Page")
});


test("Create Lead ",() => {
  console.log("create Lead")
});

test("Create file ",() => {
  console.log("create file")
});

