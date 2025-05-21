$(function() {
    initPage.init();
});

// 화면 설정
var initPage = {
    // 초기 실행 함수
    init: function() {
        // 가상 스크롤바, modal popup, 검색
        var script = '<script type="text/javascript" src="https://kr.object.ncloudstorage.com/danchoo/web/hsc_resource/asset/js/common.js"></script>';

        $('head').append(script);

        // header, side pannel, footer load
        // this.header();
        // this.rnbPannel();
        // this.footer();
        // this.UISize();
    },

    // header load
    header: function() {
        var $_this = this;
        var headerObj = $('.wrap .ui_header-group');
        headerObj.load('../layout/header.html', function() {});
    },

    // side pannel load
    rnbPannel: function() {
        var $_this = this;
        var sideObj = $('.wrap .lnb-wrap');
        sideObj.load('../layout/rnb.html', '', function() {});
    },

    // footer load
    footer: function() {
        var footerObj = $('.wrap > footer');
        footerObj.load('../layout/footer.html', function() {
            // common.js 로드
            $.getScript('/hsc_resource/asset/js/common.js', function() {});
        });
    },

    UISize: function() {
        /* 디바이스 가로 세로 확인 */
        let currentOrientation = function() {
            // 화면 방향의 각도가 0도 또는 90도인지 확인합니다.
            let isZeroNinety = window.screen.orientation.angle % 180 === 0;
            
            // 각도에 따라 class를 추가합니다.
            if (isZeroNinety) {
                document.documentElement.classList.add("zero-ninety");
            } else {
                document.documentElement.classList.remove("zero-ninety");
            }
        };

        // 현재 화면 방향을 확인합니다.
        currentOrientation();

        // window.onorientationchange 이벤트를 사용하여 화면 방향이 변경될 때마다 class를 업데이트합니다.
        window.addEventListener("orientationchange", currentOrientation);

        /* 브라우저/ 디바이스 가로 갑 체크 */
        function updateBodyClass() {
            const body = document.body;
            const windowWidth = window.innerWidth;
            if (windowWidth <= 640) {
                body.classList.add('size-640');
                body.classList.remove('size-900', 'size-1200');
            } else if (windowWidth <= 900) {
                body.classList.add('size-900');
                body.classList.remove('size-640', 'size-1200');
            } else {
                body.classList.add('size-1200');
                body.classList.remove('size-640', 'size-900');
            }
        }
        
        // 초기화 및 리사이즈 이벤트 핸들러 등록
        updateBodyClass();
        window.addEventListener('resize', updateBodyClass);
    }
};

// ready 시점 정의
$(document).ready(function() {
    setTimeout(function() {
    }, 500);
});