const fs = require('fs').promises;

const countStudents = (path) => fs.readFile(path, 'utf8')
  .then((data) => {
    const students = data.split('\n')
      .slice(1)
      .map(line => line.trim())
      .filter(line => line)
      .map(line => line.split(','))
      .filter(parts => parts.length >= 4);

    console.log(`Number of students: ${students.length}`);

    const fields = students.reduce((acc, parts) => {
      const [firstname, , , field] = parts.map(part => part.trim());
      return { ...acc, [field]: [...(acc[field] || []), firstname] };
    }, {});

    Object.entries(fields)
      .forEach(([field, names]) => 
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`)
      );
  })
  .catch(() => Promise.reject(new Error('Cannot load the database')));

module.exports = countStudents;
