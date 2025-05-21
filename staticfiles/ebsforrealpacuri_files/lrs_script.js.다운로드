(() => {
    class TimeStamp {
        constructor() {
            this.track = {};
            this.state = 'stopped'; // 상태를 'stopped'로 초기화
        }

        clear() {
            this.track = {};
            this.state = 'stopped';
        }

        start() {
            if (this.state === 'running') {
                throw "타임스탬프가 이미 실행중입니다.";
            }

            this.clear(); // 이전 상태 초기화
            this.track.start = new Date();
            this.state = 'running';
        }

        finish() {
            if (this.state !== 'running') {
                throw "타임스탬프가 실행중이지 않습니다. 먼저 실행해주세요";
            }

            this.track.finish = new Date();
            this.state = 'stopped';
            return this.printResult();
        }

        printResult() {
            const duration = (this.track.finish - this.track.start) / 1000; // 초 단위
            return duration;
        }
    }


    let timeStamp = new TimeStamp();

    /**
     * @Comment DOM 객체인 Window의 생명주기가 시작될때 시간을 측정하는 객체인 Timestamp가 시작되며,
     * 페이지의 모든 요소(HTML, CSS, 이미지, 스크립트 등)가 로드된 후 실행됨.
     */
    window.onload = () => {
        timeStamp.start();
    }

    /**
     * @Comment 페이지 종료 시점에 유저 행동 데이터를 저장 (예: 방문 시간, 페이지 이동 경로, 머문 시간 등)
     */
    window.addEventListener('beforeunload', function (e) {
        const dataSet = getData();
        sendData(dataSet);
    });

    /**
     * @Comment sendData: 이벤트 클러스터의 Router주소에 맞게 데이터를 전송하는 FetchAPI
     * @Param url : 이벤트 클러스터에 분기 태울 마지막 url 주소
     * @Param dataSet : 해당 주소에 데이터를 보낼 Object
     * @Return 실패시 console에 Error를 찍는다.
     */
    const sendData = (dataSet) => {
        const now = Date.now();
        try {
            const protocol = window.location.protocol;
            const user_id = document.querySelector("#ibricks-user-data").value || '';
            dataSet.user_id = user_id;

            const localUrl = 'http://localhost:9700/main/lrs/lrslog';
            const prodUrl = `${protocol}//aievent.ebsi.co.kr/main/lrs/lrslog`;

            // fetch(prodUrl, {
            //     method: 'POST',
            //     headers: { 'Content-Type': 'application/json' },
            //     body: JSON.stringify(dataSet)
            // });

            // 위 fetch 요청 sendBeacon 으로 변경 2025.04.28
            const blob = new Blob([JSON.stringify(dataSet)], { type: 'application/json' });
            navigator.sendBeacon(prodUrl, blob);
        } catch (error) {
            console.error('# LRS API 요청 오류:', error);
        }
    };

    /**
     * @Comment getData: 브라우저에 해당 유저의 os, 브라우저 종류, 현재 URL, 전 URL, 브라우저의 Title, 머문시간 등등 ...
     * 모든 데이터를 Object에 담아 보낸다.
     * @Return returnObj : 위에 언급된 모든 정보들을 Object에 담아 리턴한다.
     */
    // 사용자 데이터 수집
    const getData = () => {
        const os_check = () => {
            const osMap = {
                "Win": "Windows",
                "Mac": "MacOS",
                "X11": "UNIX",
                "Linux": "Linux"
            };
            return Object.keys(osMap).find(os => navigator.appVersion.indexOf(os) !== -1) || "Unknown OS";
        };

        const dataObj = {
            now_url: window.location.href,
            past_url: document.referrer,
            browser_agent: window.navigator.userAgent,
            browser_system: window.navigator.platform,
            os: os_check(),
            stay_time: timeStamp.finish()
        };
        return dataObj;
    };
})();