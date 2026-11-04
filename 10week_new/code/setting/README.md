# setup_dl2026.sh 사용법

강의실 PC가 초기화되어 실습 환경(가상환경·Git 저장소·패키지)이 사라졌을 때, 한 번에 다시 만드는 Git Bash 스크립트입니다.

---

## 1. 이 스크립트가 하는 일

| 단계 | 내용 | 입력 |
|---|---|---|
| 1 | 스크립트가 놓인 폴더를 **작업 기준 폴더(DL2026_HOME)** 로 정하고, 쓰기 권한 확인 | 없음 |
| 2 | 그 아래에 새 작업 폴더 생성 | 폴더 이름 |
| 3 | `python -m venv venv` 로 가상환경 생성 후 활성화 | (필요할 때) y/n |
| 4 | Git 저장소 설정: `git init` → 이름·이메일(`--local`) → 원격 주소(origin) → 원격 `main` 내려받기 → `.gitignore` 생성 | 이름, 이메일, 원격 주소 |
| 5 | 2주차 패키지 설치: `jupyterlab ipykernel numpy pandas matplotlib humanize` | 없음 (수 분 대기) |
| 6 | 나머지 할 일을 **명령어로 안내** (①~⑦) | 직접 입력 |

> 입력은 1~4단계에서 모두 받습니다. 5단계부터는 기다리기만 하면 됩니다.

**자동으로 하지 않는 것** (6단계에서 명령어만 보여 줌)
- 가상환경 다시 활성화 (스크립트가 끝나면 활성화가 풀림)
- PyTorch 설치
- 주피터 커널 등록
- Git 공용 PC 설정(`--global`)
- 첫 push / 저장소 확인
- JupyterLab 실행, 수업 후 뒷정리

---

## 2. 준비물

- **Python 3.13.x** (다른 버전이면 경고 후 계속할지 물어봄)
- **Git for Windows** (Git Bash 포함). 없으면 4단계를 건너뛰고 나머지만 진행
- 인터넷 연결 (패키지 설치)
- GitHub 계정과 저장소 주소 (없으면 4단계에서 Enter로 건너뛰고 나중에 연결)

---

## 3. 실행 방법

### 3-1. 스크립트를 바탕화면 > 딥러닝 폴더에 넣기

스크립트가 **놓인 폴더**가 작업 기준 폴더(DL2026_HOME)가 됩니다. 수업에서는 **바탕화면에 `딥러닝` 폴더**를 만들고 그 안에 스크립트를 넣습니다.

1. 바탕화면에서 마우스 오른쪽 → **새로 만들기 → 폴더** → 이름을 `딥러닝` 으로
2. 공유 폴더의 `setup_dl2026.sh` 를 `딥러닝` 폴더 안으로 복사

```
바탕화면
└─ 딥러닝
   ├─ setup_dl2026.sh          ← 여기에 넣는다
   └─ 20261234_hong            ← 스크립트가 2단계에서 만든다 (내 작업 폴더)
      └─ venv
```

Git Bash 로 복사하려면 (공유 폴더에서 Git Bash 를 연 상태):

```bash
mkdir -p ~/Desktop/딥러닝
cp setup_dl2026.sh ~/Desktop/딥러닝/
```

> `딥러닝` 폴더 이름은 한글이어도 괜찮습니다. 한글·공백을 쓰면 안 되는 것은 2단계에서 입력하는 **내 작업 폴더 이름**입니다.

### 3-2. Git Bash에서 실행

탐색기에서 `딥러닝` 폴더를 열고, 빈 곳에서 마우스 오른쪽 → **추가 옵션 표시 → Open Git Bash here** 를 누른 뒤:

```bash
bash setup_dl2026.sh
```

Git Bash 를 이미 열어 두었다면 `cd ~/Desktop/딥러닝` 으로 이동한 뒤 같은 명령을 입력합니다.

1단계에 `DL2026_HOME = C:\Users\<계정>\Desktop\딥러닝` 처럼 나오면 정상입니다.

> **경로에 `OneDrive` 가 보이면** (예: `C:\Users\<계정>\OneDrive\바탕 화면\딥러닝`) 바탕화면이 OneDrive 와 동기화되는 PC입니다. venv 와 PyTorch(약 2.5GB)가 계속 업로드되어 느려지므로, `Ctrl+C` 로 멈추고 같은 Git Bash 창(`딥러닝` 폴더)에서 아래처럼 `C:\dl2026` 으로 옮겨 실행하세요.
> ```bash
> mkdir -p /c/dl2026
> cp setup_dl2026.sh /c/dl2026/
> cd /c/dl2026
> bash setup_dl2026.sh
> ```
> 2단계에서 `[경고] 작업 폴더 경로가 깁니다` 가 나올 때도 같은 방법으로 옮겨 실행합니다.

또는 탐색기에서 `setup_dl2026.sh` 를 더블클릭합니다 (Git 설치 때 `.sh` 연결을 켠 경우 Git Bash로 열림). 더블클릭으로 연 창은 끝에서 `Enter 를 누르면 끝납니다...` 에서 멈추므로, 안내를 다 읽은 뒤 Enter를 누르세요.

---

## 4. 단계별 입력 안내

### 2단계 — 폴더 이름
- 영문·숫자·`_`·`-` 만 사용 (한글·공백 불가)
- 예: `20261234_hong`
- 이미 있는 폴더면 `그대로 사용할까요? (y/n)` → `y` 면 그 폴더를 계속 씀

### 3단계 — 가상환경
- 폴더에 `venv` 가 이미 있으면 `y`: 지우고 새로 만들기 / `n`: 그대로 사용
- `venv` 를 지울 수 없다고 나오면 JupyterLab·다른 터미널·탐색기를 닫고 다시 실행

### 4단계 — Git
| 질문 | 입력 예 | 비고 |
|---|---|---|
| 이름 | `Hong Gildong` | 큰따옴표(`"`) 불가 |
| GitHub 이메일 | 본인 GitHub에 등록한 이메일 | 그래야 커밋이 내 잔디(Contributions)에 기록됨. `@example.com` 은 거부 |
| 원격 주소 | `https://github.com/아이디/deeplearning-study-2026.git` | GitHub 저장소 페이지 → 초록색 **Code** 버튼 → HTTPS 주소 복사. 없으면 Enter |

- 이름·이메일은 **이 저장소에만(`--local`)** 저장합니다. 공용 PC이므로 `--global` 에는 넣지 않습니다.
- 원격에 지난주까지의 커밋(`main`)이 있으면 자동으로 내려받습니다. 로그인 창은 띄우지 않고 시도만 하므로, 비공개 저장소는 여기서 실패할 수 있습니다 (6단계 ⑤에서 직접 받음).
- `.gitignore` 가 없으면 새로 만들고, 있으면 `venv/` `__pycache__/` `.ipynb_checkpoints/` `.env` 중 빠진 항목만 덧붙입니다.
- 마지막에 `venv/ : Git 에서 제외됨 (정상)` 이 보이면 성공입니다.

---

## 5. 스크립트가 끝난 뒤 직접 할 일

스크립트 끝에 아래 명령이 순서대로 나옵니다. **VSCode 터미널을 Git Bash로 열고** 그대로 입력하세요.
(VSCode 터미널 오른쪽 위 `+` 옆 `∨` → **Git Bash** 선택)

### ① 작업 폴더로 이동 + 가상환경 활성화
```bash
cd ~/Desktop/딥러닝/20261234_hong      # C:\dl2026 에서 실행했다면  cd /c/dl2026/20261234_hong
source venv/Scripts/activate
# 프롬프트 위에 (venv) 가 보이면 성공. 끌 때는 deactivate
```

### ② PyTorch 설치 (GPU 판) — `(venv)` 가 보이는 상태에서
```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
# 2.x.x+cu126 True 가 나오면 성공 (+cpu 나 False 면 손을 들어 알리기)
```
약 2.5GB를 내려받으므로 5~20분 걸립니다. 터미널을 닫지 마세요.

### ③ 주피터 커널 등록
```bash
python -m ipykernel install --user --name dl2026 --display-name "Python (dl2026)"
jupyter kernelspec list
```

### ④ Git 공용 PC 설정
```bash
git config --global init.defaultBranch main
git config --global core.autocrlf true
git config --global core.quotepath false
git config --global user.useConfigOnly true
git config --global credential.helper manager
```

### ⑤ GitHub 저장소 확인 — 4단계 결과에 따라 안내가 달라짐
| 4단계 결과 | 해야 할 일 |
|---|---|
| 원격 `main` 을 내려받음 | `git status`, `git log --oneline -3` 으로 지난주 커밋 확인 |
| 원격 저장소가 비어 있음 | `git add .` → `git status` (venv 가 없어야 정상) → `git commit -m "week4: environment setup"` → `git push -u origin main` |
| 원격 주소를 건너뜀 | `git remote add origin <주소>` → `git pull origin main` → `git branch -u origin/main` |
| 내려받기 실패 | `git remote -v` 로 주소 확인 → `git pull origin main` (로그인 창이 뜨면 로그인) |
| git 이 없어 건너뜀 | Git 설치 후 스크립트를 다시 실행 (같은 폴더 이름, venv 는 `n`) |

내려받기가 `untracked working tree files would be overwritten` 로 멈추면, 목록에 나온 파일을 다른 이름으로 옮기고 다시 pull 합니다.
```bash
mv .gitignore .gitignore.bak
git pull origin main
rm .gitignore.bak
```

### ⑥ JupyterLab 실행
```bash
pip freeze > requirements.txt
jupyter lab
# 노트북 오른쪽 위 커널이 "Python (dl2026)" 인지 확인. 끌 때는 터미널에서 Ctrl+C
```

### ⑦ 수업이 끝나고 PC를 떠나기 전 (공용 PC)
```bash
git push
cmdkey /delete:git:https://github.com
```
두 번째 줄은 이 PC에 저장된 GitHub 로그인 정보를 지웁니다.

---

## 6. 10주차 실습을 하려면 추가로

스크립트는 **2주차 패키지까지만** 설치합니다. 10주차 LSTM 실습(`15_lstm_sentiment_*.ipynb`)에는 **scikit-learn** 이 더 필요하므로, 위 ②에서 PyTorch를 설치한 뒤 `code` 폴더의 `requirements.txt` 로 나머지를 설치합니다.

```bash
# (venv) 가 켜진 상태에서, 10week_new/code 폴더로 이동한 뒤
pip install -r requirements.txt
```

---

## 7. 자주 나는 문제

| 증상 | 원인·해결 |
|---|---|
| `python 을 실행할 수 없습니다` / Microsoft Store 가 열림 | 설정 → 앱 → 고급 앱 설정 → **앱 실행 별칭** 에서 `python.exe` 끄기. 설치가 안 되어 있으면 Python 3.13 설치 후 Git Bash를 새로 열기 |
| `[경고] 수업 기준 버전은 3.13.x 입니다` | 중단 후 `py -3.13 -m venv venv` 로 직접 만들거나, 그대로 계속(`y`) |
| `이 폴더에 쓸 수 없습니다` | 스크립트를 쓰기 가능한 폴더(예: `C:\dl2026`)로 옮겨 실행 |
| `[경고] 작업 폴더 경로가 깁니다` | 스크립트를 더 짧은 경로로 옮겨 실행 |
| `venv 를 지울 수 없습니다` | JupyterLab·다른 터미널·탐색기 창을 닫고 다시 실행 |
| `pip 업그레이드 실패` / `패키지 설치 실패` | 네트워크 확인 후 다시 실행 (같은 폴더 이름, venv 는 `n`) |
| WSL·macOS·Linux 에서 `$'\r': command not found` | 파일 줄바꿈이 CRLF로 바뀐 경우. `sed -i 's/\r$//' setup_dl2026.sh` (Git Bash 에서는 CRLF도 그대로 실행됨) |

> **다시 실행해도 안전합니다.** 같은 폴더 이름을 넣으면 기존 폴더·venv·Git 설정을 그대로 쓸지 하나씩 물어보므로, 중간에 실패한 단계부터 이어서 진행할 수 있습니다.

> 앞으로 자료에 나오는 `%DL2026_HOME%\venv` 는 **내 작업 폴더\venv** (예: `C:\Users\<계정>\Desktop\딥러닝\20261234_hong\venv`)로 바꿔 읽으세요. Git Bash 에서는 `~/Desktop/딥러닝/20261234_hong` 입니다.
