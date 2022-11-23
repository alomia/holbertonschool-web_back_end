export default function getStudentIdsSum(array) {
  const initialValue = 0;
  return array.reduce((accumelator, currentValue) => accumelator += currentValue.id, initialValue)
}
