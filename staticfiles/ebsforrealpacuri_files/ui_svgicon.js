const svgWrap = document.createElement('div'),
      svgData = `
      <!-- 닫기(두꺼움) -->
      <svg style="display: none;">
        <symbol id="svg-cross" viewBox="0 0 12 12" preserveAspectRatio="xMinYMin meet">
          <path d="M12,9.6L9.6,12L6,8.399L2.4,12L0,9.6L3.6,6L0,2.4L2.4,0L6,3.6L9.6,0L12,2.4L8.399,6L12,9.6z"/>
        </symbol>
      </svg>
      <!-- /닫기(두꺼움) -->
      <!-- 닫기(얇음) -->
      <svg style="display: none;">
        <symbol id="svg-cross2" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
          <path d="M12 10.586l4.95-4.95 1.414 1.414-4.95 4.95 4.95 4.95-1.414 1.414-4.95-4.95-4.95 4.95-1.414-1.414 4.95-4.95-4.95-4.95L7.05 5.636z"/>
        </symbol>
      </svg>
      <!-- 닫기(얇음) -->
      <!-- 담기 -->
      <svg style="display: none;">
        <symbol id="svg-file-download" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
          <path d="M4 3h16l2 4v13a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V7.004L4 3zm9 11v-4h-2v4H8l4 4 4-4h-3zm6.764-7l-1-2H5.237l-1 2h15.527z"/>
        </symbol>
      </svg>
      <!-- 담기 -->
      <!-- 하트 -->
      <svg style="display: none;">
        <symbol id="svg-heart" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
          <path fill="none" d="M0 0H24V24H0z"/><path d="M16.5 3C19.538 3 22 5.5 22 9c0 7-7.5 11-10 12.5C9.5 20 2 16 2 9c0-3.5 2.5-6 5.5-6C9.36 3 11 4 12 5c1-1 2.64-2 4.5-2z"/>
        </symbol>
      </svg>
      <!-- 하트 -->
      <!-- 공유하기 -->
      <svg style="display: none;">
        <symbol id="svg-share" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
          <path fill="none" d="M0 0h24v24H0z"/>
          <path d="M13.12 17.023l-4.199-2.29a4 4 0 1 1 0-5.465l4.2-2.29a4 4 0 1 1 .959 1.755l-4.2 2.29a4.008 4.008 0 0 1 0 1.954l4.199 2.29a4 4 0 1 1-.959 1.755zM6 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm11-6a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm0 12a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/>
        </symbol>
      </svg>
      <!-- 공유하기 -->
      <!-- 유저 -->
      <svg style="display: none;">
        <symbol id="svg-user" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
          <path fill="none" d="M0 0h24v24H0z"/><path d="M12 2c5.52 0 10 4.48 10 10s-4.48 10-10 10S2 17.52 2 12 6.48 2 12 2zM6.023 15.416C7.491 17.606 9.695 19 12.16 19c2.464 0 4.669-1.393 6.136-3.584A8.968 8.968 0 0 0 12.16 13a8.968 8.968 0 0 0-6.137 2.416zM12 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
        </symbol>
      </svg>
      <!-- 유저 -->
      <!-- 검색(돋보기) -->
      <svg style="display: none;">
        <symbol id="svg-search" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
          <path fill="none" d="M0 0h24v24H0z"/><path d="M18.031 16.617l4.283 4.282-1.415 1.415-4.282-4.283A8.96 8.96 0 0 1 11 20c-4.968 0-9-4.032-9-9s4.032-9 9-9 9 4.032 9 9a8.96 8.96 0 0 1-1.969 5.617zm-2.006-.742A6.977 6.977 0 0 0 18 11c0-3.868-3.133-7-7-7-3.868 0-7 3.132-7 7 0 3.867 3.132 7 7 7a6.977 6.977 0 0 0 4.875-1.975l.15-.15z"/>
        </symbol>
      </svg>
      <!-- 검색(돋보기) -->
      <!-- 펜 -->
    <svg style="display: none;">
      <symbol id="svg-test_pen" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/>
        <path d="M9.243 19H21v2H3v-4.243l9.9-9.9 4.242 4.244L9.242 19zm5.07-13.556l2.122-2.122a1 1 0 0 1 1.414 0l2.829 2.829a1 1 0 0 1 0 1.414l-2.122 2.121-4.242-4.242z"/>
      </symbol>
    </svg>
    <!-- 펜 -->
    <!-- 메뉴 -->
    <svg style="display: none;">
      <symbol id="svg-menu" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/>
        <path d="M3 4h18v2H3V4zm0 7h18v2H3v-2zm0 7h18v2H3v-2z"/>
      </symbol>
    </svg>
    <!-- 메뉴 -->
    <!-- 느낌표 -->
    <svg style="display: none;">
      <symbol id="svg-info" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/>
        <path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm-1-11v6h2v-6h-2zm0-4v2h2V7h-2z"/>
      </symbol>
    </svg>
    <!-- 느낌표 -->
    <!-- 물음표 -->
    <svg style="display: none;">
      <symbol id="svg-question" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm-1-7v2h2v-2h-2zm2-1.645A3.502 3.502 0 0 0 12 6.5a3.501 3.501 0 0 0-3.433 2.813l1.962.393A1.5 1.5 0 1 1 12 11.5a1 1 0 0 0-1 1V14h2v-.645z"/>
      </symbol>
    </svg>
    <!-- 물음표 -->
    <!-- 로그인 -->  
    <svg style="display: none;">
      <symbol id="svg-login" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none"  d="M0 0h24v24H0z"/>
        <path d="M4 15h2v5h12V4H6v5H4V3a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-6zm6-4V8l5 4-5 4v-3H2v-2h8z"/>
      </symbol>
    </svg>
    <!-- 로그인 -->
    <!-- 로그아웃 -->
    <svg style="display: none;">
      <symbol id="svg-logout" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/>
        <path d="M4 18h2v2h12V4H6v2H4V3a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-3zm2-7h7v2H6v3l-5-4 5-4v3z"/>
      </symbol>
    </svg>
    <!-- 로그아웃 -->
    <!-- 화이트모드전환 -->
    <svg style="display: none;">
      <symbol id="svg-sun" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/>
        <path d="M12 18a6 6 0 1 1 0-12 6 6 0 0 1 0 12zm0-2a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM11 1h2v3h-2V1zm0 19h2v3h-2v-3zM3.515 4.929l1.414-1.414L7.05 5.636 5.636 7.05 3.515 4.93zM16.95 18.364l1.414-1.414 2.121 2.121-1.414 1.414-2.121-2.121zm2.121-14.85l1.414 1.415-2.121 2.121-1.414-1.414 2.121-2.121zM5.636 16.95l1.414 1.414-2.121 2.121-1.414-1.414 2.121-2.121zM23 11v2h-3v-2h3zM4 11v2H1v-2h3z"/>
      </symbol>
    </svg>
    <!-- 화이트모드전환 -->
    <!-- 다크모드전환 -->
    <svg style="display: none;">
      <symbol id="svg-moon" viewBox="0 0 24 24"" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/>
        <path d="M10 7a7 7 0 0 0 12 4.9v.1c0 5.523-4.477 10-10 10S2 17.523 2 12 6.477 2 12 2h.1A6.979 6.979 0 0 0 10 7zm-6 5a8 8 0 0 0 15.062 3.762A9 9 0 0 1 8.238 4.938 7.999 7.999 0 0 0 4 12z"/>
      </symbol>
    </svg>
    <!-- 다크모드전환 -->
    <!-- 불러오기 -->
    <svg style="display: none;">
      <symbol id="svg-folder" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/><path d="M22 13.126A6 6 0 0 0 13.303 21H3a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h7.414l2 2H21a1 1 0 0 1 1 1v7.126zM18 17v-3.5l5 4.5-5 4.5V19h-3v-2h3z"/>
      </symbol>
    </svg>
    <!-- 불러오기 -->
    <!-- 달력 -->
    <svg style="display: none;">
      <symbol id="svg-calendar" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/><path d="M9 1v2h6V1h2v2h4a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h4V1h2zm11 9H4v9h16v-9zm-4.964 1.136l1.414 1.414-4.95 4.95-3.536-3.536L9.38 12.55l2.121 2.122 3.536-3.536zM7 5H4v3h16V5h-3v1h-2V5H9v1H7V5z"/>
      </symbol>
    </svg>
    <!-- 달력 -->
    <!-- 체크(블루) -->
    <svg style="display: none;">
      <symbol id="svg-check-blue" viewBox="0 0 32 32" preserveAspectRatio="xMinYMin meet">
        <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
          <g fill="#31a9d7">
            <path d="M8,12 L12,16 L24,4 L30,10 L12,28 L2,18 L8,12 Z"></path>
          </g>
        </g>
      </symbol>
    </svg>
    <!-- 체크(블루) -->
    <!-- 타임 -->
    <svg style="display: none;">
      <symbol id="svg-time" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">  
        <path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-2a8 8 0 1 0 0-16 8 8 0 0 0 0 16zm1-8h4v2h-6V7h2v5z"/>
      </symbol>
    </svg>
    <!-- 타임 -->
    <!-- 타이머 -->
    <svg style="display: none;">
      <symbol id="svg-timer" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path d="M17.618 5.968l1.453-1.453 1.414 1.414-1.453 1.453a9 9 0 1 1-1.414-1.414zM12 20a7 7 0 1 0 0-14 7 7 0 0 0 0 14zM11 8h2v6h-2V8zM8 1h8v2H8V1z"/>
      </symbol>
    </svg>
    <!-- 타이머 -->
    <!-- 별 -->
    <svg style="display: none;">
      <symbol id="svg-star" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path d="M12 18.26l-7.053 3.948 1.575-7.928L.587 8.792l8.027-.952L12 .5l3.386 7.34 8.027.952-5.935 5.488 1.575 7.928z"/>
      </symbol>
    </svg>
    <!-- 별 -->
    <!-- 정답 확인 -->
    <svg style="display: none;">
      <symbol id="svg-examination" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0L24 0 24 24 0 24z"/>
        <path d="M20 2c.552 0 1 .448 1 1v3.757l-2 2V4H5v16h14v-2.758l2-2V21c0 .552-.448 1-1 1H4c-.552 0-1-.448-1-1V3c0-.552.448-1 1-1h16zm1.778 6.808l1.414 1.414L15.414 18l-1.416-.002.002-1.412 7.778-7.778zM13 12v2H8v-2h5zm3-4v2H8V8h8z"/>
      </symbol>
    </svg>
    <!-- 정답 확인 끝-->
    <!-- 라운드 플러스 -->
    <svg style="display: none;">
      <symbol id="svg-round-plus" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">
        <path fill="none" d="M0 0h24v24H0z"/><path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm-1-11H7v2h4v4h2v-4h4v-2h-4V7h-2v4z"/>
      </symbol>
    </svg>
    <!-- 라운드 플러스 끝-->
    <!-- 라운드 닫기-->
    <svg style="display: none;">
      <symbol id="svg-round-close" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">  
        <path d="M12 22C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10-4.477 10-10 10zm0-11.414L9.172 7.757 7.757 9.172 10.586 12l-2.829 2.828 1.415 1.415L12 13.414l2.828 2.829 1.415-1.415L13.414 12l2.829-2.828-1.415-1.415L12 10.586z"/>
      </symbol>
    </svg>
    <!-- 라운드 닫기 끝-->
    <!-- 눈 아이콘 -->
    <svg style="display: none;">
      <symbol id="svg-eye" viewBox="0 0 24 24" preserveAspectRatio="xMinYMin meet">  
        <path fill="none" d="M0 0h24v24H0z"/>
        <path d="M1.181 12C2.121 6.88 6.608 3 12 3c5.392 0 9.878 3.88 10.819 9-.94 5.12-5.427 9-10.819 9-5.392 0-9.878-3.88-10.819-9zM12 17a5 5 0 1 0 0-10 5 5 0 0 0 0 10zm0-2a3 3 0 1 1 0-6 3 3 0 0 1 0 6z"/>
      </symbol>
    </svg>
    <!-- 눈 아이콘 끝-->
      `;

svgWrap.innerHTML = svgData;
document.body.appendChild(svgWrap);