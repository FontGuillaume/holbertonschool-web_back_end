export default function cleanSet(set, startString) {
  if (!(set instanceof Set) || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  return Array.from(set)
    .filter((value) => typeof value === 'string' && value.startsWith(startString) && value !== startString)
    .map((value) => value.slice(startString.length))
    .join('-');
}