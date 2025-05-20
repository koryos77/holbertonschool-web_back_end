const fs = require('fs');


function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf-8');
        const lines = data.trim().split('\n').filter(line => line.trim() !== '');
        const students = lines.slice(1).map(line => {
            const [firstname, , , field] = line.split(',')
            return  { firstname, field };
        }).filter(student => student.firstname && student.field);

        console.log(`Number of students: ${students.length}`);

        const fields = {};
        students.forEach(student => {
            if (!fields[student.field]) {
                fields[student.field] = [];
            }
            fields[student.field].push(student.firstname);
        });

        for (const field in fields) {
            if (Object.prototype.hashOwnProperty.call(fields, field)) {
                console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
            }
        }
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
