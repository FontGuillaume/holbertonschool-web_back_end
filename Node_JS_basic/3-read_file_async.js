const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split('\n').map(line => line.trim()).filter(line => line);
      const students = lines.slice(1);
      console.log(`Number of students: ${students.length}`);

      // Regroupement par filière
      const fields = students.reduce((acc, line) => {
        const [firstname, , , field] = line.split(',');
        if (!acc[field]) acc[field] = [];
        acc[field].push(firstname);
        return acc;
      }, {});

      Object.entries(fields).forEach(([field, names]) => {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      });
    })
    .catch(() => Promise.reject(new Error('Cannot load the database')));
}

module.exports = countStudents;
