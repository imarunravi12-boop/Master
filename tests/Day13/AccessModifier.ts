class Access {

// public access modifier - default access modifier
// private access modifier - can be accessed only within the class
// protected access modifier - can be accessed within the class and its subclasses

public loadurl(){
    console.log("Loading URL");
}

private Loadusername(){
    console.log("Loading Username");
}

protected Loadpassword(){
    console.log("Loading Password");}

}

let access = new Access();
access.loadurl();
// acc.Loadusername(); // Error: Property 'Loadusername' is private and only accessible within class 'Access'.
// acc.Loadpassword(); // Error: Property 'Loadpassword' is protected and only accessible within class 'Access'.