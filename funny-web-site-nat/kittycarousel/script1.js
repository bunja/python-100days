(function() {
    var memes = document.querySelectorAll("#memes img");
    // var dots = document.getElementsByClassName("dot");

    var current = 0;
    var timer;
    var animationInProgress = false;
    moveMemes();

    // for (var i = 0; i < dots.length; i++) {
    //     dots[i].addEventListener("click", function(e) {
    //         console.log("click");
    //         if (e.target.classList.contains("highlighted")) {
    //             return;
    //         }

    //         if (animationInProgress === true) {
    //             return;
    //         }
    //         clearTimeout(timer);

    //         var nextMeme = parseInt(e.target.id.replace("dot", ""));
    //         moveMemes(nextMeme);
    //     });
    // }

    document.addEventListener("transitionend", function(e) {
        if (e.target.classList.contains("offscreen-left")) {
            e.target.classList.remove("offscreen-left");
            timer = setTimeout(moveMemes, 5000);
            animationInProgress = false;
        }
    });

    function moveMemes(nextMeme) {
        animationInProgress = true;
        memes[current].classList.add("offscreen-left");
        memes[current].classList.remove("onscreen");
        // dots[current].classList.remove("highlighted");

        if (typeof nextMeme == "undefined") {
            current++;
            if (current >= memes.length) {
                current = 0;
            }
        } else {
            current = nextMeme;
        }

        memes[current].classList.add("onscreen");
        // dots[current].classList.add("highlighted");
    }
})();
