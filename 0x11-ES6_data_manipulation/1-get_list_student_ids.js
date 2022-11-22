export default function getListStudentIds(arrObjct) {
  if (typeof arrObjct == 'object') {
    const idsList = arrObjct.map((obj) => {
      return obj['id'];
    });

    return idsList;
  }

  return []
}
