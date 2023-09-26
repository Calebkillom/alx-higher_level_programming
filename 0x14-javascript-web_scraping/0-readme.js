#!/usr/bin/node

const fs = require('fs').promises;

async function readFile (filePath) {
  try {
    // Read the file with UTF-8 encoding
    const content = await fs.readFile(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    console.error(error);
  }
}

// Check if the correct number of command line arguments are provided
if (process.argv.length !== 3) {
  console.log('Usage: node read_file.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
readFile(filePath);
