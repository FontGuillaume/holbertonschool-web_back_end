export default function getListStudentIds(object) {
  if (!Array.isArray(object)) {
    return [];
  }
  else 
    return object.map(student => student.id);
}