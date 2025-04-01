export default function cleanSet(set, startString) {
  const values = [...set]
    .filter((value) => typeof value === 'string' && value.startsWith(startString))
    .map((value) => value.slice(startString.length));
  return values.join('-');
}
