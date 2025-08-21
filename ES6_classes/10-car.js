export default class Car {
  constructor(brand, motor, color) {

    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Méthode cloneCar
  cloneCar() {
    // Utilise this.constructor pour créer une instance de la bonne classe
    return new this.constructor();
  }
}
