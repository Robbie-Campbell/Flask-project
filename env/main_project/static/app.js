let last_known_scroll_position = 0;
let ticking = false;

function doSomething(scroll_pos) {
    if (scroll_pos > 150)
    {
        document.body.style.backgroundImage = "url('https://cdn.hipwallpaper.com/i/47/48/CVZrNI.jpeg')";
    }
    else
    {
        document.body.style.backgroundImage = "url('https://i.pinimg.com/originals/cb/10/9d/cb109d5d1402ae804422a89aa168da00.jpg')";
    }
}

window.addEventListener('scroll', function(e) {
  last_known_scroll_position = window.scrollY;

  if (!ticking) {
    window.requestAnimationFrame(function() {
      doSomething(last_known_scroll_position);
      ticking = false;
    });

    ticking = true;
  }
});