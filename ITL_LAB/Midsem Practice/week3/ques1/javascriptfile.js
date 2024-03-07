$(document).ready(function(){
    
    $('table tr:even').css({"background-color": "blue"});
    $('table tr:odd').css("background-color", "pink");
    $('#btnshift').click(function(){
        $('#image').animate({"left":"500px"});
        // Assuming the input has an ID of 'colorInput'
        $('table tr:even').css("background-color", $('#color').val());
    });
});
