$(function(){
    $('a').each(function(){
        if ($(this).prop('href') == window.location.href) {
            //get the name of the page, and add 'active' class to it
            $(this).addClass('active'); 
            //Add this class...
            $(this).parents('li').addClass('current-nav');
        }
    });
});

function toggleCodeDiv(){
    var codeDiv = document.getElementById('codeDiv');
    if(codeDiv.style.display == 'block'){
        codeDiv.style.display = 'none';
        $('#toggleCodeIcon').removeClass('fa-angle-double-up');
        $('#toggleCodeIcon').addClass('fa-angle-double-down');
        $('#toggleCodeText').html('Show me the code');
    }else{
        codeDiv.style.display = 'block';
        $('#toggleCodeIcon').removeClass('fa-angle-double-down');
        $('#toggleCodeIcon').addClass('fa-angle-double-up');
        $('#toggleCodeText').html('Minimize');
        codeDiv.scrollIntoView({behavior: 'smooth'});
    }
}