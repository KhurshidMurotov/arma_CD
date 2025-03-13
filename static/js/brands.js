$(document).ready(function() {

    $('.brands-section__dropdown').click(function (event) {
        $('.brand__item').toggleClass('show')
    })
    
    $('.brand__item').click(function (event) {
        if ($(this).hasClass('show')) {
            // Getting id
            id = $(this).attr('id')

            // Setting classes for brands
            $('.brand__item').removeClass('show')
            $('.brand__item').removeClass('active')
            $(this).addClass('active')

            // Filtering cars with brands
            $('.car__item').removeClass('active')
            $(`.${id}`).addClass('active')
        }
    })
})