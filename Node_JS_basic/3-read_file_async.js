const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split('\n');
      const students = lines.slice(1).filter(line => line.trim() !== '');
      console.log(`Number of students: ${students.length}`);
      const fields = {};
      students.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[0].trim();
        const field = parts[parts.length - 1].trim();
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      });
      Object.keys(fields).forEach((field) => {
        const list = fields[field].join(', ');
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${list}`);
      });
    })
    .catch(() => Promise.reject(new Error('Cannot load the database')));
}

module.exports = countStudents;
