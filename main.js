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

document.addEventListener('DOMContentLoaded', function() {
    var menu = document.getElementById('menu');
    var menuIcon = document.querySelector('.menu-icon');
    var menuItems = menu.querySelectorAll('.menu-item');
    var isMobile = window.matchMedia("(max-width: 768px)").matches;

    menuIcon.addEventListener('click', function(event) {
        event.stopPropagation();
        toggleMenu();
    });

    // Open sesame open
    menuIcon.addEventListener('mouseenter', function() {
        if (!menu.classList.contains('visible') && !isMobile) {
            menu.classList.add('visible');
            menuIcon.classList.add('active');
        }
    });

    // Nooo don't gooo
    menuIcon.addEventListener('mouseleave', function() {
        if (!isMobile) {
            setTimeout(function() {
                if (menu.classList.contains('visible') && !menu.matches(':hover') && !menuIcon.matches(':hover')) {
                    menu.classList.remove('visible');
                    menuIcon.classList.remove('active');
                }
            }, 100);
        }
    });

    // Never leavin'
    menu.addEventListener('mouseenter', function() {
        if (!menu.classList.contains('visible') && !isMobile) {
            menu.classList.add('visible');
            menuIcon.classList.add('active');
        }
    });

    // Here 'til u go
    menuItems.forEach(function(item) {
        item.addEventListener('mouseenter', function() {
            if (!isMobile) {
                menu.classList.add('visible');
                menuIcon.classList.add('active');
            }
        });
    });

    // Closing on leaving :'(
    menu.addEventListener('mouseleave', function() {
        if (!isMobile) {
            setTimeout(function() {
                if (menu.classList.contains('visible') && !menu.matches(':hover') && !menuIcon.matches(':hover')) {
                    menu.classList.remove('visible');
                    menuIcon.classList.remove('active');
                }
            }, 100);
        }
    });

    // Touched outside, touche.
    document.addEventListener('click', function(event) {
        if (menu.classList.contains('visible') && !menu.contains(event.target) && !menuIcon.contains(event.target)) {
            toggleMenu();
        }
    });

    function toggleMenu() {
        if (menu.classList.contains('visible')) {
            menu.classList.remove('visible');
            menuIcon.classList.remove('active');
        } else {
            menu.classList.add('visible');
            menuIcon.classList.add('active');
        }
    }
});

function showLoginModal() {
    var loginModal = document.getElementById('loginModal');
    loginModal.style.display = 'block';
}

function showRegisterModal() {
    var registerModal = document.getElementById('registerModal');
    registerModal.style.display = 'block';
}

document.querySelectorAll('.close').forEach(function(element) {
    element.onclick = function() {
        this.parentElement.parentElement.style.display = 'none';
    };
});

window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
};