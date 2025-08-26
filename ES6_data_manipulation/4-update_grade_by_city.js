export default function updateStudentGradeByCity(students, city, newGrades) {
    let result = students.filter(student => student.location === city);
    return result.map(student => {
        let studentGrade = "N/A";

        for (const gradeInfo of newGrades) {
            if (gradeInfo.studentId === student.id) {
                studentGrade = gradeInfo.grade;
                break;
            }
        }

    return {
            ...student,
            grade: studentGrade
        };
        
    });

}