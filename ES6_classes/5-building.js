export default class Building {
    constructor(sqft) {
        if (typeof sqft !== 'number')
          throw new TypeError('Sqft must be a number');
    
    this._sqft = sqft;
}
get sqft() {
    
}
}