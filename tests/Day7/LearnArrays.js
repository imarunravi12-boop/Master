// Arrays is collection items can store multiple values in a single variable.
// Array index starts from 0.

let fruits = ["Apple", "Banana", "Mango", "Orange"];
console.log(fruits);
console.log(fruits[1]);
console.log(fruits.length);

// Loop through an array
for(let i = 0; i < fruits.length; i++){
    console.log(fruits[i]);
}


// we can able to add the value and remove the value from an array using array methods.
// Example: push, pop, shift, unshift, slice, splice

// push and unshift - to add values to an array
fruits.push("Grapes"); // adds to the end
console.log(fruits);
fruits.unshift("Pineapple"); // adds to the beginning
console.log(fruits);

// pop and shift - to remove values from an array 
fruits.pop(); // removes from the end
console.log(fruits);
fruits.shift(); // removes from the beginning
console.log(fruits);

// for loop
// for.of loop

let num = [10, 20, 30, 40, 50];
for (let number of num){
    console.log(number);
};