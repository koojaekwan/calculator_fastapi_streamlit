import threading
import subprocess

def run_streamlit():
    subprocess.run(['streamlit', 'run', 'streamlit_app.py'])

def run_fastapi():
    subprocess.run(['uvicorn', 'api:app', '--reload', '--host=127.0.0.1'])


if __name__=="__main__":
    # Streamlit을 실행하는 스레드 시작
    streamlit_thread = threading.Thread(target=run_streamlit)
    streamlit_thread.start()

    # FastAPI를 실행하는 스레드 시작
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()

    # 두 스레드가 모두 종료될 때까지 대기
    streamlit_thread.join()
    fastapi_thread.join()
