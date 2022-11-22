export default function getListStudentIds(arrObjct) {
  let idsList = [];

  if (typeof arrObjct == 'object') {
    arrObjct.map((obj) => {
      idsList.push(obj['id']);
    });
  }

  return idsList;
}
