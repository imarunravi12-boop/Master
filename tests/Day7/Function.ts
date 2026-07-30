function goto(url: string,timeout:number,wait:string){
    console.log(`${url}, ${timeout}, ${wait}`);
}

// Example calls to the `goto` function (invoke after the function to avoid recursion)
goto("google", 5000, "load");
goto("facebook", 5000, "networkidle");

export {};