# Settings
## Git , Git Bash , Vscode (Visual Studio for Code) 다운 & 연동
https://www.youtube.com/watch?v=lelVripbt2M

## Installed list
(zlib은 Pillow 설치를 위치한 것이고, Pillow는 Tkdesigner에서 사용하는 이미지 처리 라이브러리)

https://pypi.org/project/tkdesigner/1.0.7/ (1.0.7 Latest version)
https://www.zlib.net/ ( zlib source code, version 1.3.1, zipfile format (1616K, SHA-256 hash 72af66d44fcc14c22013b46b814d5d2514673dda3d115e64b690c1ad636e7b17):)
Pillow==10.3.0

# Process Notes
## README.md 작성
https://www.youtube.com/watch?v=MFJIOqxK6k8
https://gist.github.com/ihoneymon/652be052a0727ad59601
https://www.youtube.com/watch?v=oLxFqpUbaAE

# Python Gui 

## Open the Python Gui after Figma
TKDESIGNER 실행
```windowpowershell
 cd Tkinter-Designer
```
```windowpowershell
 pip install -r requirements.txt
```
```windowpowershell
 cd gui
```
```windowpowershell
 python gui.py
```

## Using TkDesigner with Figma (python)
https://velog.io/@alirz-pixel/tkinter-designer-%EC%82%AC%EC%9A%A9%EB%B2%95-%EB%B0%8F-%EC%A3%BC%EC%9D%98%EC%82%AC%ED%95%AD
https://denev6.tistory.com/entry/tkinter-palette

## Figma to Tkdesinger by ParthJadhav (orgn)
https://www.youtube.com/watch?v=Qd-jJjduWeQ

### Formatting Figma Design 

### {1} Reference

##### Naming is Important
|FIgma Element Name|Tkinter Element|-|
|:--:|:--:|:--:|
|Button|Button|(Same)|
|Line|Line|(Same)|
|Text|Name it anything|-|
|Rectangle|Rectangle|(Same)|
|TextArea|Text Area|(Same)|
|TextBox|Entry|-|
|Image|Canvas.Image()|-|

### {2} After Make a UI in Figma : Generate Figma to TkDesigner
1. Figma 접속 -> [Setting]-> [Account] -> [Personal ]access token] -> [Generate a New Token] -> Name your New token -> [(copy this token)] : will be the [Token ID] -> copy the URL of your board that you finished : will be the [FIle URL]
2. Open your window powershell and open the tkdesigner
   ```windowpowershell
    python gui.py
   ```
3. Paste the Token ID and File Url and set the Output Path and Generate

### {3} Oopen your buil File
1. Open the windowpowershell
2. open python gui.py
    ```windowpowershell
   python gui.py
   ```
3. cd paste the output path then it will be looks like PS C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\figma_to_tkdesigner> 
   ```windowpowershell
   cd "C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\figma_to_tkdesigner"
   ```
4. check the files inside that path with ls (for mac os) or dir (for window os)
   ```windowpowershell
   dir
   ```
5. go to build and clear
   ```windowpowershell
   cd build
   ```
6. open all files wint open . (for mac os) or explorer . (for window os) <- . mean all
   ```windowpowershell
   explorer .
   ```
-> then you can see the 'build' folder. In there, your assets will be at assets folder and generated code for python gui as 'gui'file.

7. Open Python Gui
   ```windowpowershell
   python gui.py
   ```
-> THen you can see what you created on your Figma board

#### Example
```windowpowershell
PS C:\Users\MSI> cd "C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\figma_to_tkdesigner"
PS C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\figma_to_tkdesigner> dir


    디렉터리: C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\figma_to_tkdesigner


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2024-06-08   오전 4:02                build


PS C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\figma_to_tkdesigner> cd build
PS C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\figma_to_tkdesigner\build> explorer .
PS C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\figma_to_tkdesigner\build> python gui.py
```
![figma_to_tk_open_example](https://github.com/JinieFerry/instant_jinie_voice_final_ciritic/assets/166553319/68ca7bf7-b1c8-42de-9d74-df1ad90ad4e3)



# Codes

### KU'S ORIGIN_TextInput
##### original code by Ku
```python

# Import the tkinter module
from tkinter import * 
from elevenlabs import play
from elevenlabs.client import ElevenLabs

# Creating the GUI window.
window = Tk()
window.title("Welcome to geeksforgeeks")
window.geometry("800x100")

client = ElevenLabs(
	api_key="e75347c1353dd3083be81b47c4705fd6", # Defaults to ELEVEN_API_KEY
)

# Creating the function to set the text 
# with the help of button
def set_text_by_button():

	# Delete is going to erase anything
	# in the range of 0 and end of file,
	# The respective range given here
	#sample_text.delete(0,"end")
	
	# Insert method inserts the text at
	# specified position, Here it is the
	# beginning
	#sample_text.insert(0, sample_text.get())
	#print(sample_text.get())	

	audio = client.generate(
		text=sample_text.get(),
  		#text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
  		voice="Rachel", # try Nicole
  		model="eleven_multilingual_v2"
	)
	play(audio)

# Creating our text widget.
sample_text = Entry(window)
sample_text.pack()

# Setting up the button, set_text_by_button() 
# is passed as a command
set_up_button = Button(window, height=1, width=10, text="Set", 
					command=set_text_by_button)

set_up_button.pack()

window.mainloop()
```

# Error Notes

## Git and Git Hub Download . Install . Set up

https://www.youtube.com/watch?v=lelVripbt2M&t=309s

Visual Studio for Code Download - select the file - ‘terminal’ - New Terminal 

https://wikidocs.net/195273

https://ebbnflow.tistory.com/196

https://zzingonglog.tistory.com/10

1 ) 터미널에서 복사, 붙여넣기가 안될 때는 Ctrl + Shift + C & V 

2 ) 그래도 붙여넣기가 안된다면 Shift + Insert

##Pillow 8.4.0 Error History

### 깃 포기 전까지 대화 백업링크

https://chatgpt.com/share/b4f8d632-bb17-4b47-a7b0-19d732c2d15b

### Figma-PythonGui
Python Gui with Figma → Tkinter
https://blog.naver.com/yug311861/222915865128

### tkdesigner install error history (fixed)
pip install tkdesigner코드를 이용해 다운로드 하려했지만, 

```python
Failed to build Pillow
ERROR: Could not build wheels for Pillow, which is required to install pyproject.toml-based projects
PS C:\Users\MSI>
```
 1. 위의 에러가 지속적으로 발생함.
->(GPT 피드백) Pillow 설치 중에 발생한 문제로 보입니다. Pillow은 Python 이미지 처리 라이브러리이며, 대부분의 경우 pip를 통해 쉽게 설치할 수 있습니다. 그러나 현재 Pillow이 Python 3.11을 지원하지 않는 것으로 보입니다.

 2.PILLOW에 맞춰 파이썬 버전을 낮춰서 대설치해도 같은 문제 반복
-> (GPT 피드백) 이 문제는 Pillow을 설치하기 위해 필요한 zlib의 헤더 또는 라이브러리 파일을 찾을 수 없다는 것을 나타냅니다. 이는 Windows에서 Pillow을 컴파일하는 데 필요한 외부 종속성이 없는 경우 발생할 수 있습니다.

이 문제를 해결하기 위해서는 zlib 라이브러리를 설치하고 그 위치를 Pillow에 알려주어야 합니다. 일반적으로 zlib은 이미 Windows에 설치되어 있지만, Pillow이 해당 위치를 찾을 수 있도록 환경 변수를 설정해야 할 수 있습니다.

3. Zlib 직접 다운로드
zlib 최신버전을 다운로드해, 인스턴트 지니 보이스를 만들고 있는 폴더, (C:\Users\MSI\Desktop\instant_jinie_voice_finalPt)에 저장, 압축해제함.

4.zlib 라이브러리가 설치된 위치를 Pillow에 알려주기 위한 환경 변수설정
제어판 → 시스템 및 보안 → 시스템 → 고급 시스템 설정 → 환경 변수
시스템 변수 중에서 "Path"를 찾아 선택한 후 편집을 클릭합니다.
zlib 라이브러리가 설치된 디렉토리("C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\zlib131"
#Installed list")를 추가했음.

5.pip install Pillow==8.3.2 시도 & 같은 에러 다시 발생
에러코드
```
        File "<string>", line 1035, in <module>
      RequiredDependencyException:

      The headers or library files could not be found for zlib,
      a required dependency when compiling Pillow from source.

      Please see the install instructions at:
         https://pillow.readthedocs.io/en/latest/installation.html


      <string>:46: RuntimeWarning: Pillow 8.3.2 does not support Python 3.11 and does not provide prebuilt Windows binaries. We do not recommend building from source on Windows.
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for Pillow
Failed to build Pillow
ERROR: Could not build wheels for Pillow, which is required to install pyproject.toml-based projects
```

-> (GPT)설정한 시스템 변수에 zlib 라이브러리의 경로를 추가한 것은 올바른 접근입니다. 하지만, Pillow이 해당 위치를 올바르게 인식하지 못할 수도 있습니다. Pillow에게 직접 zlib의 위치를 알려주는 방법이 있습니다. 아래와 같은 방법으로 시도해 볼 수 있습니다.

Pillow 설치 시에 zlib의 위치를 명시적으로 지정하는 방법:
bash
```
pip install --global-option="build_ext" --global-option="--include-dirs=C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\zlib131" --global-option="--library-dirs=C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\zlib131" pillow
```
위 명령어에서 --include-dirs 옵션은 zlib 헤더 파일이 위치한 경로를 지정하고, --library-dirs 옵션은 zlib 라이브러리 파일이 위치한 경로를 지정합니다.

6. 5.의 코드로 zlib 위치 직접 지정해 pillow 낮은 버전 설치 후, 삭제하고 최신버전 설치로 해결 (Pillow 설치 완료)
입력한 코드

##6-1
```window Powershell
   pip install --global-option="build_ext" --global-option="--include-dirs=C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\zlib131" --global-option="--library-dirs=C:\Users\MSI\Desktop\instant_jinie_voice_finalPt\zlib131" pillow
```
결과:
Requirement already satisfied: pillow in c:\users\msi\appdata\local\programs\python\python311\lib\site-packages (10.3.0)

6-2
```
pip uninstall pillow
```
```
pip install pillow
```
결과:
  Successfully uninstalled pillow-10.3.0

6-3
위의 과정 다시 시도했을 때 다시 에러발생
에러:
```powershell
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pillow
Failed to build pillow
ERROR: Could not build wheels for pillow, which is required to install pyproject.toml-based projects
```
-> 상위버전 지정해서 설치

```powershell
pip install pillow==10.3.0
```

결과:
PS C:\Users\MSI> pip install pillow==10.3.0
Collecting pillow==10.3.0
  Using cached pillow-10.3.0-cp311-cp311-win_amd64.whl.metadata (9.4 kB)
Using cached pillow-10.3.0-cp311-cp311-win_amd64.whl (2.5 MB)
Installing collected packages: pillow
Successfully installed pillow-10.3.0

7. tkdesigner 설치 계속해서 오류 (pillow 10.3.0 설치 후에도 같은 에러 반복)
-> tkdesigner 직접 설치 (실패)
https://packaging.python.org/en/latest/tutorials/installing-packages/

에러코드:
```
      <string>:46: RuntimeWarning: Pillow 8.4.0 does not support Python 3.11 and does not provide prebuilt Windows binaries. We do not recommend building from source on Windows.
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for Pillow
Failed to build Pillow
ERROR: Could not build wheels for Pillow, which is required to install pyproject.toml-based projects
```

7-1
Ensure you can run Python from the command line
```powershell
py --version
```
Ensure you can run pip from the command lin
```powershell
py -m pip --version
```
Ensure pip, setuptools, and wheel are up to date
```powershell
py -m pip --version
```
Optionally, create a virtual environment
```powershell
py -m venv tutorial_env
tutorial_env\Scripts\activate
```

8. Git Clone 이용한 WINDOW POWERSHELL에서의 TKDESIGNER 직접 설치
https://www.youtube.com/watch?v=oLxFqpUbaAE&t=236s (실패)
https://blog.naver.com/yug311861/222915865128(실패)
https://github.com/ParthJadhav/Tkinter-Designer
TKDESIGNER 설치
```powershell
git clone https://github.com/ParthJadhav/Tkinter-Designer.git
```
```powershell
 cd Tkinter-Designer
```
```powershell
pip install -r requirements.txt
```

TKDESIGNER 실행
```POWERSHELL
cd gui
```

```python gui
python3 gui.py
```
->결과: TKDESIGNER 프로그램 안뜸
```window powershell
PS C:\Users\MSI\Tkinter-Designer> cd gui
PS C:\Users\MSI\Tkinter-Designer\gui> python3 gui.py
Python
```

9. 드디어 TkinterDesigner실행 성공
-> 중립적으로 PYTHON 선언함으로써 성공 (python3 gui.py는 실행 실패 -> python gui.py는 실행성공)

```windowpowershell
PS C:\Users\MSI\Tkinter-Designer\gui> cd C:\Users\MSI\Tkinter-Designer\gui
```
```windowpowershell
PS C:\Users\MSI\Tkinter-Designer\gui> python gui.py
```


