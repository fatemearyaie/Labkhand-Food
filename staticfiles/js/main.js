(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });
    
    
    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";
    
    $(window).on("load resize", function() {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(
            function() {
                const $this = $(this);
                $this.addClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "true");
                $this.find($dropdownMenu).addClass(showClass);
            },
            function() {
                const $this = $(this);
                $this.removeClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "false");
                $this.find($dropdownMenu).removeClass(showClass);
            }
            );
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });


    // Modal Video
    $(document).ready(function () {
        var $videoSrc;
        $('.btn-play').click(function () {
            $videoSrc = $(this).data("src");
        });
        console.log($videoSrc);

        $('#videoModal').on('shown.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0");
        })

        $('#videoModal').on('hide.bs.modal', function (e) {
            $("#video").attr('src', $videoSrc);
        })
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav : false,
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });
    
})(jQuery);

document.querySelectorAll('.nav-item a').forEach(link => {
    link.addEventListener('click', function() {
        document.querySelectorAll('.nav-item a').forEach(l => l.classList.remove('active')); // حذف کلاس active از همه لینک‌ها
        this.classList.add('active'); // اضافه کردن کلاس active به لینک انتخاب شده
    });
});
// کد Ajax برای اضافه کردن محصول به سبد خرید
$(document).on('click', '.add-to-cart-button', function(e) {
    e.preventDefault(); // جلوگیری از رفتار پیش‌فرض لینک
    var foodId = $(this).data('food-id'); // فرض بر این است که id غذا به عنوان داده ذخیره شده است
    var quantity = $('#quantity-' + foodId).val(); // مقدار quantity را دریافت کنید

    $.ajax({
        url: '/add_to_cart/' + foodId + '/', // URL درست را وارد کنید
        type: 'POST',
        data: JSON.stringify({ 'quantity': quantity }), // داده‌ها را به فرمت JSON ارسال کنید
        contentType: 'application/json', // نوع محتوا را تعیین کنید
        headers: {
            'X-CSRFToken': getCookie('csrftoken') // توکن CSRF را دریافت کنید
        },
        success: function(response) {
            // عملیات موفق
            console.log(response);
        },
        error: function(xhr, status, error) {
            // خطا در عملیات
            console.error(xhr.responseText);
        }
    });
});

// تابع برای دریافت توکن CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
