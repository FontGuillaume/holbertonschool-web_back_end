export default function appendToEachArrayValue(array, appendString) {
  const Result = [];
  for (const value of array) {
  const newValue = appendString + value;
  Result.push(newValue);
  }
return Result;
  

}
