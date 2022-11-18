// Let's make some classrooms
import ClassRoom from "./0-classroom.js";

const room1 = new ClassRoom(19);
const room2 = new ClassRoom(20);
const room3 = new ClassRoom(34);

export default function initializeRooms() {
  return [room1, room2, room3];
}
