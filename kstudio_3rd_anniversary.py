import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# KSTUDIO 3RD ANNIVERSARY APP
# Animated Pixel Gym Miniature Celebration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Happy 3rd Anniversary, Kstudio!",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown('''
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        max-width: 100%;
    }
</style>
''', unsafe_allow_html=True)

html = r'''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
    :root {
        --bg1: #12091f;
        --bg2: #261447;
        --bg3: #3b1d66;
        --gold: #ffd166;
        --cream: #fff2cc;
        --pink: #ff7eb6;
        --cyan: #72e6ff;
        --green: #7dff9b;
        --purple: #b690ff;
        --white: #ffffff;
    }

    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        min-height: 100vh;
        overflow: hidden;
        font-family: 'Courier New', monospace;
        background:
            radial-gradient(circle at 20% 20%, rgba(255, 126, 182, 0.18), transparent 30%),
            radial-gradient(circle at 80% 15%, rgba(114, 230, 255, 0.14), transparent 28%),
            linear-gradient(135deg, var(--bg1), var(--bg2), var(--bg3));
        color: white;
    }

    .scene {
        position: relative;
        width: 100%;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        padding: 28px 20px 20px;
        isolation: isolate;
    }

    .stars, .confetti, .hearts {
        position: absolute;
        inset: 0;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }

    .star {
        position: absolute;
        width: 4px;
        height: 4px;
        background: white;
        opacity: .8;
        image-rendering: pixelated;
        animation: twinkle 2s infinite steps(2);
    }

    @keyframes twinkle {
        0%, 100% { transform: scale(1); opacity: .35; }
        50% { transform: scale(1.8); opacity: 1; }
    }

    .confetti-piece {
        position: absolute;
        top: -30px;
        width: 10px;
        height: 16px;
        opacity: 0.95;
        animation: fall linear infinite;
        image-rendering: pixelated;
    }

    @keyframes fall {
        0% {
            transform: translateY(-40px) rotate(0deg);
        }
        100% {
            transform: translateY(110vh) rotate(360deg);
        }
    }

    .heart {
        position: absolute;
        bottom: -40px;
        font-size: 22px;
        animation: floatUp linear infinite;
        filter: drop-shadow(0 0 6px rgba(255,255,255,.4));
    }

    @keyframes floatUp {
        0% {
            transform: translateY(0) scale(.8);
            opacity: 0;
        }
        15% {
            opacity: 1;
        }
        100% {
            transform: translateY(-110vh) scale(1.35);
            opacity: 0;
        }
    }

    .top-card {
        position: relative;
        z-index: 3;
        width: min(1100px, 96vw);
        text-align: center;
        padding: 18px 24px 20px;
        border: 4px solid rgba(255, 209, 102, .95);
        background: rgba(12, 7, 28, .72);
        box-shadow:
            0 0 0 6px rgba(255,255,255,.08),
            0 18px 60px rgba(0,0,0,.35),
            inset 0 0 25px rgba(255, 209, 102, .12);
        backdrop-filter: blur(4px);
        image-rendering: pixelated;
    }

    .mini-label {
        display: inline-block;
        padding: 8px 14px;
        margin-bottom: 10px;
        color: var(--bg1);
        background: var(--gold);
        font-weight: 800;
        font-size: clamp(12px, 1.4vw, 16px);
        letter-spacing: 2px;
        text-transform: uppercase;
        animation: pulseLabel 1.4s infinite steps(2);
    }

    @keyframes pulseLabel {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    h1 {
        margin: 4px 0 6px;
        font-size: clamp(34px, 5.2vw, 76px);
        line-height: 1.05;
        color: var(--cream);
        text-shadow:
            4px 4px 0 #63247d,
            8px 8px 0 rgba(0,0,0,.35);
        animation: titleBounce 1.8s infinite steps(3);
    }

    @keyframes titleBounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-6px); }
    }

    .subtitle {
        max-width: 950px;
        margin: 0 auto;
        font-size: clamp(15px, 1.65vw, 22px);
        line-height: 1.45;
        color: rgba(255,255,255,.95);
    }

    .highlight {
        color: var(--gold);
        font-weight: 800;
    }

    .gym-area {
        position: relative;
        z-index: 2;
        margin-top: 22px;
        width: min(1180px, 98vw);
        height: min(500px, 52vh);
        border: 6px solid rgba(255,255,255,.95);
        background:
            linear-gradient(to bottom, rgba(77, 42, 120, .95) 0 64%, rgba(35, 20, 57, .95) 64% 100%);
        box-shadow:
            0 18px 60px rgba(0,0,0,.45),
            inset 0 0 0 6px rgba(255, 209, 102, .24);
        overflow: hidden;
        image-rendering: pixelated;
    }

    .gym-sign {
        position: absolute;
        top: 18px;
        left: 50%;
        transform: translateX(-50%);
        padding: 10px 18px;
        border: 4px solid var(--gold);
        background: #1b1032;
        color: var(--gold);
        font-size: clamp(18px, 2vw, 28px);
        font-weight: 900;
        letter-spacing: 4px;
        text-shadow: 2px 2px 0 #000;
        animation: neon 1.1s infinite steps(2);
    }

    @keyframes neon {
        0%, 100% {
            box-shadow: 0 0 0 rgba(255,209,102,0);
            opacity: 1;
        }
        50% {
            box-shadow: 0 0 18px rgba(255,209,102,.75);
            opacity: .87;
        }
    }

    .floor-grid {
        position: absolute;
        inset: 64% 0 0 0;
        background:
            linear-gradient(rgba(255,255,255,.08) 2px, transparent 2px),
            linear-gradient(90deg, rgba(255,255,255,.08) 2px, transparent 2px);
        background-size: 46px 32px;
    }

    .window {
        position: absolute;
        top: 92px;
        width: 150px;
        height: 110px;
        border: 5px solid #f7ecff;
        background:
            linear-gradient(180deg, #6dd5ff, #ab7cff 70%, #ffd166);
        box-shadow: inset 0 0 0 5px rgba(255,255,255,.18);
    }

    .window::before,
    .window::after {
        content: "";
        position: absolute;
        background: rgba(255,255,255,.75);
    }

    .window::before {
        width: 5px;
        height: 100%;
        left: 50%;
        transform: translateX(-50%);
    }

    .window::after {
        width: 100%;
        height: 5px;
        top: 50%;
        transform: translateY(-50%);
    }

    .window.left { left: 70px; }
    .window.right { right: 70px; }

    .equipment {
        position: absolute;
        bottom: 68px;
    }

    .rack {
        left: 48px;
        width: 210px;
        height: 150px;
    }

    .rack-frame {
        position: absolute;
        bottom: 0;
        left: 10px;
        width: 190px;
        height: 122px;
        border-left: 8px solid #d7d2e9;
        border-right: 8px solid #d7d2e9;
        border-bottom: 8px solid #d7d2e9;
    }

    .rack-shelf {
        position: absolute;
        left: 14px;
        width: 182px;
        height: 8px;
        background: #d7d2e9;
    }

    .rack-shelf.s1 { bottom: 37px; }
    .rack-shelf.s2 { bottom: 78px; }

    .db {
        position: absolute;
        width: 40px;
        height: 18px;
        bottom: 43px;
        background: transparent;
    }

    .db::before, .db::after {
        content: "";
        position: absolute;
        top: 2px;
        width: 12px;
        height: 14px;
        background: var(--cyan);
    }

    .db::before { left: 0; }
    .db::after { right: 0; }

    .db span {
        position: absolute;
        left: 10px;
        top: 7px;
        width: 20px;
        height: 4px;
        background: white;
    }

    .db.d1 { left: 28px; }
    .db.d2 { left: 82px; bottom: 84px; }
    .db.d3 { left: 136px; }

    .bench {
        left: 305px;
        width: 280px;
        height: 190px;
    }

    .bench-seat {
        position: absolute;
        left: 70px;
        bottom: 34px;
        width: 132px;
        height: 20px;
        background: #ff7eb6;
        box-shadow: 0 7px 0 #b44678;
    }

    .bench-leg {
        position: absolute;
        bottom: 0;
        width: 12px;
        height: 45px;
        background: #e8e1ff;
    }

    .bench-leg.l1 { left: 90px; }
    .bench-leg.l2 { left: 182px; }

    .stand {
        position: absolute;
        bottom: 45px;
        width: 12px;
        height: 110px;
        background: #e8e1ff;
    }

    .stand.sleft { left: 48px; }
    .stand.sright { right: 48px; }

    .bar {
        position: absolute;
        top: 40px;
        left: 22px;
        width: 236px;
        height: 8px;
        background: #fff;
        animation: barLift 1.35s infinite steps(3);
        transform-origin: center;
    }

    @keyframes barLift {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-16px); }
    }

    .plate {
        position: absolute;
        top: 26px;
        width: 20px;
        height: 36px;
        background: var(--green);
        animation: barLift 1.35s infinite steps(3);
    }

    .plate.left { left: 18px; }
    .plate.right { right: 18px; }

    .treadmill {
        right: 330px;
        width: 230px;
        height: 180px;
    }

    .tm-base {
        position: absolute;
        bottom: 16px;
        left: 18px;
        width: 190px;
        height: 28px;
        background: #2a203d;
        border: 6px solid #e8e1ff;
        overflow: hidden;
    }

    .belt {
        position: absolute;
        inset: 5px;
        background: repeating-linear-gradient(
            90deg,
            #72e6ff 0 22px,
            #1c5260 22px 38px
        );
        animation: moveBelt .55s linear infinite;
    }

    @keyframes moveBelt {
        from { background-position: 0 0; }
        to { background-position: 38px 0; }
    }

    .tm-post {
        position: absolute;
        bottom: 40px;
        right: 40px;
        width: 12px;
        height: 90px;
        background: #e8e1ff;
        transform: skewX(-10deg);
    }

    .tm-console {
        position: absolute;
        right: 20px;
        top: 35px;
        width: 54px;
        height: 34px;
        background: var(--gold);
        border: 5px solid #20112f;
    }

    .runner {
        position: absolute;
        right: 404px;
        bottom: 122px;
        width: 84px;
        height: 120px;
        animation: runnerBounce .45s infinite steps(2);
    }

    @keyframes runnerBounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-7px); }
    }

    .head {
        position: absolute;
        top: 0;
        left: 28px;
        width: 34px;
        height: 34px;
        background: #ffd4b8;
        box-shadow:
            0 -8px 0 #3d2233 inset;
    }

    .body {
        position: absolute;
        top: 38px;
        left: 24px;
        width: 42px;
        height: 40px;
        background: #ff7eb6;
    }

    .arm {
        position: absolute;
        top: 46px;
        width: 12px;
        height: 38px;
        background: #ffd4b8;
        transform-origin: top;
    }

    .arm.a1 {
        left: 12px;
        animation: armSwing .45s infinite steps(2);
    }

    .arm.a2 {
        right: 6px;
        animation: armSwingReverse .45s infinite steps(2);
    }

    @keyframes armSwing {
        0%, 100% { transform: rotate(28deg); }
        50% { transform: rotate(-28deg); }
    }

    @keyframes armSwingReverse {
        0%, 100% { transform: rotate(-28deg); }
        50% { transform: rotate(28deg); }
    }

    .leg {
        position: absolute;
        top: 76px;
        width: 14px;
        height: 42px;
        background: #72e6ff;
        transform-origin: top;
    }

    .leg.l1 {
        left: 28px;
        animation: legRun .45s infinite steps(2);
    }

    .leg.l2 {
        left: 50px;
        animation: legRunReverse .45s infinite steps(2);
    }

    @keyframes legRun {
        0%, 100% { transform: rotate(22deg); }
        50% { transform: rotate(-22deg); }
    }

    @keyframes legRunReverse {
        0%, 100% { transform: rotate(-22deg); }
        50% { transform: rotate(22deg); }
    }

    .corner {
        right: 54px;
        width: 210px;
        height: 180px;
    }

    .mat {
        position: absolute;
        bottom: 16px;
        left: 12px;
        width: 184px;
        height: 28px;
        background: var(--purple);
        box-shadow: 0 7px 0 #62449e;
    }

    .kettlebell {
        position: absolute;
        bottom: 44px;
        left: 30px;
        width: 42px;
        height: 42px;
        background: var(--gold);
        border-radius: 0;
        animation: jiggle 1.1s infinite steps(2);
    }

    .kettlebell::before {
        content: "";
        position: absolute;
        left: 9px;
        top: -18px;
        width: 24px;
        height: 22px;
        border: 7px solid var(--gold);
        border-bottom: 0;
    }

    @keyframes jiggle {
        0%,100% { transform: rotate(0); }
        50% { transform: rotate(7deg); }
    }

    .plant {
        position: absolute;
        right: 20px;
        bottom: 44px;
        width: 58px;
        height: 88px;
    }

    .pot {
        position: absolute;
        bottom: 0;
        left: 11px;
        width: 36px;
        height: 34px;
        background: #ff9f68;
    }

    .leaf {
        position: absolute;
        width: 22px;
        height: 34px;
        background: var(--green);
        transform-origin: bottom;
        animation: sway 1.8s infinite steps(3);
    }

    .leaf.one { left: 18px; bottom: 28px; transform: rotate(-24deg); }
    .leaf.two { left: 32px; bottom: 33px; transform: rotate(20deg); animation-delay: .4s; }
    .leaf.three { left: 7px; bottom: 40px; transform: rotate(-44deg); animation-delay: .8s; }

    @keyframes sway {
        0%,100% { margin-left: 0; }
        50% { margin-left: 4px; }
    }

    .dancer {
        position: absolute;
        left: 595px;
        bottom: 93px;
        width: 92px;
        height: 145px;
        animation: danceBody .7s infinite steps(2);
    }

    @keyframes danceBody {
        0%, 100% { transform: translateY(0) rotate(-2deg); }
        50% { transform: translateY(-9px) rotate(2deg); }
    }

    .d-head {
        position: absolute;
        top: 0;
        left: 26px;
        width: 40px;
        height: 40px;
        background: #ffd4b8;
        box-shadow: 0 -10px 0 #402453 inset;
    }

    .d-body {
        position: absolute;
        top: 45px;
        left: 22px;
        width: 48px;
        height: 48px;
        background: var(--gold);
    }

    .d-arm {
        position: absolute;
        top: 52px;
        width: 14px;
        height: 48px;
        background: #ffd4b8;
        transform-origin: top;
    }

    .d-arm.left {
        left: 5px;
        animation: cheerLeft .7s infinite steps(2);
    }

    .d-arm.right {
        right: 5px;
        animation: cheerRight .7s infinite steps(2);
    }

    @keyframes cheerLeft {
        0%,100% { transform: rotate(-48deg); }
        50% { transform: rotate(-82deg); }
    }

    @keyframes cheerRight {
        0%,100% { transform: rotate(48deg); }
        50% { transform: rotate(82deg); }
    }

    .d-leg {
        position: absolute;
        top: 92px;
        width: 14px;
        height: 48px;
        background: var(--pink);
        transform-origin: top;
    }

    .d-leg.left { left: 30px; transform: rotate(10deg); }
    .d-leg.right { left: 52px; transform: rotate(-10deg); }

    .speech {
        position: absolute;
        left: 530px;
        top: 138px;
        width: 235px;
        padding: 12px;
        border: 4px solid white;
        background: rgba(18,9,31,.94);
        color: var(--cream);
        font-weight: 800;
        text-align: center;
        font-size: 16px;
        box-shadow: 6px 6px 0 rgba(0,0,0,.25);
        animation: speechPop 1.1s infinite steps(2);
    }

    .speech::after {
        content: "";
        position: absolute;
        left: 32px;
        bottom: -20px;
        width: 0;
        height: 0;
        border-left: 18px solid transparent;
        border-right: 18px solid transparent;
        border-top: 20px solid white;
    }

    @keyframes speechPop {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.03); }
    }

    .footer-message {
        position: relative;
        z-index: 3;
        width: min(1100px, 96vw);
        margin-top: 18px;
        padding: 14px 20px;
        text-align: center;
        background: rgba(12, 7, 28, .74);
        border: 4px solid rgba(255,255,255,.88);
        font-size: clamp(14px, 1.5vw, 20px);
        line-height: 1.45;
        color: rgba(255,255,255,.97);
        box-shadow: 0 14px 40px rgba(0,0,0,.28);
    }

    .typed {
        display: inline-block;
        overflow: hidden;
        white-space: nowrap;
        border-right: 4px solid var(--gold);
        animation:
            typing 7s steps(86, end) infinite,
            cursor .7s step-end infinite;
        max-width: 100%;
    }

    @keyframes typing {
        0% { width: 0; }
        45% { width: 100%; }
        80% { width: 100%; }
        100% { width: 0; }
    }

    @keyframes cursor {
        50% { border-color: transparent; }
    }

    .badge {
        position: absolute;
        z-index: 4;
        top: 16px;
        right: 18px;
        padding: 10px 14px;
        background: var(--pink);
        color: #230f35;
        border: 4px solid white;
        font-weight: 900;
        transform: rotate(4deg);
        box-shadow: 6px 6px 0 rgba(0,0,0,.25);
        animation: badgeWiggle 1s infinite steps(2);
    }

    @keyframes badgeWiggle {
        0%,100% { transform: rotate(4deg); }
        50% { transform: rotate(-4deg); }
    }

    .miniatures-row {
        position: relative;
        z-index: 2;
        width: min(1180px, 98vw);
        margin-top: 22px;
        display: flex;
        gap: 18px;
        align-items: stretch;
        justify-content: center;
    }

    .mini-panel {
        position: relative;
        flex: 1 1 0;
        min-height: 340px;
        border: 6px solid rgba(255,255,255,.95);
        background:
            linear-gradient(to bottom, rgba(77, 42, 120, .95) 0 66%, rgba(35, 20, 57, .95) 66% 100%);
        box-shadow:
            0 18px 60px rgba(0,0,0,.45),
            inset 0 0 0 6px rgba(255, 209, 102, .24);
        overflow: hidden;
        image-rendering: pixelated;
    }

    .mini-panel .floor-grid {
        inset: 71% 0 0 0;
        background-size: 32px 24px;
    }

    .mini-panel .gym-sign {
        top: 18px;
        padding: 8px 12px;
        font-size: 18px;
        letter-spacing: 3px;
    }

    .mini-panel .badge {
        top: 12px;
        right: 12px;
        padding: 7px 10px;
        border-width: 3px;
        font-size: 13px;
        box-shadow: 4px 4px 0 rgba(0,0,0,.25);
    }

    .mini-panel .window {
        top: 78px;
        width: 96px;
        height: 74px;
        border-width: 4px;
        box-shadow: inset 0 0 0 4px rgba(255,255,255,.18);
    }

    .mini-panel .window.left { left: 16px; }
    .mini-panel .window.right { right: 16px; }

    .left-panel .rack {
        left: 8px;
        bottom: 18px;
        transform: scale(.56);
        transform-origin: bottom left;
    }

    .left-panel .bench {
        left: auto;
        right: -10px;
        bottom: 18px;
        transform: scale(.58);
        transform-origin: bottom right;
    }

    .right-panel .treadmill {
        left: 10px;
        right: auto;
        bottom: 18px;
        transform: scale(.60);
        transform-origin: bottom left;
    }

    .right-panel .runner {
        left: 58px;
        right: auto;
        bottom: 64px;
        transform: scale(.60);
        transform-origin: bottom left;
    }

    .right-panel .corner {
        right: -10px;
        bottom: 18px;
        transform: scale(.56);
        transform-origin: bottom right;
    }

    .right-panel .speech {
        top: 82px;
        left: auto;
        right: 14px;
        width: 178px;
        padding: 9px;
        font-size: 12px;
        line-height: 1.35;
    }

    .right-panel .speech::after {
        left: 112px;
        border-left: 14px solid transparent;
        border-right: 14px solid transparent;
        border-top: 16px solid white;
        bottom: -16px;
    }

    .right-panel .dancer {
        left: 50%;
        bottom: 126px;
        margin-left: -42px;
        transform: scale(.74);
        transform-origin: bottom center;
    }

    @media (max-width: 980px) {
        .miniatures-row {
            width: 97vw;
            gap: 14px;
        }

        .mini-panel {
            min-height: 315px;
        }

        .mini-panel .window.right {
            display: none;
        }

        .right-panel .speech {
            width: 160px;
            font-size: 11px;
        }

        .right-panel .speech::after {
            left: 96px;
        }
    }

    @media (max-width: 720px) {
        body { overflow-y: auto; }

        .scene {
            min-height: 100vh;
            height: auto;
            padding: 18px 10px 26px;
        }

        .top-card,
        .footer-message {
            width: 97vw;
        }

        .mini-label {
            line-height: 1.35;
            letter-spacing: 1.5px;
        }

        h1 {
            font-size: clamp(31px, 8.3vw, 44px);
            line-height: 1.08;
            text-shadow:
                3px 3px 0 #63247d,
                6px 6px 0 rgba(0,0,0,.35);
        }

        .subtitle,
        .footer-message {
            font-size: 15px;
            line-height: 1.55;
        }

        .miniatures-row {
            width: 97vw;
            flex-direction: column;
            gap: 14px;
            margin-top: 18px;
        }

        .mini-panel {
            min-height: 282px;
            border-width: 5px;
        }

        .mini-panel .badge {
            top: 10px;
            right: 10px;
            font-size: 12px;
            padding: 6px 9px;
        }

        .mini-panel .gym-sign {
            top: 16px;
            font-size: 17px;
            letter-spacing: 2px;
            max-width: 72%;
        }

        .mini-panel .window {
            top: 72px;
            width: 84px;
            height: 64px;
        }

        .mini-panel .window.right {
            display: none;
        }

        .left-panel .rack {
            transform: scale(.48);
            left: 2px;
            bottom: 10px;
        }

        .left-panel .bench {
            transform: scale(.50);
            right: -24px;
            bottom: 10px;
        }

        .right-panel .treadmill {
            transform: scale(.52);
            left: 2px;
            bottom: 8px;
        }

        .right-panel .runner {
            transform: scale(.52);
            left: 40px;
            bottom: 46px;
        }

        .right-panel .corner {
            transform: scale(.48);
            right: -20px;
            bottom: 10px;
        }

        .right-panel .dancer {
            transform: scale(.62);
            bottom: 106px;
            margin-left: -38px;
        }

        .right-panel .speech {
            top: 74px;
            right: 10px;
            width: 150px;
            font-size: 10.5px;
            padding: 8px;
        }

        .right-panel .speech::after {
            left: 92px;
        }

        .typed {
            white-space: normal;
            border-right: none;
            animation: none;
        }
    }
</style>
</head>
<body>
    <div class="scene">
        <div class="stars" id="stars"></div>
        <div class="confetti" id="confetti"></div>
        <div class="hearts" id="hearts"></div>

        <div class="top-card">
            <div class="mini-label">A celebration of strength, discipline & community</div>
            <h1>🎉 Happy 3rd Anniversary, Kstudio! 🎉</h1>
            <div class="subtitle">
                Congratulations on <span class="highlight">3 inspiring years</span> of building stronger bodies,
                stronger minds, and a beautiful fitness family. Thank you for being my beloved gym —
                a place of growth, encouragement, and countless personal victories. 💪✨
            </div>
        </div>

        <div class="miniatures-row">
            <div class="mini-panel left-panel">
                <div class="badge">LIFT ZONE</div>
                <div class="gym-sign">KSTUDIO</div>

                <div class="window left"></div>
                <div class="window right"></div>

                <div class="floor-grid"></div>

                <div class="equipment rack">
                    <div class="rack-frame"></div>
                    <div class="rack-shelf s1"></div>
                    <div class="rack-shelf s2"></div>
                    <div class="db d1"><span></span></div>
                    <div class="db d2"><span></span></div>
                    <div class="db d3"><span></span></div>
                </div>

                <div class="equipment bench">
                    <div class="stand sleft"></div>
                    <div class="stand sright"></div>
                    <div class="bar"></div>
                    <div class="plate left"></div>
                    <div class="plate right"></div>
                    <div class="bench-seat"></div>
                    <div class="bench-leg l1"></div>
                    <div class="bench-leg l2"></div>
                </div>
            </div>

            <div class="mini-panel right-panel">
                <div class="badge">FIT & FUN</div>
                <div class="gym-sign">KSTUDIO</div>

                <div class="window left"></div>
                <div class="window right"></div>

                <div class="floor-grid"></div>

                <div class="speech">“Thank you, Kstudio, for every sweat, smile & stronger version of me!”</div>

                <div class="dancer">
                    <div class="d-head"></div>
                    <div class="d-body"></div>
                    <div class="d-arm left"></div>
                    <div class="d-arm right"></div>
                    <div class="d-leg left"></div>
                    <div class="d-leg right"></div>
                </div>

                <div class="equipment treadmill">
                    <div class="tm-base"><div class="belt"></div></div>
                    <div class="tm-post"></div>
                    <div class="tm-console"></div>
                </div>

                <div class="runner">
                    <div class="head"></div>
                    <div class="body"></div>
                    <div class="arm a1"></div>
                    <div class="arm a2"></div>
                    <div class="leg l1"></div>
                    <div class="leg l2"></div>
                </div>

                <div class="equipment corner">
                    <div class="mat"></div>
                    <div class="kettlebell"></div>
                    <div class="plant">
                        <div class="leaf one"></div>
                        <div class="leaf two"></div>
                        <div class="leaf three"></div>
                        <div class="pot"></div>
                    </div>
                </div>
            </div>
        </div>

        <div class="footer-message">
            <span class="typed">
                Wishing Kstudio many more years of success, transformation, friendship, and powerful gym memories. ❤️
            </span>
        </div>
    </div>

<script>
    const stars = document.getElementById('stars');
    const confetti = document.getElementById('confetti');
    const hearts = document.getElementById('hearts');

    const confettiColors = ['#ffd166', '#ff7eb6', '#72e6ff', '#7dff9b', '#b690ff', '#ffffff'];
    const heartIcons = ['❤', '💛', '💗', '✨'];

    for (let i = 0; i < 48; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 70 + '%';
        star.style.animationDelay = (Math.random() * 2) + 's';
        stars.appendChild(star);
    }

    for (let i = 0; i < 34; i++) {
        const piece = document.createElement('div');
        piece.className = 'confetti-piece';
        piece.style.left = Math.random() * 100 + '%';
        piece.style.background = confettiColors[Math.floor(Math.random() * confettiColors.length)];
        piece.style.animationDuration = (4 + Math.random() * 4) + 's';
        piece.style.animationDelay = (-Math.random() * 8) + 's';
        confetti.appendChild(piece);
    }

    for (let i = 0; i < 18; i++) {
        const heart = document.createElement('div');
        heart.className = 'heart';
        heart.textContent = heartIcons[Math.floor(Math.random() * heartIcons.length)];
        heart.style.left = Math.random() * 100 + '%';
        heart.style.animationDuration = (5 + Math.random() * 5) + 's';
        heart.style.animationDelay = (-Math.random() * 10) + 's';
        hearts.appendChild(heart);
    }
</script>
</body>
</html>
'''

components.html(html, height=1180, scrolling=False)
