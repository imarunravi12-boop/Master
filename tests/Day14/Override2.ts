import { parent } from "./Overide1";

class child extends parent{

    phone(){
        console.log("smart phone")
        // get the parent class method -> refer your parent class with super keyword
        super.phone()
    }

}

let c=new child()
c.phone()