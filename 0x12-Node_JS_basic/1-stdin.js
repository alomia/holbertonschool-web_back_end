const process = require("process");

let name;

console.log("Welcome to Holberton School, what is your name?");

process.stdin.on('data', (name) => {
  console.log(`Your name is: Bob ${name}`);
});
