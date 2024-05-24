// for...in 

let person = {
    name: 'le',
    age: 20,
    weight: 88.5 
}

for(let property in person) {
    console.log(property)
    console.log(person[property])
}