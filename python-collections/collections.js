// create it
var my_colors = ["red", "yellow", "orange"]

my_colors.push("green")
my_colors[4] = "blue"

// removes item at i 
delete my_colors[3]

//removes last item
my_colors.pop()

//traverse
for (var i = 0; i < my_colors.length; i++) {
    console.log(my_colors[i])
}











// List Slices
var my_colors = ["red", "yellow", "orange"]

// 1st item you want: 1st item you DO NOT want

var primary_colors = my_colors.slice(0, 2)










// LIST COMPREHENSIONS

var my_colors = ["red", "yellow", "orange", "blue", "green"]
// build new list of colors with #less than 5 chars

var new_colors = []
for (c in my_colors) {
    if (c.length < 5) {
        new_colors.push(c)
    }
}