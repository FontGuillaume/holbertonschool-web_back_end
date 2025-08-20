import ClassRoom from './0-classroom.js';

export default initializeRooms;

function initializeRooms() {
  return [new ClassRoom(19), new ClassRoom(20), new ClassRoom(34)];
}
