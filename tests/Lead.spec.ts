import { cfixture } from "./Customfixture";

cfixture("Click on the app launcher", async ({ login }) => {
  await login.click("//div[@class='slds-icon-waffle']");
});


