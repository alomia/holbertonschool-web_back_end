export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents.map((obj) => obj["grade"] = newGrades)
  // return getListStudents.filter((obj) => obj.location === city);
}
