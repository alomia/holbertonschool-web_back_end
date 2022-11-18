export default class Currency {
  constructor(code, name) {
    if (typeof code != 'string') throw TypeError('Code must be a string');
    if (typeof name != 'string') throw TypeError('Name must be a string');

    this._code = code;
    this._name = name;
  }
  
  get getCode() {
    return this._code;
  }

  set setCode(code) {
    if (typeof code != 'string') throw TypeError('Code must be a string');
    this._code = code;
  }

  get getName() {
    return this._name;
  }

  set setName(name) {
    if (typeof name != 'string') throw TypeError('Name must be a string');
    this._name = name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
