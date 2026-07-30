import path from 'path';
import dotenv from 'dotenv';
import test from '@playwright/test';

// set path where env file present

dotenv.config({path:"utils/QA.env" });
test('Read value from env file', async ({page}) => {

    //process.env.variable
    //process -> global object for nodejs
    //env -> environment variable
    //variable -> SF_username / SF_password
    console.log (process.env.SF_username);
    console.log (process.env.SF_password);  
    
});
