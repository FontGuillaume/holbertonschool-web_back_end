console.log('Welcome to Holberton School, what is your name?');
process.stdin.setEncoding('utf8');

let hasReceivedInput = false;

process.stdin.on('data', (data) => {
  if (!hasReceivedInput) {
    hasReceivedInput = true;
    const name = data.trim();
    console.log(`Your name is: ${name}`);
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
