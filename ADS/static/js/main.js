const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){//setTimeout its javascript function which hold off on doing something and it takes a function
    $('#message').fadeOut('slow');/// so we used jquey to grab the element with id
},3000);
