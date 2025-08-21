import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    // Appeler le constructeur parent avec sqft
    super(sqft);
    
    // Validation pour floors
    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    
    // Stocker floors dans _floors
    this._floors = floors;
  }

  // Getter pour floors
  get floors() {
    return this._floors;
  }

  // Override de la méthode evacuationWarningMessage
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
