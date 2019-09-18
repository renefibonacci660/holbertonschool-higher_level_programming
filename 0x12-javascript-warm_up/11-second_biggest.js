#!/usr/bin/node
// Searches the second biggest integer in the list of arguments
function SecondBiggest (GivenArray) {
  let Max = GivenArray[2];
  let SecMax = GivenArray[3];

  if (GivenArray.length === 2 || GivenArray.length === 3) {
    return (0);
  }

  for (let index = 2; index < GivenArray.length; index++) {
    if (GivenArray[index] > Max) {
      SecMax = Max;
      Max = GivenArray[index];
    } else if (GivenArray[index] > SecMax && GivenArray[index] < Max) {
      SecMax = GivenArray[index];
    }
  }
  return (SecMax);
}
console.log(SecondBiggest(process.argv));
