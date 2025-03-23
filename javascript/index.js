console.log("hello world")
// js variables 
var num=34;
num=11;
var num1="manan";
console.log(num+num1);

// data types in js
//int
var num=34;
//string
var str='varun';
//objects
var marks ={
    ravi:99,
    shunbham:90,
    manan:100
}
console.log(marks);
//bool
var a =true

/* there are 2 types of dt
1. primitive dt undefined,null,number,string,boolean,symbol
2. reference dt arrays and objects
 */

//array
var arr=[1,2,3,4]

//operators
//arithmetic operators
var a1=34
var b1=56
console.log("value of 2 number is :",a1+b1)
console.log("value of 2 number is :",a1-b1)
console.log("value of 2 number is :",a1/b1)
console.log("value of 2 number is :",a1*b1)

//assignment operators

var c=b1
console.log(c)

//comparison operators
console.log(c>=a1)
console.log(c<=a1)
console.log(c==b1)

//logical operators

//and

console.log(true && true)
console.log(true && false)
console.log(false && true)
console.log(false && false)

//or

console.log(true || true)
console.log(true || false)
console.log(false || true)
console.log(false || false)

//not

console.log(!true)
console.log(!false)

//functions

function avg(a,b) {
    return(a+b)/2
    
}
c1=avg(4,6)
c2=avg(14,16)
console.log(c1)
console.log(c2)

//conditionals in js

var age = 21
if (age >=32) {
    console.log("you are not a kid ")
    
}else if(age >=21){
    console.log("you are good to go ")
    
}
else{
    console.log("you are a kid")
}


var arr =[1,2,3,4,5,6,7,8,9]

// for(let i = 0; i < arr.length; i++){
//     console.log(arr[i])
// }

// arr.forEach(function(element){
//     console.log(element)
// })

let j=0
while (j<arr.length) {
    console.log(arr[j])
    j++
    
}


