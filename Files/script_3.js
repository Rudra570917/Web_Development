arr=[['make', 'Ford'], ['model', 'Mustang'], ['year', 1964]]
function fun(arr){

 var obj={}
for (i=0, i<arr.length; i++;){
   let newarr=arr[i]
    obj[newarr[0]]=newarr[1]

}
return obj
}
console.log(fun(arr))
