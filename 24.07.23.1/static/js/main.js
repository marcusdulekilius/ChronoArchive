document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('chat-form');
    var inputField = document.getElementById('soru');
    var slider = document.getElementById('themeSlider');

    inputField.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            form.submit();
        }
    });

    slider.addEventListener('change', function() {
        if (slider.checked) {
            document.body.classList.remove('light-theme');
            document.body.classList.add('dark-theme');
        } else {
            document.body.classList.remove('dark-theme');
            document.body.classList.add('light-theme');
        }
    });

    // Modal özellikleri
    var loginLink = document.getElementById('loginLink');
    var modal = document.getElementById('loginModal');
    var close = document.getElementsByClassName('close')[0];

    loginLink.onclick = function() {
        modal.style.display = 'block';
    }

    close.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    }
});
