// Union
let deatils: string | number;
deatils = "Arun";
deatils = 27;

// Intersection

let info: string & number; 
// it will not allow because string and number are different data types
// type alias - creating custom type of data
interface Person {
    name: string;
    age: number;
    location: string;
}
interface Employee {
    empId: number;
    name: string;
    age: number;
    location: string;
}

let empdeatils: Person & Employee = {
    name: "Arun",
    age: 27,
    location: "Chennai",
    empId: 101
} 

console.log(empdeatils);

export {};





