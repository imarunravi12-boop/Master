//  Arrow function - 2015 -ES6
// normal function
function greet(name) {
    return "hello " + name
}
// Call the function
console.log(greet('Arun'))

// Arrow function
const welcome = (name) =>{
    return "Welcome " + name
}
console.log(welcome("Kumar"))

// Arrow function - single parameter and single line return
const hi = name => "Hi " + name
console.log(hi("Team"))
// Arrow function - no parameter
const thankyou = () => "Thank you"
console.log(thankyou())