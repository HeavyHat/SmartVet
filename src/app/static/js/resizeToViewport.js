fitToViewport = function ()
{
    var currentViewPortHeight = $(window).height();
    var currentViewPortWidth = $(window).width();
    $("#viewport").css(
        {
            "height": currentViewPortHeight
        },
        {
            "width": currentViewPortWidth
        }
    );
}

$(window).resize(fitToViewport);
$(document).ready(fitToViewport)