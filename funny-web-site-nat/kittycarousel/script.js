(function() {
    var kitties = document.querySelectorAll("#kitties img");
    var dots = document.getElementsByClassName("dot");
    var current = 0;
    var timer;

    var animationInProgress;
    moveKitties();
    // clicking on dots
    for (var i = 0; i < dots.length; i++) {
        dots[i].addEventListener("click", function(e) {
            // console.log("dot was clicked");
            if(e.target.classList.contains('highlighted')){
                return;
            }
            if(animationInProgress){
                return;
            }
            clearTimeout(timer);
        var nextKitty = e.target.id.replace('dot','')
        moveKitties(nextKitty);
        //     // console.log(e.target.id.replace("dot", ""));
        //     for (var i = 0; i < dots.length; i++) {
        //         if (dots[i] == e.target) {
        //             console.log(i);
        //             break;
        //         }
        //     }
        // });
        // dots[i].addEventListener("click", getClickHandler(i));
    }
    // function getClickHandler(i) {
    //     return function(e) {
    //         console.log(i);
    //     };
    // }
    // [].forEach.call(dots,function(item, index){
    //     console.log(index);
    // })

    // console.log([].slice.call(dots)); quick way to convert array like object to an array
    // [].slice.call(dots).forEach(function(item, index){
    //     item.addEventListener('click',function(e) {
    //         console.log(index);
    //     })
    // })
    //  the best event delegation
    // check if the transition that ended is the one i need
    document.addEventListener("transitionend", function(e) {
        if (e.target.classList.contains("offscreen-left")) {
            e.target.classList.remove("offscreen-left");
            timer = setTimeout(moveKitties, 1000);
            // storing timeout
            animationInProgress = false;
        }
    });
    // do not do this in the moveKitties functions because it will call this many many times which causes memory overload
    timer =  setTimeout(moveKitties, 1000);
    function moveKitties(nextKitty) {
        animationInProgress = true;
        //add the offscreen-left class to  the onscreen kitty
        //remove the onscreen class from the onscreen kitty
        kitties[current].classList.add("offscreen-left");
        kitties[current].classList.remove("onscreen");
        dots[current].classList.remove("highlited");
        //figure out the next kitty
        console.log("the current kitty is" + current);

        if (typeof next == 'undefined') {
            current++;
            if (current >= kitties.length) {
                current = 0;
            }
        } else {
            current = nextKitty;
        }

        console.log("tne New current kitty is" + current);
        // add the onscreen class to the next kitty
        kitties[current].classList.add("onscreen");
        dots[current].classList.add("highlited");
        animationInProgress = false;
    }
})();
