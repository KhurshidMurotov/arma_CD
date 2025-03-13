$(document).ready(function() {

    $('.profile-section__back-btn').attr('href', document.referrer)
    $('.mobile-profile-section__back-btn').attr('href', document.referrer)
    
    $('.submit-review-form').click(function (event) {
        
        // Input values
        var review_name = $('#review_name').val()
        var review_phone_number = $('#review_phone_number').val()
        var review_time = $('#review_time').val()

        if (review_name != '' && review_phone_number != '' && review_time != '') {
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
        if (review_time == '') {
            $('#review_time').addClass('danger')
            $('#review_time').removeClass('success')
        } else {
            $('#review_time').addClass('success')
            $('#review_time').removeClass('danger')
        }

    })

    $(window).bind('hashchange', function() {
        hash_name = window.location.hash
        if (hash_name.startsWith('#equipment')) {
            $('.mobile-profile-section__equipment').removeClass('active')
            new_class = hash_name.replace('#', '')
            $(`.block-${new_class}`).addClass('active')
        }
    });

    $('.profile-section__main-side-btn').click(function (event) {
        $('.profile-section__main-side-btn').removeClass('active')
        $(this).addClass('active')
    })

    $('.mobile-profile-section__order-btn').click(function (event) {
        window.scrollTo({
        top: $('.review-section').offset().top,
        left: 0,
        behavior: 'smooth'
  })
    })

    $('.profile-section__main-body-btn').click(function (event) {
        window.scrollTo({
        top: $('.review-section').offset().top,
        left: 0,
        behavior: 'smooth'
  })
    })

})