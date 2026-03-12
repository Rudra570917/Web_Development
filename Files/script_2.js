myObj = {

    "name" : "John",

    "age" : 30,

    "cars" : [

                { "name" : "Ford",  "models":[ "Fiesta", "Focus", "Mustang" ] },

                { "name" : "BMW", "models" : [ "320", "X3", "X5" ] },

                { "name" : "Fiat", "models" : [ "500", "Panda" ] }

  ] }
  statement=myObj.name+" "+"has"+" "+myObj.cars[1].name+"-"+myObj.cars[1].models[1]+" "+"at the age of"+" "+myObj.age+" "+"in web browser"
  console.log(statement)