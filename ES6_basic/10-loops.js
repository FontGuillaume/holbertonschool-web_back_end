export default function appendToEachArrayValue(array, appendString) {
  const newArray = [...array];
  for (const [idx, value] of newArray.entries()) {
    newArray[idx] = appendString + value;
  }
  return newArray;
}
