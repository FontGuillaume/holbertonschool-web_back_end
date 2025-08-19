export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // Variables are not overwritten in this block
  }

  return [task, task2];
}
