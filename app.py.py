from flask import Flask
import os  # Render의 포트 설정을 읽기 위해 필요합니다.

app = Flask(__name__)

# 공통 디자인 설정 (CSS)
STYLE = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
    body { font-family: 'Noto Sans KR', sans-serif; background-color: #f8f9fa; margin: 0; padding: 0; color: #333; }
    .header { background-color: #ffffff; padding: 20px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    h1 { color: #2d3436; font-size: 1.8rem; margin: 0; }
    .container { display: flex; flex-direction: column; align-items: center; padding: 30px 20px; }
    
    /* 카드 레이아웃 */
    .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; width: 100%; max-width: 1000px; }
    .card { background: white; border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 10px 20px rgba(0,0,0,0.05); transition: all 0.3s ease; text-decoration: none; color: inherit; display: block; }
    .card:hover { transform: translateY(-7px); box-shadow: 0 15px 30px rgba(0,0,0,0.1); }
    
    /* 아이콘 및 텍스트 */
    .icon { font-size: 3.5rem; margin-bottom: 20px; display: block; }
    .card h2 { margin: 10px 0; font-size: 1.4rem; color: #2d3436; }
    .card p { color: #636e72; font-size: 1rem; line-height: 1.5; margin: 0; }
    
    /* 상세 페이지 전용 */
    .detail-box { background: white; padding: 40px; border-radius: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); max-width: 600px; width: 90%; text-align: center; }
    .btn-home { display: inline-block; margin-top: 30px; padding: 12px 30px; background-color: #0984e3; color: white; text-decoration: none; border-radius: 50px; font-weight: bold; transition: background 0.2s; }
    .btn-home:hover { background-color: #74b9ff; }
    ul { text-align: left; display: inline-block; color: #2d3436; line-height: 2; margin-top: 20px; }
</style>
"""

# 1. 메인 페이지: 카드 메뉴
@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">{STYLE}</head>
    <body>
        <div class="header">
            <h1>🚶‍♂️ 스마트 보행기 시스템</h1>
        </div>
        <div class="container">
            <div class="card-grid">
                <a href="/location" class="card" style="border-bottom: 6px solid #00b894;">
                    <span class="icon">📍</span>
                    <h2>실시간 위치 확인</h2>
                    <p>보행기의 현재 위치와<br>이동 경로를 확인합니다.</p>
                </a>
                <a href="/danger" class="card" style="border-bottom: 6px solid #d63031;">
                    <span class="icon">⚠️</span>
                    <h2>위험 지역 알림</h2>
                    <p>주의가 필요한 장소를 파악하고<br>안전 사고를 예방합니다.</p>
                </a>
                <a href="/extra" class="card" style="border-bottom: 6px solid #0984e3;">
                    <span class="icon">✨</span>
                    <h2>부가 기능</h2>
                    <p>기기 상태 점검 및<br>보행 데이터를 관리합니다.</p>
                </a>
            </div>
        </div>
    </body>
    </html>
    """

# 2. 실시간 위치 확인 상세
@app.route("/location")
def location():
    return f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">{STYLE}</head>
    <body>
        <div class="container">
            <div class="detail-box">
                <span class="icon">📍</span>
                <h1>실시간 위치 확인</h1>
                <ul>
                    <li>✅ 구글 맵 기반 실시간 GPS 확인 </li>
                    <li>✅ 지정된 '안심 구역' 이탈 시 알림 발송</li>
                    <li>✅ 요일별/시간별 이동 경로 로그 기록</li>
                </ul>
                <br>
                <a href="/" class="btn-home">메인 화면으로</a>
            </div>
        </div>
    </body>
    </html>
    """

# 3. 위험 지역 알림 상세
@app.route("/danger")
def danger():
    return f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">{STYLE}</head>
    <body>
        <div class="container">
            <div class="detail-box">
                <span class="icon">⚠️</span>
                <h1>위험 지역 알림</h1>
                <ul>
                    <li>✅ 사고 다발 구역 진입 시 보호자 알림</li>
                    <li>✅ 보행기 센서를 통한 급경사 및 장애물 감지</li>
                    <li>✅ 위험 상황 자동 기록 및 알림</li>
                </ul>
                <br>
                <a href="/" class="btn-home">메인 화면으로</a>
            </div>
        </div>
    </body>
    </html>
    """

# 4. 부가 기능 상세
@app.route("/extra")
def extra():
    return f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">{STYLE}</head>
    <body>
        <div class="container">
            <div class="detail-box">
                <span class="icon">✨</span>
                <h1>부가 기능</h1>
                <ul>
                    <li>✅ 배터리 잔량 확인 및 교체 시기 알림</li>
                    <li>✅ 일일 걸음 수 및 보행 속도 통계 분석</li>
                    <li>✅ 기기 상태 원격 모니터링</li>
                </ul>
                <br>
                <a href="/" class="btn-home">메인 화면으로</a>
            </div>
        </div>
    </body>
    </html>
    """

# --- 서버 실행부 (Render 최적화) ---
if __name__ == "__main__":
    # Render는 PORT 환경 변수를 통해 포트를 지정합니다. 기본값은 5000으로 설정합니다.
    port = int(os.environ.get("PORT", 5000))
    # 외부 접속을 위해 host를 '0.0.0.0'으로 설정합니다.
    app.run(host='0.0.0.0', port=port)