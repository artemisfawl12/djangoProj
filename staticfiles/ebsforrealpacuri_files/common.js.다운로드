class GnbMenu {
    constructor(jsonUrl) {
        this.$gnbContainer = $('ul.gnb'); // 메뉴 컨테이너
        this.jsonUrl = jsonUrl;          // JSON 데이터 경로
        this.isMobile = window.matchMedia("(max-width: 1024px)").matches; // 모바일 환경 감지
        this.init();                     // 초기화
    }

    // 초기화
    init() {
        this.loadMenuData().then((menuData) => {
            this.renderMenu(menuData.menu); // 메뉴 생성
            if (!this.isMobile) {          // 모바일 환경에서는 메뉴 이벤트를 바인딩하지 않음
                this.bindMenuEvents();     // 메뉴 이벤트 설정
            }
            this.setActiveMenuByUrl();     // 현재 URL 활성화
        }).catch((error) => {
            console.error('Failed to load menu data:', error);
        });
    }

    // JSON 데이터를 로드
    loadMenuData() {
        return $.getJSON(this.jsonUrl);
    }

    // 메뉴 렌더링
    renderMenu(menuData) {
        const html = menuData.map(menu => {
            let submenuHTML = '';
            if (menu.items) {
                submenuHTML = `
                    <div class="gnb__submenu">
                        <ul class="sec-depth">
                            ${menu.items.map(sub => {
                                let thirdLevelHTML = '';
                                if (sub.items) {
                                    thirdLevelHTML = `
                                        <ul class="third-depth">
                                            ${sub.items.map(third => `
                                                <li class="third-depth__item">
                                                    <a href="${third.link}">${third.title}</a>
                                                </li>
                                            `).join('')}
                                        </ul>
                                    `;
                                }

                                const subMenuTitle = sub.items ?
                                    `<span>${sub.title}</span>` :
                                    `<a href="${sub.link}">${sub.title}</a>`;

                                return `
                                    <li class="sec-depth__item">
                                        ${subMenuTitle}
                                        ${thirdLevelHTML}
                                    </li>
                                `;
                            }).join('')}
                        </ul>
                    </div>
                `;
            }

            return `
                <li class="gnb__item">
                    <a href="${menu.link}">${menu.title}</a>
                    ${submenuHTML}
                </li>
            `;
        }).join('');

        this.$gnbContainer.html(html);
    }

    /*bindMenuEvents() {
        // 메뉴 클릭 이벤트 처리
        this.$gnbContainer.on('click', '.gnb__item > a, .sec-depth__item > a, .third-depth__item > a', (e) => {
            const $link = $(e.target);
            const $item = $link.closest('.gnb__item');
            const $submenu = $item.children('.gnb__submenu');

            // 자식 메뉴가 있을 경우 토글
            if ($submenu.length > 0 && !$link.closest('.sec-depth__item, .third-depth__item').length) {
                e.preventDefault(); // 기본 링크 이동 방지
                this.toggleMenu($item, $submenu);
            } else {
                this.closeAllMenusExceptActive();
            }
        });

        // 서브메뉴 영역에서 마우스가 벗어났을 때 서브메뉴 닫기
        this.$gnbContainer.on('mouseleave', '.gnb__submenu', (e) => {
            const $submenu = $(e.currentTarget);
            const $item = $submenu.parent('.gnb__item');

            $submenu.slideUp(200, () => this.toggleHeaderClass());
            $item.removeClass('active');
        });

        // 스크롤 이벤트 처리
        this.handleScrollEvent();
    }*/

// 신규 업데이트 정의 - 마우스를 올리면 서브메뉴 열기
    bindMenuEvents() {
        // 마우스를 올리면 서브메뉴 열기
        this.$gnbContainer.on('mouseenter', '.gnb__item', (e) => {
            const $item = $(e.currentTarget);
            const $submenu = $item.children('.gnb__submenu');
            //console.log("마우스 온 입니다이~");

            if ($submenu.length > 0) {
                this.closeAllMenusExcept($item);// 다른 메뉴 닫기
                $submenu.stop(true, true).slideDown(0);
                $item.addClass('active');
                $('header.header').addClass('on');
            }
        });

        // 마우스를 벗어나면 서브메뉴 닫기
        this.$gnbContainer.on('mouseleave', '.gnb__item', (e) => {
            const $item = $(e.currentTarget);
            const $submenu = $item.children('.gnb__submenu');
            //console.log("마우스 아웃 입니다이~");

            if ($submenu.length > 0) {
                $submenu.stop(true, true).slideUp(0, () => $item.removeClass('active'));
                $('header.header').removeClass('on');
            }
        });

        // 클릭 이벤트 (서브메뉴 없는 항목만 동작)
        this.$gnbContainer.on('click', '.gnb__item > a', (e) => {
            const $link = $(e.target);
            const $item = $link.closest('.gnb__item');
            const $submenu = $item.children('.gnb__submenu');

            if ($submenu.length > 0) {
                e.preventDefault(); // 기본 이동 방지
            } else {
                // this.closeAllMenusExceptActive();  // 삭제
                this.closeAllMenus();
            }
        });

        // 스크롤 이벤트 처리
        this.handleScrollEvent();
    }
 // 신규 업데이트 정의 - 마우스를 올리면 서브메뉴 열기
    bindMenuEvents() {
        // 마우스를 올리면 서브메뉴 열기
        this.$gnbContainer.on('mouseenter', '.gnb__item', (e) => {
            const $item = $(e.currentTarget);
            const $submenu = $item.children('.gnb__submenu');
            //console.log("마우스 온 입니다이~");

            if ($submenu.length > 0) {
                this.closeAllMenusExcept($item);// 다른 메뉴 닫기
                $submenu.stop(true, true).slideDown(0);
                $item.addClass('active');
                $('header.header').addClass('on');
            }
        });

        // 마우스를 벗어나면 서브메뉴 닫기
        this.$gnbContainer.on('mouseleave', '.gnb__item', (e) => {
            const $item = $(e.currentTarget);
            const $submenu = $item.children('.gnb__submenu');
            //console.log("마우스 아웃 입니다이~");

            if ($submenu.length > 0) {
                $submenu.stop(true, true).slideUp(0, () => $item.removeClass('active'));
                $('header.header').removeClass('on');
            }
        });

        // 클릭 이벤트 (서브메뉴 없는 항목만 동작)
        this.$gnbContainer.on('click', '.gnb__item > a', (e) => {
            const $link = $(e.target);
            const $item = $link.closest('.gnb__item');
            const $submenu = $item.children('.gnb__submenu');

            if ($submenu.length > 0) {
                e.preventDefault(); // 기본 이동 방지
            } else {
                // this.closeAllMenusExceptActive();  // 삭제
                this.closeAllMenus();
            }
        });

        // 스크롤 이벤트 처리
        this.handleScrollEvent();
    }
    // 특정 메뉴를 제외하고 모든 메뉴 닫기
    closeAllMenusExcept(activeItem) {
        this.$gnbContainer.find('.gnb__item').each((_, item) => {
            const $item = $(item);
            if (!$item.is(activeItem)) {
                $item.children('.gnb__submenu').stop(true, true).slideUp(0);
                $item.removeClass('active');
                $('header.header').removeClass('on');
            }
        });
    }

    // 모든 메뉴 닫기
    closeAllMenus() {
        this.$gnbContainer.find('.gnb__submenu').slideUp(0);
        this.$gnbContainer.find('.gnb__item').removeClass('active');
        $('header.header').removeClass('on');
    }

    handleScrollEvent() {
        $(window).on('scroll', () => {
            const scrollTop = $(window).scrollTop();

            if (scrollTop > 890) {
                $('.header-bg').addClass('bg-on'); // 스크롤이 시작되면 클래스 추가
            } else {
                $('.header-bg').removeClass('bg-on'); // 스크롤이 맨 위로 돌아오면 클래스 제거
            }
        });
    }

   /* closeAllMenusExceptActive() {
        this.$gnbContainer.find('.gnb__submenu').slideUp(200, () => this.toggleHeaderClass());
        this.$gnbContainer.find('.gnb__item').removeClass('active');

        const currentUrl = window.location.href;
        this.$gnbContainer.find('.gnb__item > a').each((_, link) => {
            const $link = $(link);
            if ($link[0].href === currentUrl) {
                $link.closest('.gnb__item').addClass('active');
                $link.parents('.gnb__submenu').show().parent().addClass('active');
            }
        });
    }*/

    setActiveMenuByUrl() {
        const currentUrl = window.location.href;

        this.$gnbContainer.find('.gnb__item > a').each((_, link) => {
            const $link = $(link);
            if ($link[0].href === currentUrl) {
                $link.closest('.gnb__item').addClass('active');
                $link.parents('.gnb__submenu').show().parent().addClass('active');
            }
        });
    }

    toggleMenu($item, $submenu) {
        const isOpen = $submenu.is(':visible');

        this.toggleHeaderClass();

        if (isOpen) {
            $submenu.removeClass('open').slideUp(200, () => this.toggleHeaderClass());
            $item.removeClass('active');
            this.setActiveMenuByUrl();
        } else {
            $item.siblings().removeClass('active').find('.gnb__submenu')
                .removeClass('open')
                .slideUp(200, () => this.toggleHeaderClass());

            $submenu.addClass('open').slideDown(200, () => this.toggleHeaderClass());
            $item.addClass('active');
        }
    }

    toggleHeaderClass() {
        setTimeout(() => {
            const hasOpenMenu = this.$gnbContainer.find('.gnb__submenu:visible').length > 0;

            if (hasOpenMenu) {
                $('header').addClass('on');
            } else {
                $('header').removeClass('on');
            }
        }, 50);
    }
}

new GnbMenu('https://kr.object.ncloudstorage.com/danchoo/web/hsc_resource/asset/data/menu.json');  // 메뉴 데이터를 로드

//mobile menu open
class mobileGnbMenu {
    constructor() {
        this.$menuOpen = $('.menu-open');
        this.$menuClose = $('.mo-gnb .close');
        this.$gnb = $('.mo-gnb');
        this.$body = $('body');
        this.$html = $('html');

        this.init();
    }
    // 초기화 함수 - 이벤트 바인딩
    init() {
        this.$menuOpen.on('click', () => this.openMenu());
        this.$menuClose.on('click', () => this.closeMenu());
    }

    // 메뉴 열기 함수
    openMenu() {
        this.$gnb.addClass('mo-gnb-open').removeClass('mo-gnb-close');
        this.$body.addClass('overflow-hidden');
    }

    // 메뉴 닫기 함수
    closeMenu() {
        this.$gnb.removeClass('mo-gnb-open').addClass('mo-gnb-close');
        this.$body.removeClass('overflow-hidden');
    }
}

new mobileGnbMenu();

// accordion
class Accordion {
    constructor(selector, options = {}) {
        this.$accordion = $(selector);
        this.type = options.type || 'single';
        this.animationMode =
            options.animationMode !== undefined ? options.animationMode : true;
        this.activeIndices = options.defaultActiveIndices || [];

        this.init();
    }

    // 초기화 함수
    init() {
        this.$accordion.on('click', '[data-js="accordion__btn"]', (event) => {
            const $item = $(event.currentTarget).closest('.accordion__item');
            const index = $item.data('index');
            this.toggleAccordion(index);
        });

        this.updateAccordion();
    }

    // 아코디언 토글 함수
    toggleAccordion(index) {
        const isActive = this.activeIndices.includes(index);

        if (this.type === 'single') {
            this.activeIndices = isActive ? [] : [index];
        } else {
            if (isActive) {
                this.activeIndices = this.activeIndices.filter(
                    (i) => i !== index,
                );
            } else {
                this.activeIndices.push(index);
            }
        }

        this.updateAccordion();
    }

    // 아코디언 상태 업데이트 함수
    updateAccordion() {
        this.$accordion.find('.accordion__item').each((_, item) => {
            const $item = $(item);
            const index = $item.data('index');
            const isOpen = this.activeIndices.includes(index);

            if (isOpen) {
                if (this.animationMode) {
                    $item.find('.accordion__panel').stop().slideDown();
                } else {
                    $item.find('.accordion__panel').show();
                }
                $item.addClass('is-active');
            } else {
                if (this.animationMode) {
                    $item.find('.accordion__panel').stop().slideUp();
                } else {
                    $item.find('.accordion__panel').hide();
                }
                $item.removeClass('is-active');
            }
        });
    }
}

// tab
class Tab {
    constructor(selector, options = {}) {
        this.$tabsContainer = $(selector);
        this.activeIndex = options.defaultActiveIndex || 0;

        this.init();
    }

    init() {
        this.$tabsContainer.on('click', '[data-js="tab__btns"]', (event) => {
            const $btn = $(event.currentTarget);
            const index = $btn.data('index');
            this.activateTab(index);
        });

        this.updateTabs();
    }

    activateTab(index) {
        if (this.activeIndex === index) return;
        this.activeIndex = index;
        this.updateTabs();
    }

    updateTabs() {
        this.$tabsContainer.find('[data-js="tab__btns"]').each((_, btn) => {
            const $btn = $(btn);
            const index = $btn.data('index');
            $btn.toggleClass('active', index === this.activeIndex);
        });

        this.$tabsContainer.find('.tab__panels__box').each((_, panel) => {
            const $panel = $(panel);
            const index = $panel.data('index');
            if (index === this.activeIndex) {
                $panel.show();
                $panel.addClass('active');
            } else {
                $panel.hide();
                $panel.removeClass('active');
            }
        });
    }
}

// 얼럿 팝업
class AlertPopup {
    constructor(options = {}) {
        this.title = options.title || '';
        this.message = options.message || '';
        this.btnFirText = options.btnFirText || null;
        this.btnSecText = options.btnSecText || null;
        this.btnFirCallback = options.btnFirCallback || (() => {});
        this.btnSecCallback = options.btnSecCallback || (() => {});

        this.$popup = $('.popWrap');
        this.$dimmed = $('.popWrap .dimd'); // Alert 전용 dimd로 설정
        this.$body = $('body');
        this.$html = $('html');

        // 팝업 내 버튼들 가져오기
        this.$btnFir = this.$popup.find('.btn__fir');
        this.$btnSec = this.$popup.find('.btn__sec');

        // 팝업이 제대로 초기화되지 않으면 경고를 출력
        if (this.$popup.length === 0) {
            console.warn('Alert popup container not found. Make sure the HTML structure is correct.');
        }
        if (this.$btnFir.length === 0) {
            console.warn('Primary button (.btn__fir) not found.');
        }
        if (this.$btnSec.length === 0) {
            console.warn('Secondary button (.btn__sec) not found.');
        }

        this.init();
    }

    init() {
        this.setTitle(this.title);
        this.setMessage(this.message);

        this.configureButton(this.$btnFir, this.btnFirText, this.btnFirCallback);
        this.configureButton(this.$btnSec, this.btnSecText, this.btnSecCallback);

        this.$popup.find('.alert__close').off('click').on('click', () => this.closePopup());

        this.$dimmed.off('click').on('click', () => this.closePopup());
    }

    setTitle(title) {
        this.$popup.find('.alert__tit').text(title);
    }

    setMessage(message) {
        const $messageElement = this.$popup.find('.alert__message');
        $messageElement.text(message);
        $messageElement.toggleClass('long', message.length > 100);
    }

    configureButton($button, text, callback) {
        if (text) { // 텍스트가 있을 때만 버튼을 설정하고 보여줍니다.
            $button.text(text).show(); // 텍스트 설정 후 버튼 표시
            $button.off('click').on('click', callback); // 클릭 이벤트 설정
        } else {
            $button.hide(); // 텍스트가 없으면 버튼 숨김
        }
    }

    showPopup() {
        this.$popup.show();
        this.$dimmed.show();
        this.$body.addClass('overflow-hidden');
    }

    closePopup() {
        this.$popup.hide();
        this.$dimmed.hide();
        this.$body.removeClass('overflow-hidden');
    }
}

// 모달 팝업
class Modal {
    constructor(modalId) {
        this.modal = document.getElementById(modalId);
        if (!this.modal) {
          //  console.error(`Modal with ID "${modalId}" not found.`);
            return;
        }

        this.overlay = this.modal.querySelector('.dimd');
        this.closeButton = this.modal.querySelector('.modal--close');

        if (this.overlay) this.overlay.addEventListener('click', () => this.close());
        if (this.closeButton) this.closeButton.addEventListener('click', () => this.close());

    }

    open() {
        if (this.modal) {
            this.modal.style.display = 'flex';
            $('body').addClass('overflow-hidden');

        }
    }

    close() {
        if (this.modal) {
            this.modal.style.display = 'none';
            $('body').removeClass('overflow-hidden');

        }
    }
}

//드롭 다운
class DropDown {
    constructor(selector) {
        this.$dropDown = $(selector);
        this.$dropDownSelect = this.$dropDown.find('[data-js="select"]');
        this.$dropDownItems = this.$dropDown.find('[data-js="item"]');
        this.$dropDownList = this.$dropDown.find('[data-js="list"]');
        this.selected = false; // 선택 여부를 추적하는 변수

        this.init();
    }

    init() {
        // 드롭다운을 클릭하면 열고 닫음
        this.$dropDownSelect.on('click', (event) => {
            const $currentDropDown = $(event.currentTarget).closest(
                '.drop-down',
            );
            this.selected = false; // 드롭다운이 열릴 때 초기화

            // 모든 드롭다운을 닫음
            $('.drop-down').not($currentDropDown).removeClass('open');

            // 현재 드롭다운을 열거나 닫음
            $currentDropDown.toggleClass('open');

            console.log('ddd');
        });

        // 리스트 항목을 클릭하면 선택 처리
        this.$dropDownItems.on('click', (event) => {
            event.stopPropagation(); // 이벤트 버블링 방지
            const $item = $(event.currentTarget);
            const selectedText = $item.text();

            this.$dropDownSelect.text(selectedText);
            this.$dropDownItems.removeClass('active');
            $item.addClass('active');
            this.$dropDown.removeClass('open');

            // 선택된 상태로 설정
            this.selected = true; // 선택된 상태로 업데이트
            this.$dropDown.removeClass('err'); // 선택 시 에러 클래스 제거
        });

        // 빈 영역 클릭 시 드롭다운 닫기
        $(document).on('click', (event) => {
            if (!$(event.target).closest('.drop-down').length) {
                $('.drop-down').removeClass('open'); // 모든 드롭다운 닫기
            }
        });
    }

    // 유효성 검사를 위한 메서드
    validate() {
        // 선택되지 않았으면 에러 클래스를 추가하고 부모 컬럼에 err 클래스 추가
        if (!this.selected) {
            this.$dropDown.addClass('err');
            this.$dropDown.closest('.input-form__col').addClass('err'); // 에러 클래스 추가
            return false; // 유효성 검사 실패
        } else {
            this.$dropDown.removeClass('err');
            this.$dropDown.closest('.input-form__col').removeClass('err'); // 에러 클래스 제거
            return true; // 유효성 검사 성공
        }
    }
}

function updateCharCount(input) {
    const currentCount = input.value.length; // 현재 입력된 문자 수
    const charCountDisplay = input.closest('.input-box').querySelector('.current-count');
    charCountDisplay.textContent = currentCount; // 카운트를 갱신
}

// 파일 첨부 변경 시 파일 이름 업데이트 및 삭제 버튼 표시
$('.file-input').on('change', function () {
    const fileName = this.files[0] ? this.files[0].name : '파일을 선택하세요';
    const fileWrap = $(this).closest('.file-wrap');
    fileWrap.find('.file-name').text(fileName);
    fileWrap.find('.btn-delete').show();
    fileWrap.find('.btn-select').prop('disabled', true);
});

// 파일 삭제 기능
$('.btn-delete').on('click', function () {
    const fileWrap = $(this).closest('.file-wrap');
    fileWrap.find('.file-input').val('');
    fileWrap.find('.file-name').text('파일을 선택하세요');
    fileWrap.find('.btn-select').prop('disabled', false);
    $(this).hide();
});



// 여러 개의 DropDown 인스턴스를 처리하기 위해 각각 초기화
const dropDownInstances = [];
$('.drop-down').each(function (index, element) {
    dropDownInstances.push(new DropDown(element));
});

// text field 삭제 버튼
class InputWithClear {
    constructor(selector) {
        this.$inputField = $(selector);
        this.$clearBtn = this.$inputField.siblings('.btn-clear');

        this.init();
    }

    init() {
        // 입력 필드에 값이 입력될 때마다 이벤트 리스너 설정
        this.$inputField.on('input', () => {
            this.toggleClearButton();
        });
        // 삭제 버튼 클릭 시 입력 필드 초기화
        this.$clearBtn.on('click', () => {
            this.clearInputField();
        });
    }

    // 입력 필드에 값이 있으면 삭제 버튼을 표시하고, 없으면 숨김
    toggleClearButton() {
        if (this.$inputField.val().trim()) {
            this.$clearBtn.show();
        } else {
            this.$clearBtn.hide();
        }
    }
    // 입력 필드를 초기화하고 삭제 버튼 숨김
    clearInputField() {
        this.$inputField.val('');
        this.$clearBtn.hide();
    }
}

$('.input-field').each(function () {
    new InputWithClear(this); // 각 input 필드에 대해 InputWithClear 클래스 생성
});

// 상단으로 가기 버튼
class GoTopButton {
    constructor(selector, scrollOffset = 100) {
        this.$button = $(selector);
        this.scrollOffset = scrollOffset;
        this.init();
    }
    // 초기화 메서드: 스크롤 및 클릭 이벤트 설정
    init() {
        $(window).on('scroll', () => this.toggleButtonVisibility());

        this.$button.on('click', () => this.scrollToTop());
    }

    toggleButtonVisibility() {
        if ($(window).scrollTop() > this.scrollOffset) {
            this.$button.fadeIn();
        } else {
            this.$button.fadeOut();
        }
    }
    // 최상단으로 스크롤하는 메서드
    scrollToTop() {
        $('html, body').animate({ scrollTop: 0 }, 'slow');
    }
}

const goTopButton = new GoTopButton('.go-top');

// stopWatch
class Stopwatch {
    constructor(element) {
        this.$element = $(element);
        this.$display = this.$element.find(".display");
        this.$startBtn = this.$element.find(".start-btn");
        this.$pauseBtn = this.$element.find(".pause-btn");
        this.$resetBtn = this.$element.find(".reset-btn");
        this.timer = null;
        this.startTime = null;
        this.elapsedTime = 0;
        this.isRunning = false;

        // 버튼 이벤트 설정
        this.$startBtn.on("click", () => this.start());
        this.$pauseBtn.on("click", () => this.pause());
        this.$resetBtn.on("click", () => this.reset());
    }

    start() {
        if (!this.isRunning) {
            this.isRunning = true;
            this.startTime = Date.now() - this.elapsedTime;
            this.timer = setInterval(() => this.updateDisplay(), 10);
        }
    }

    pause() {
        if (this.isRunning) {
            clearInterval(this.timer);
            this.elapsedTime = Date.now() - this.startTime;
            this.isRunning = false;
        }
    }

    reset() {
        clearInterval(this.timer);
        this.elapsedTime = 0;
        this.isRunning = false;
        this.updateDisplay(true);
    }

    updateDisplay(reset = false) {
        const time = reset ? 0 : Date.now() - this.startTime;
        const minutes = String(Math.floor((time / (1000 * 60)) % 60)).padStart(2, "0");
        const seconds = String(Math.floor((time / 1000) % 60)).padStart(2, "0");
        const milliseconds = String(Math.floor((time % 1000) / 10)).padStart(2, "0"); // 1/100초 표시

        this.$display.text(`${minutes}:${seconds}:${milliseconds}`);
    }
}

// jQuery로 DOM 로드 후 스톱워치 초기화
$(".stop-watch").each(function() {
    new Stopwatch(this);
});

// header toggle 체크 여부에 따라 'dark-mode' 클래스 추가 및 그래프 색상 변경
$("#toggle1, #toggle2").on("change", function() {
    const isChecked = $(this).is(":checked"); // 클릭한 토글의 상태 확인
    $("body").toggleClass("dark-mode", isChecked);

    if (isChecked) {
    	$.cookie('_skin_saved', 'style_dark', { expires: 365, path: '/' });
    } else {
    	$.cookie('_skin_saved', 'style_white', { expires: 365, path: '/' });
    }

    updateChartColors(isChecked);
});

function updateChartColors() {

};

// 툴팁 표시
$('.ico-mark').on('click', function () {
    const $tooltip = $(this).find('.tooltip-box');
    $tooltip.toggleClass('on');
});
// 툴팁 표시
$('.info').on('click', function () {
    const $tooltip = $(this).find('.tooltip-box');
    $tooltip.toggleClass('on');
});

// 툴팁 표시
$('.count-today').on('click', function () {
    const $tooltip = $(this).find('.tooltip-box');
    $tooltip.toggleClass('on');
});

// 닫기 버튼 클릭 시 툴팁 숨기기
$('.tooltip-box .close-tooltip').on('click', function (event) {
    const $tooltip = $(this).closest('.tooltip-box');
    $tooltip.removeClass('on');
    event.stopPropagation();
});

// textarea 글자 수 카운트
var textareas = document.querySelectorAll('.textarea-input');
textareas.forEach(function(textarea) {
    var current = textarea.closest('.textarea-wrap').querySelector('.textarea-count__current');

    var initialCharacterCount = textarea.value.length;
    if (current) {
        current.textContent = initialCharacterCount || '0';
    }

    textarea.addEventListener('keyup', function() {
        var characterCount = this.value.length;
        if (current) {
            current.textContent = characterCount || '0';
        }
    });
});

// checkbox 전체 선택
document.querySelectorAll('.checkbox__all').forEach(function(allCheckbox) {
    const name = allCheckbox.name;
    const boxes = document.querySelectorAll('input[name=' + name + ']:not(.checkbox__all)');

    if (allCheckbox.checked) {
        boxes.forEach(function(box) {
            box.checked = true;
        });
    }

    allCheckbox.addEventListener('change', () => {
        const checked = allCheckbox.checked;
        boxes.forEach(function(box) {
            box.checked = checked;
        });
    });

    boxes.forEach(function(box) {
        box.addEventListener('change', () => {
            const boxLength = boxes.length;
            const checkedLength = Array.from(boxes).filter(function(box) {
                return box.checked;
            }).length;

            const selectAll = (boxLength === checkedLength);
            allCheckbox.checked = selectAll;
        });
    });
});

// 레벨 난이도 버튼 선택
const levelWraps = document.querySelectorAll('.level-wrap');
levelWraps.forEach(levelWrap => {
  const levelButtons = levelWrap.querySelectorAll('button');
  levelButtons.forEach(button => {
    button.addEventListener('click', () => {
      levelButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
    });
  });
});

// 해시태그 입력
const tagField = document.querySelector('.tagfield');
const tagsContainer = document.querySelector('.tagcontainer');
if(tagField) {
    tagField.addEventListener('keydown', (event) => {
    const inputValue = tagField.value.trim();

    if (event.key === ' ' && inputValue.length > 0) {
        const validTag = inputValue.replace(/[^a-zA-Z0-9가-힣\s]/g, '');

        if (validTag.length <= 8) {
            const tag = document.createElement('li');
            tag.classList.add('tag');
            tag.textContent = '#' + validTag;
            tagsContainer.appendChild(tag);
        }
        tagField.value = '';
    }
    });
}

// 해설지 보기/닫기
const commentary = document.querySelector('.btn.commentary');
if(commentary) {
    commentary.addEventListener('click', () => {
        document.querySelector('.commentary-sheet').classList.toggle('active');
        commentary.classList.toggle('active');
    });
}

// 아이폰 하단값
function resize() {
    document.documentElement.style.setProperty('--vh', `${window.innerHeight * 0.01}px`);
}
window.addEventListener('resize', resize);


/*고등 전용 /////////// */
// 이미지 변경하기 팝업
const changeProfile = new Modal('changeProfile');

// 고등학교검색 팝업
const searchHigh = new Modal('searchHigh');

// 대학검색 팝업
const searchUniv = new Modal('searchUniv');

// 선호 과목 검색
const searchPref = new Modal('searchPref');

// 취약 과목 검색
const searchWeak = new Modal('searchWeak');

// 선택 과목 검색
const searchElective = new Modal('searchElective');

// 자가진단 레이어팝업
const selfTest = new Modal('selfTest');
// 2024.12.19 추가 - 이어서 시작하기 레이어팝업
const progressPop = new Modal('progressPop');
// 2024.12.19 추가 - 진단평가 다시 풀기 레이어팝업
const newTest = new Modal('newTest');

//샘플 문제 풀기 안내
const sampleExamInfo = new Modal('sampleExamInfo');

//학년 설정 변경 안내
const gradeSetGuide = new Modal('gradeSetGuide');

//랜덤 단원 바로 풀기 안내
const randomExamInfo = new Modal('randomExamInfo');

//검색문항안내
const searchQuestionsGuide = new Modal('searchQuestionsGuide');
//단원명/작품명 선택
const unitSelect = new Modal('unitSelect');





/*고등 전용 /////////// */

// 시험지 리그 레벨 안내 팝업
const levelGuide = new Modal('levelGuide');



/*중등 전용 /////////// */

const tabMini = new Tab('.tab-mini');

// 단어장 관리 레이어팝업
const setWordList = new Modal('setWordList');

// 단어 테스트 설정 레이어팝업
const testWord = new Modal('testWord');

// 단어장 담기 레이어팝업
const saveWord = new Modal('saveWord');

// 단어장 이동 레이어팝업
const moveWordList = new Modal('moveWordList');

// 미리보기 팝업
const prevExam = new Modal('prevExam');

// 해설지 보기 팝업
const explainView = new Modal('explainView');

// 게시판 이용수칙 팝업
const useBoard = new Modal('useBoard');

// 게시물 신고 팝업
const reportBoard = new Modal('reportBoard');

// 시험지 만들기(시험지정보 입력) 팝업
const testPaperAdd = new Modal('testPaperAdd');

// 부모님이 만드는 시험지 안내 팝업
const workbookGuide = new Modal('workbookGuide');

// 시험지 수정 팝업
const workbookEdit = new Modal('workbookEdit');

// SNS 공유 팝업
const snsShare = new Modal('snsShare');

// 시험지 공유하기 팝업
const workbookShare = new Modal('workbookShare');

// 시험지 공유현황 팝업
const workbookShareInfo = new Modal('workbookShareInfo');

// 문제이력 팝업
const questionHistory = new Modal('questionHistory');

// 채점결과 팝업
const markingResult = new Modal('markingResult');

// 영상 보기 윈도우 팝업
function openVideoPopup(url) {
    const popupOptions = "width=800,height=600,resizable=yes,scrollbars=yes";
    window.open(url, "_blank", popupOptions);
}
// 학년선택 팝업
const gradeSelect = new Modal('gradeSelect');

// 학습 목표 달성 현황 안내 팝업
const statusMap = new Modal('statusMap');

//수학MAP > 문제선택
const mathMapSelect = new Modal('mathMapSelect');

//수학MAP > 문제 결과확인
const mathMapResult = new Modal('mathMapResult');

//수학MAP > 선수학습 안내
const mathMapPreStudy = new Modal('mathMapPreStudy');

//수학MAP > 오류신고
const mathMapReport = new Modal('mathMapReport');

//수학MAP > 풀이 결과
const mathMapSolveResult = new Modal('mathMapSolveResult');

//오늘 문제 설명
const examInfo = new Modal('examInfo');

// 정답확인
const checkAnswer = new Modal('checkAnswer');

//수학MAP > 담기
const mathMapSave = new Modal('mathMapSave');

const answerChk = new Modal('answerChk');

/*중등 전용 /////////// */








/* /////////////////////// lnb-top__item 버튼 클릭시 시작 ///////////////////// */


// ai-bot 버튼 클릭 이벤트
$(".ai-bot").on("click", function () {
    const $botList = $(this).parent().children(".ai-bot__list");

    if ($botList.is(":visible")) {
        $botList.slideUp(200).fadeOut(200);  // slideUp 후 fadeOut
    } else {
        $botList.stop(true, true).slideDown(200).fadeIn(200); // slideDown 후 fadeIn
    }
});


/*$(".lnb-top__item > button").on("click", function () {
    $(".lnb-top__item > button").removeClass('active');
    $(this).addClass('active');
});*/

// lnb 영역 2뎁스 메뉴 온오프 정의 //////////////////////
const lnb = document.querySelector(".lnb");
const buttons = document.querySelectorAll(".lnb-inner-btn");

buttons.forEach(button => {
    button.addEventListener("click", function (event) {
        event.stopPropagation(); // 이벤트 버블링 방지

        const submenu = this.nextElementSibling;

        if (submenu && submenu.classList.contains("lnb-inner-btn__list")) {
            // 다른 열린 메뉴 닫기
            document.querySelectorAll(".lnb-inner-btn__list").forEach(menu => {
                if (menu !== submenu) {
                    menu.style.display = "none";
                }
            });

            // 현재 메뉴 토글
            submenu.style.display = submenu.style.display === "block" ? "none" : "block";
        }
    });
});

// .lnb 영역을 벗어나면 모든 서브메뉴 닫기
lnb.addEventListener("mouseleave", function () {
    document.querySelectorAll(".lnb-inner-btn__list").forEach(menu => {
        menu.style.display = "none";
    });
});

// 빈영역 클릭 시 메뉴 닫기 (lnb 내부 클릭 시 닫히지 않음)
document.addEventListener("click", function (event) {
    if (!lnb.contains(event.target)) {
        document.querySelectorAll(".lnb-inner-btn__list").forEach(menu => {
            menu.style.display = "none";
        });
    }
});
/* /////////////////////// lnb-top__item 버튼 클릭시 끝 ///////////////////// */