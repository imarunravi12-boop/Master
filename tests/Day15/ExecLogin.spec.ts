import test from "@playwright/test";
import { LoginPage } from "./Login";

test (' Login with wrapper method', async ({page})=> {

const lp = new LoginPage(page)  
await lp.LaunchApp("http://leaftaps.com/opentaps/control/login")
await lp.logindata("Demosalesmanager","crmsfa")
await lp.LoginClick()

});