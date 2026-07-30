// replace - replace single oldchar with newchar in str
let info = "Test leaf"
inform = info.replace("T","B")
console.log(inform)

// replaceall - replac all oldchar with newchar in str
let data = "Test Leaf Test"
datam = data.replaceAll("Test","Best")
console.log(datam)

// substring - print value based on the index value - index 5 to 9
// index value starts with 0
let message = "HelloTestTeamChennai"
let messages = message.substring(5,9)
console.log(messages) // end index -1

// slice - expect the negative value also
let mes = "HelloTestTeamChennai"
let mess = mes.slice(-7,-5)
console.log(mess)