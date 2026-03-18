(() => {
    const btnCloseMenu = document.querySelector('.button-close-menu');
    const btnShowMenu = document.querySelector('.button-show-menu');
    const MenuContainer = document.querySelector('.menu-container');

    const btnShowMenuVisibleClass = 'button-show-menu-visible';
    const menuHiddenClass = 'menu-hidden';

    const closeMenu = () => {
        btnShowMenu.classList.add(btnShowMenuVisibleClass);
        MenuContainer.classList.add(menuHiddenClass);
    }

    const showMenu = () => {
        btnShowMenu.classList.remove(btnShowMenuVisibleClass);
        MenuContainer.classList.remove(menuHiddenClass);
    }

    if(btnCloseMenu){
        btnCloseMenu.removeEventListener('click', closeMenu);
        btnCloseMenu.addEventListener('click', closeMenu);
    }

    if(btnShowMenu){
        btnCloseMenu.removeEventListener('click', showMenu);
        btnShowMenu.addEventListener('click', showMenu);
    }
    
})();