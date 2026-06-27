const array = [0, 1, 2, -10, 3, 4, 1333, 5, 6, 7, 8, 9, 10];
let largest = array[0];
let smallest = array[0];
for (let num of array) {
  if (num < smallest) smallest = num;
  if (num > largest) largest = num;
}

console.log(largest);

console.log(smallest);

const array2 = [0, 40, 60, 20, 10, 30, 50, 70, 80, 90, 100];

console.log(array2.push(55, 65, 75, 85, 95));
console.log(array2.pop());
console.log(array2.sort((a, b) => a - b));
