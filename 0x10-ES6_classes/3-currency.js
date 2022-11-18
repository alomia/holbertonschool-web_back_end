export default class Currency {
  constructor(code, name) {
    if (typeof code != 'string') throw TypeError('Code must be a string');
    if (typeof name != 'string') throw TypeError('Name must be a string');

    this._code = code;
    this._name = name;
  }

  /* getter code */
  get getCode() {
    return this._code;
  }

  /* setter code */
  set setCode(code) {
    if (typeof code != 'string') throw TypeError('Code must be a string');
    this._code = code;
  }

  /* getter name */
  get getName() {
    return this._name;
  }

  /* setter name */
  set setName(name) {
    if (typeof name != 'string') throw TypeError('Name must be a string');
    this._name = name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
