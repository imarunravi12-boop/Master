// Var - 1995
// Let - 2015 - (ECMAScript 6)
// Const - 2015 - (ECMAScript 6)

// var - will do re-declaration and re-assignment
var Employeename = "ArunKumar"
Employeename=true // re-assignment
console.log(Employeename)

var Employeecode = 12
var Employeecode = 28 // re-declaration
console.log(Employeecode)
var Employeecode = 45
console.log(Employeecode)

// let - will do re-assignment but not re-declaration
let fruitname = "Apple"
fruitname = "Mango" // re-assignment
console.log(fruitname)
// re-declaration not allowed
// let fruitname = "Banana" // ❌ not allowed (re-declaration)
// console.log(fruitname)

// const - will not do re-assignment and re-declaration also block scope
const num = 100
num = 200
console.log(num) // ❌ not allowed (re-assignment)
