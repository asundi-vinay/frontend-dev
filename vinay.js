function vinayMenu() {
    const menu = document.getElementById('leftMenu');
    menu.classList.toggle('collapsed');
}

function scrn() {
    const scrnsize= window.innerWidth;
    if (scrnsize>= 992 && scrnsize <= 1600) {
        document.body.style.transform = 'scale(0.9)';
    } 
    else if (scrnsize >= 700 && scrnsize < 992) 
           {
          document.body.style.transform = 'scale(0.8)';
    } else if (scrnsize >= 600 && scrnsize< 700) 
        {
document.body.style.transform = 'scale(0.75)';
    } else if (scrnsize<= 600) 
          {
              document.body.style.transform = 'scale(0.5)';
    } else 
        {
        document.body.style.transform = '';
    }
}

window.addEventListener('resize', scrn);
window.addEventListener('load', scrn);