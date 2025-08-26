export default function createInt8TypedArray(length, position, value) {
// Créer le buffer
const buffer = new ArrayBuffer(length);
// Créer la DataView
const view = new DataView(buffer);
// Vérifier la position
if (position >= length) {
    throw new Error('Position outside range')
}
// Ecrire la valeur 
view.setInt8(position, value);
return view

}