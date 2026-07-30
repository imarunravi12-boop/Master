// call function 

// Simple functions
function printEmployeeName(employeeName){
    console.log(employeeName)
}

function printEmployeeID(employeeID){
    console.log(employeeID)
}

printEmployeeName("Arun Kumar")
printEmployeeID(12)

// call one function from another function using a callback
function Employee(employeeName, callback){
    console.log(employeeName)
    callback(12)
}

function Employees(employeeName, callback){
    console.log(employeeName)
    callback(True)
}
function handleEmployeeID(employeeID){
    console.log(employeeID)
}

Employee("Arun Kumar", Employees)