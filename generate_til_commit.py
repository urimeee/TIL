import os
import sys
import subprocess
from datetime import datetime

# 카테고리별 챕터 또는 제목 리스트 (필요 시 확장 가능)
clean_code_chapters = {
    1: "깨끗한 코드",
    2: "의미 있는 이름",
    3: "함수",
    4: "주석",
    5: "형식 맞추기",
    6: "객체와 자료구조",
    7: "오류 처리",
    8: "경계",
    9: "단위 테스트",
    10: "클래스",
    11: "시스템",
    12: "창발성",
    13: "동시성",
    14: "점진적인 개선",
    15: "Junit 들여다보기",
    16: "깨끗한 코드",
    17: "부록: 나쁜 코드 사례",
}

def kebab_case(text):
    return text.replace(' ', '-').replace('/', '').replace(':', '').lower()

def create_markdown_file(filepath, title):
    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"> 📅 작성일: {datetime.now().strftime('%Y-%m-%d')}\n\n")
            f.write("## 📌 핵심 요약\n\n- \n\n## 🔍 예시 코드\n\n```js\n// 예시\n```\n\n## 💭 느낀 점\n\n- ")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("사용법: python generate_til_commit.py <카테고리> <챕터번호 또는 파일이름>")
        sys.exit(1)

    category = sys.argv[1].lower()
    identifier = sys.argv[2]

    try:
        if category == "clean-code" and identifier.isdigit():
            chapter_num = int(identifier)
            title = f"{chapter_num}장 {clean_code_chapters[chapter_num]}"
            filename = f"{chapter_num:02d}_{kebab_case(clean_code_chapters[chapter_num])}.md"
        else:
            title = identifier.replace("-", " ").title()
            filename = f"{kebab_case(identifier)}.md"

        filepath = os.path.join(category, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        create_markdown_file(filepath, title)

        print(f"✅ 파일 생성 및 커밋 완료!")
        print(f"📄 파일 경로: {filepath}")
        print(f"📝 문서 제목: {title}")


    except Exception as e:
        print(f"❌ 오류: {e}")
