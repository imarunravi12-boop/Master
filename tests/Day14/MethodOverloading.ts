class Resuablemethods{

ElementClick(Locator:string):void
ElementClick(Locator:string,timeout:number):void

ElementClick(Locator:string,timeout?:number):void{

if(timeout){
    console.log('Add time')
}
else{
    console.log('Enter the username')
}    

  
}

}


let rm=new Resuablemethods()
rm.ElementClick("#username")
rm.ElementClick("#username",5000)
