console.log('Welcome to Holberton School, what is your name?');
process.stdin.setEncoding('utf8');

let hasProcessed = false;

process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null && !hasProcessed) {
    hasProcessed = true;
    const name = chunk.trim();
    console.log(`Your name is: ${name}`);
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
