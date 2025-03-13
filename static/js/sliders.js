let my_image_slider = new Swiper('.image-slider', {
    // Стрелки
    navigation: {
        nextEl: '.car-slider-right',
        prevEl: '.car-slider-left'
    },
    // Навигация
    // Буллемы, мекущее положение, прогрессбар
    pagination: {
        el: '.swiper-pagination',
        //! Буллеты
        /*
        type: 'bullets',
        clickable: true,
        // Динамические буллеты
        dynamicBullets: true,
        */
        //! Фракция
        /*
        type: 'fraction',
        // Кастомный вывод фракции
        renderFraction: function (currentClass, totalClass) {
            return 'Photo <span class="' + currentClass + '"></span>' + 
            ' of ' + 
            '<span class="' + totalClass + '"></span>';
        }
        */
        //! Прогрессбар
        type: 'progressbar',
    },
    scrollbar: {
        el: '.swiper-scrollbar',
        // Возможность перетаскивать скролл
        draggable: true
    },

    //! Включение/отключение
    // перетаскивание на ПК
    stimulateTouch: true,
    // чувствтельность свайпа
    touchRation: 1,
    // угол срабатывания свайпа/перетаскивания
    touchAngle: 45,
    // курсор перетаскивания
    grabCursor: true,

    // Переключение при клике на слайд
    slideToClickedSlide: true,

    // Навигация по хешу
    hashNavigation: {
        // Отслеживать состояние
        watchState: true,
    },

    // Управление клавиатурой
    keyboard: {
        // Включить/выключить
        enabled: true,
        // Включить/выключить в пределах вюпорта
        onlyInViewport: true,
        // Включить/выключить клавишами pageUp, pageDown
        pageUpDown: true,
    },

    // Управление колесом мыши
    // mousewheel: {
    //     // Чувствительность колеса мыши
    //     sensitivity: 1,
    //     // Класс на котором будет срабатывать прокрутка
    //     // eventsTarget: ".image-slider",
    // },

    // Автовысота
    autoHeight: false,

    // Количество слайдов для показа
    slidesPerView: 1,

    // Отступ между слайдами
    spaceBetween: 30,

    // Количество пролистываемых слайдов
    slidesPerGroup: 1,

    // Активный слайд по центру
    centeredSlides: true,

    // Стартовый слайд
    initialSlide: 0,

    // Мультирядность
    slidesPerColumn: 1,

    // Бесконечный слайдер
    loop: false,

    // Кол-во дублирующих слайдов
    loopedSlides: 1,

    // Свободный режим
    freeMode: false,

    // Автопрокрутка
    // autoplay: {
    //     // Пауза между прокрумкой
    //     delay: 2000,
    //     // Закончить на последнем слайде
    //     stopOnLastSlide: true,
    //     // Отключить после ручного переключения
    //     disableOnIteraction: false,
    // },

    //? Скорость
    speed: 500,

    //? Направление
    direction: 'horizontal',

    //! Эффекты
    //? Листание
    effect: 'slide',

    //? Смена прозрачности
    // effect: 'fade',

    // Дополнительные параметры fade
    fadeEffect: {
        // Параллельная смена прозрачгости
        crossFade: true,
    },

    //? Переворот
    // effect: 'flip',

    // Дополнительные параметры flip
    flipEffect: {
        // Тень
        slideShadows: true,
        // Показ только активного слайда
        limitRotation: true,
    },

    //? Куб
    // effect: 'cube',

    // Дополнительные параметры cube
    cubeEffect: {
        // Настройка тени
        slideShadows: true,
        shadow: true,
        shadowOffset: 20,
        shadowScale: 0.94,
    },

    //? Поток
    // effect: 'coverflow',

    // Дополнительные параметры coverflow
    coverflowEffect: {
        // Угол
        rotate: 20,
        // Наложение
        stretch: 50,
        // Тень
        slideShadows: true,
    },

    //? Адаптивность
    // Ширина экрана
    breakpoints: {
        320: {
            slidesPerView: 1,
        },
        480: {
            // slidesPerView: 2,
        },
        992: {
            // slidesPerView: 3,
        },
    },

    // Отключение предзагрузки картинок
    // preloadImages: false,
    // // Lazy loading
    // lazy: {
    //     // Подгрузка картинок на старте переключения слайда 
    //     loadOnTransitionStart: false,
    //     // Подгрузить преведущую и следующую картинку
    //     loadPrevNext: true,
    // },
    // // Слежка за видымыми слайдами
    // watchSlidesProgress: true,
    // // Добавление класса видымым слайдам
    // watchSlidesVisibility: true,

    // Зум картинок
    zoom: {
        // Максимальное увелечение
        maxRatio: 5,
        // Минимальное увелечение
        minRatio: 1,
    },

    // thumbs: {
    //     // Свайпер с миниатюрами
    //     swiper: {
    //         el: '.image-mini-slider',
    //         slidesPerView: 5,
    //     }
    // },

    // Настройки для слайдера внутри табов
    observe: true, 
    observeParents: true, 
    observeSlideChildren: true,

    // Динамический слайдер
    // virtual: {
    //     slides: (function () {
    //         let slides = []
    //         for (let i = 0; i < 20; i++) {
    //             slides.push(`<div class="image-slider__text">Slide #i</div>`)
    //         }
    //     })
    // },

});

let sliderBlock = document.querySelector('.image-slider');

if (sliderBlock != null) {
    sliderBlock.addEventListener('mouseenter', function () {
        // my_image_slider.params.autoplay.disableOnInteraction = false;
        // my_image_slider.params.autoplay.delay = 3000;
        // my_image_slider.autoplay.start()
    })
    
    sliderBlock.addEventListener('mouseleave', function () {
        // my_image_slider.autoplay.stop()
    })
}


let my_equipment_slider = new Swiper('.equipment-slider', {
    // Стрелки
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    // Навигация
    // Буллемы, мекущее положение, прогрессбар
    pagination: {
        el: '.swiper-pagination',
        //! Буллеты
        /*
        type: 'bullets',
        clickable: true,
        // Динамические буллеты
        dynamicBullets: true,
        */
        //! Фракция
        /*
        type: 'fraction',
        // Кастомный вывод фракции
        renderFraction: function (currentClass, totalClass) {
            return 'Photo <span class="' + currentClass + '"></span>' + 
            ' of ' + 
            '<span class="' + totalClass + '"></span>';
        }
        */
        //! Прогрессбар
        type: 'progressbar',
    },
    scrollbar: {
        el: '.swiper-scrollbar',
        // Возможность перетаскивать скролл
        draggable: true
    },

    //! Включение/отключение
    // перетаскивание на ПК
    stimulateTouch: true,
    // чувствтельность свайпа
    touchRation: 1,
    // угол срабатывания свайпа/перетаскивания
    touchAngle: 45,
    // курсор перетаскивания
    grabCursor: true,

    // Переключение при клике на слайд
    slideToClickedSlide: true,

    // Навигация по хешу
    hashNavigation: {
        // Отслеживать состояние
        watchState: true,
    },

    // Управление клавиатурой
    keyboard: {
        // Включить/выключить
        enabled: true,
        // Включить/выключить в пределах вюпорта
        onlyInViewport: true,
        // Включить/выключить клавишами pageUp, pageDown
        pageUpDown: true,
    },

    // Управление колесом мыши
    // mousewheel: {
    //     // Чувствительность колеса мыши
    //     sensitivity: 1,
    //     // Класс на котором будет срабатывать прокрутка
    //     // eventsTarget: ".image-slider",
    // },

    // Автовысота
    autoHeight: false,

    // Количество слайдов для показа
    slidesPerView: 2.5,

    // Отступ между слайдами
    spaceBetween: 20,

    // Количество пролистываемых слайдов
    slidesPerGroup: 1,

    // Активный слайд по центру
    centeredSlides: true,

    // Стартовый слайд
    initialSlide: 0,

    // Мультирядность
    slidesPerColumn: 1,

    // Бесконечный слайдер
    loop: false,

    // Кол-во дублирующих слайдов
    loopedSlides: 1,

    // Свободный режим
    freeMode: false,

    // Автопрокрутка
    // autoplay: {
    //     // Пауза между прокрумкой
    //     delay: 2000,
    //     // Закончить на последнем слайде
    //     stopOnLastSlide: true,
    //     // Отключить после ручного переключения
    //     disableOnIteraction: false,
    // },

    //? Скорость
    speed: 500,

    //? Направление
    direction: 'horizontal',

    //! Эффекты
    //? Листание
    effect: 'slide',

    //? Смена прозрачности
    // effect: 'fade',

    // Дополнительные параметры fade
    fadeEffect: {
        // Параллельная смена прозрачгости
        crossFade: true,
    },

    //? Переворот
    // effect: 'flip',

    // Дополнительные параметры flip
    flipEffect: {
        // Тень
        slideShadows: true,
        // Показ только активного слайда
        limitRotation: true,
    },

    //? Куб
    // effect: 'cube',

    // Дополнительные параметры cube
    cubeEffect: {
        // Настройка тени
        slideShadows: true,
        shadow: true,
        shadowOffset: 20,
        shadowScale: 0.94,
    },

    //? Поток
    // effect: 'coverflow',

    // Дополнительные параметры coverflow
    coverflowEffect: {
        // Угол
        rotate: 20,
        // Наложение
        stretch: 50,
        // Тень
        slideShadows: true,
    },

    //? Адаптивность
    // Ширина экрана
    // breakpoints: {
    //     320: {
    //         slidesPerView: 1,
    //     },
    //     480: {
    //         // slidesPerView: 2,
    //     },
    //     992: {
    //         // slidesPerView: 3,
    //     },
    // },

    // Отключение предзагрузки картинок
    // preloadImages: false,
    // // Lazy loading
    // lazy: {
    //     // Подгрузка картинок на старте переключения слайда 
    //     loadOnTransitionStart: false,
    //     // Подгрузить преведущую и следующую картинку
    //     loadPrevNext: true,
    // },
    // // Слежка за видымыми слайдами
    // watchSlidesProgress: true,
    // // Добавление класса видымым слайдам
    // watchSlidesVisibility: true,

    // Зум картинок
    // zoom: {
    //     // Максимальное увелечение
    //     maxRatio: 5,
    //     // Минимальное увелечение
    //     minRatio: 1,
    // },

    // thumbs: {
    //     // Свайпер с миниатюрами
    //     swiper: {
    //         el: '.image-mini-slider',
    //         slidesPerView: 5,
    //     }
    // },

    // Настройки для слайдера внутри табов
    observe: true, 
    observeParents: true, 
    observeSlideChildren: true,

    // Динамический слайдер
    // virtual: {
    //     slides: (function () {
    //         let slides = []
    //         for (let i = 0; i < 20; i++) {
    //             slides.push(`<div class="image-slider__text">Slide #i</div>`)
    //         }
    //     })
    // },

});

let equipment_sliderBlock = document.querySelector('.equipment-slider');

if (equipment_sliderBlock != null) {
    equipment_sliderBlock.addEventListener('mouseenter', function () {
        // my_image_slider.params.autoplay.disableOnInteraction = false;
        // my_image_slider.params.autoplay.delay = 3000;
        // my_image_slider.autoplay.start()
    })
    
    equipment_sliderBlock.addEventListener('mouseleave', function () {
        // my_image_slider.autoplay.stop()
    })
}
