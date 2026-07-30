import path from 'path';
import { parse } from 'csv-parse/sync';
import fs from 'fs';
import test from '@playwright/test';

type SalesForceRow = { username: string; [key: string]: string };

const csvPath = path.join(__dirname, '../utils/salesforce.csv');
const csvText = fs.readFileSync(csvPath, 'utf-8');
const readValue: SalesForceRow[] = parse(csvText, {
  columns: true,
  skip_empty_lines: true,
});

for (const read of readValue) {
  test(`Read Value from CSV file ${read.username}`, async ({ page }) => {
    console.log(read.username);
  });
}