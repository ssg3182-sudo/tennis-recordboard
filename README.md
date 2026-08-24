# 이수의 코트 — 실시간 테니스 기록관리 현황판

GitHub + Vercel + Firebase로 배포하는 실시간 동기화 버전입니다. 여러 기기에서 열어도 같은 데이터가 실시간으로 보이고, PIN을 아는 사람만 기록을 추가·수정할 수 있어요.

## 이 프로젝트의 구조

```
index.html        ← 사이트 전체 (디자인 + 로직, Firebase 연동 포함)
api/login.js       ← PIN 확인 후 로그인 토큰을 발급하는 서버 함수 (Vercel이 실행)
package.json        ← api/login.js가 필요로 하는 라이브러리 목록
firestore.rules     ← Firebase 데이터베이스 보안 규칙
data.json           ← 지금까지의 기록 (최초 1회 업로드용, index.html 안에도 이미 포함되어 있어요)
```

전체 흐름: **GitHub**(코드 저장) → **Vercel**(사이트 배포 + PIN 로그인 서버) → **Firebase**(실제 기록 데이터 저장 + 실시간 동기화).

---

## 1단계. Firebase 프로젝트 만들기

1. https://console.firebase.google.com 접속 → 구글 계정으로 로그인 → **프로젝트 추가**
2. 프로젝트 이름 입력 (예: `isu-tennis`) → Google Analytics는 꺼도 무방 → 만들기

## 2단계. Firestore 데이터베이스 켜기

1. 왼쪽 메뉴 **빌드 > Firestore Database** → **데이터베이스 만들기**
2. 위치(리전)는 `asia-northeast3 (서울)` 선택 추천
3. 보안 규칙은 일단 아무 모드로 시작해도 괜찮아요 (바로 다음 단계에서 우리가 직접 규칙을 덮어씁니다)
4. 데이터베이스가 만들어지면 **규칙(Rules)** 탭으로 이동 → 이 프로젝트의 `firestore.rules` 파일 내용을 전체 복사해서 붙여넣기 → **게시(Publish)**

## 3단계. 웹 앱 등록하고 설정값 받기

1. Firebase 콘솔 왼쪽 위 톱니바퀴 ⚙️ → **프로젝트 설정**
2. 아래로 스크롤 → **내 앱** → 웹 아이콘(`</>`) 클릭 → 앱 닉네임 입력(아무거나, 예: `tennis-web`) → 앱 등록
3. `firebaseConfig` 라는 값이 화면에 나타나요. 이 안의 `apiKey`, `authDomain`, `projectId`, `storageBucket`, `messagingSenderId`, `appId` 값을 그대로 복사
4. `index.html` 파일을 열어서 `FIREBASE_CONFIG` 부분을 찾아 (파일 안에서 "YOUR_API_KEY"로 검색하면 바로 찾을 수 있어요) 위에서 복사한 값으로 교체

   ```js
   var FIREBASE_CONFIG = {
     apiKey: "여기에 붙여넣기",
     authDomain: "여기에 붙여넣기",
     projectId: "여기에 붙여넣기",
     storageBucket: "여기에 붙여넣기",
     messagingSenderId: "여기에 붙여넣기",
     appId: "여기에 붙여넣기"
   };
   ```

   이 값들은 브라우저에 그대로 노출되어도 괜찮은 "공개 식별자"예요. 실제 접근 제한은 Firestore 규칙과 PIN 로그인이 담당합니다.

5. Firebase 콘솔 왼쪽 메뉴 **빌드 > Authentication** 을 한 번 열어서 **시작하기** 버튼을 눌러주세요 (별도 로그인 방식을 켤 필요는 없고, 이 메뉴를 한 번 열어야 인증 기능 자체가 프로젝트에서 활성화돼요).

## 4단계. 서비스 계정 키 만들기 (PIN 로그인 서버용)

1. Firebase 콘솔 ⚙️ **프로젝트 설정 > 서비스 계정** 탭
2. **새 비공개 키 생성** 클릭 → JSON 파일이 다운로드돼요. 이 파일은 절대 GitHub에 올리지 말고 안전하게 보관하세요.
3. 다운로드한 JSON을 열어보면 아래 세 값이 들어있어요 (5단계에서 Vercel에 등록할 값이에요).
   - `project_id`
   - `client_email`
   - `private_key`

## 5단계. GitHub에 올리기

1. https://github.com 에서 새 저장소(Repository) 생성 (예: `isu-tennis-live`), Private으로 만드는 걸 추천해요.
2. 이 폴더의 파일 전체(`index.html`, `api/login.js`, `package.json`, `firestore.rules`, `.gitignore`, `data.json`, `README.md`)를 그 저장소에 업로드 (GitHub Desktop을 쓰거나, 웹에서 "Add file > Upload files"로도 가능해요).

## 6단계. Vercel에 배포하기

1. https://vercel.com 접속 → GitHub 계정으로 로그인
2. **Add New > Project** → 방금 만든 GitHub 저장소 선택 → Import
3. Framework Preset은 **Other**로 두고 그대로 **Deploy** (index.html이 루트에 있으므로 별도 빌드 설정이 필요 없어요)
4. 배포가 끝나기 전에, 같은 화면(또는 배포 후 프로젝트 **Settings > Environment Variables**)에서 아래 4개 환경변수를 추가하세요.

   | 이름 | 값 |
   |---|---|
   | `TENNIS_PIN` | 원하는 PIN 번호 (예: `2580` — 직접 정하세요) |
   | `FIREBASE_PROJECT_ID` | 서비스 계정 JSON의 `project_id` |
   | `FIREBASE_CLIENT_EMAIL` | 서비스 계정 JSON의 `client_email` |
   | `FIREBASE_PRIVATE_KEY` | 서비스 계정 JSON의 `private_key` 값 전체 (`-----BEGIN PRIVATE KEY-----`부터 `-----END PRIVATE KEY-----\n`까지, 줄바꿈이 `\n`으로 되어있는 그대로 큰따옴표 없이 붙여넣기) |

5. 환경변수를 저장한 뒤 **Deployments** 탭에서 **Redeploy** (환경변수는 재배포해야 적용돼요).
6. 배포가 끝나면 `https://your-project.vercel.app` 같은 주소가 생겨요. 이 주소가 실제 사용할 사이트 링크예요.

## 7단계. 첫 접속 & 데이터 올리기

1. 배포된 주소로 접속하면 지금까지의 기록이 그대로 보여요 (사이트 안에 미리 담아둔 데이터라 최초 1회는 인터넷 연결 없이도 보입니다).
2. 오른쪽 위 **🔒 관리자 로그인** 클릭 → 6단계에서 정한 PIN 입력
3. 로그인에 성공하면 그 순간 지금까지의 기록이 자동으로 Firebase에 한 번 업로드돼요 (저장 상태 배지에 "저장 중…" → "저장됨"이 표시됩니다). 이후부터는 모든 기록이 Firebase에 실시간으로 저장·동기화됩니다.
4. 다른 기기(휴대폰, 다른 컴퓨터)에서 같은 주소로 접속하면 실시간으로 같은 기록을 볼 수 있고, PIN으로 로그인한 사람만 수정할 수 있어요.

---

## 이후 사용법

- **기록 보기**: 누구나 링크로 접속해서 볼 수 있어요 (로그인 불필요).
- **기록 추가/수정**: 🔒 관리자 로그인 → PIN 입력 → "+ 대회 추가" 버튼이나 각 대회의 ✏️ 아이콘으로 편집.
- **로그아웃**: 로그인 상태에서 같은 버튼(🔓 로그아웃)을 다시 누르면 로그아웃돼요.
- **PIN을 바꾸고 싶을 때**: Vercel 프로젝트 Settings > Environment Variables에서 `TENNIS_PIN` 값을 수정하고 다시 배포(Redeploy)하면 돼요.
- **디자인/문구를 바꾸고 싶을 때**: `index.html`을 직접 수정한 뒤 GitHub에 다시 올리면 Vercel이 자동으로 재배포해요.
- **`build.py`에 대해**: 이 파일은 참고용 생성 스크립트예요 (평소에는 실행할 필요가 없어요). 만약 나중에 `python3 build.py`를 다시 실행하면 `index.html`이 처음 상태(FIREBASE_CONFIG가 `YOUR_...` placeholder인 상태)로 새로 만들어지니, 다시 실행했다면 3단계의 FIREBASE_CONFIG 값을 한 번 더 채워 넣어야 해요.

## 참고사항

- 이 구조는 "PIN을 아는 사람은 모두 같은 편집 권한"을 갖는 간단한 방식이에요. 가족 안에서 공유하는 용도로는 충분하지만, 아주 민감한 데이터를 위한 강력한 보안은 아니에요.
- 두 사람이 동시에 저장하면 나중에 저장한 내용이 앞선 내용을 덮어써요(마지막 저장이 우선). 여러 명이 동시에 활발히 편집할 상황이 아니라면 문제되지 않아요.
- Firebase 무료 요금제(Spark)로도 이 정도 사용량은 충분히 감당돼요.
