import fs from 'fs';

const readDatabase = (filePath) => new Promise ((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            reject(new Error('Cannot load the database'));
            return;
        }

        try {
            const students = data.split('\n').slice(1);
            const validStudents = students.filter((line) => line.trim() !== '');
            const fields = {};

            validStudents.forEach((line) => {
                const parts = line.split(',');
                const firstname = parts[0].trim();
                const field = parts[3].trim();

                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstname);
            });
                
            resolve (fields);

        } catch (error) {
            reject(new Error('Cannot load the database'));
        }
    });
});

export default readDatabase;

        