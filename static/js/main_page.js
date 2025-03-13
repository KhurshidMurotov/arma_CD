$(document).ready(function() {
    
    $('.play-video').click(function (event) {
        $('#video-popup').addClass('open')
    })

    $('.popup__close').click(function (event) {
        $('#video-popup').removeClass('open')
    })
    
    $('.popup__area').click(function (event) {
        $('#video-popup').removeClass('open')
    })

    $('.submit-review-form').click(function (event) {
        
        // Input values
        var review_name = $('#review_name').val()
        var review_phone_number = $('#review_phone_number').val()
        var review_model_id = $('#review_model_id').val()
        var review_time = $('#review_time').val()

        if (review_name != '' && review_phone_number != '' && review_model_id != '' && review_time != '') {
            $('#review_form').submit()
        }
        if (review_name == '') {
            $('#review_name').addClass('danger')
            $('#review_name').removeClass('success')
        } else {
            $('#review_name').addClass('success')
            $('#review_name').removeClass('danger')
        }
        if (review_phone_number == '') {
            $('#review_phone_number').addClass('danger')
            $('#review_phone_number').removeClass('success')
        } else {
            $('#review_phone_number').addClass('success')
            $('#review_phone_number').removeClass('danger')
        }
        if (review_model_id == '') {
            $('#review_model_id').addClass('danger')
            $('#review_model_id').removeClass('success')
        } else {
            $('#review_model_id').addClass('success')
            $('#review_model_id').removeClass('danger')
        }
        if (review_time == '') {
            $('#review_time').addClass('danger')
            $('#review_time').removeClass('success')
        } else {
            $('#review_time').addClass('success')
            $('#review_time').removeClass('danger')
        }

    })

    $('.mobile-banner-section__burger-btn').click(function (event) {
        $(this).toggleClass('active')
        $('.mobile-banner-section__sidebar').toggleClass('active')
    })

    $('.mobile-banner-section__header').click(function (event) {
        $('.mobile-banner-section__burger-btn').removeClass('active')
        $('.mobile-banner-section__sidebar').removeClass('active')
    })
    
    $('.mobile-banner-section__content').click(function (event) {
        $('.mobile-banner-section__burger-btn').removeClass('active')
        $('.mobile-banner-section__sidebar').removeClass('active')
    })

    $(window).bind('hashchange', function() {
        hash_name = window.location.hash
        $('.content__data').removeClass('active')
        $(`${hash_name}`).addClass('active')
    });
    
})