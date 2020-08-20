$(function(){
    $('a').each(function(){
        if ($(this).prop('href') == window.location.href) {
            $(this).addClass('current-page'); $(this).parents('li').addClass('current-page');
        }
    });
});

function toggleCodeDiv(){
    var codeDiv = document.getElementById('codeDiv');
    if(codeDiv.style.display == 'block'){
        codeDiv.style.display = 'none';
        document.getElementById('toggleCodeIcon').classList.remove('fa-angle-double-up');
        document.getElementById('toggleCodeIcon').classList.add('fa-angle-double-down');
        document.getElementById('toggleCodeText').innerText = 'Show me the code';
    }else{
        codeDiv.style.display = 'block';
        document.getElementById('toggleCodeIcon').classList.remove('fa-angle-double-down');
        document.getElementById('toggleCodeIcon').classList.add('fa-angle-double-up');
        document.getElementById('toggleCodeText').innerText = 'Minimize';
    }
}