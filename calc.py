# tkinter 라이브러리 호출: tkinter의 함수를 쓸 수 있게 된다, as => tk로 부르겠다
import tkinter as tk
# 시간 라이브러리 호출
import time

#계산기의 오른쪽에 나올 문자들을 나열
num_list=['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '=']
#계산기의 왼쪽에 나올 문자들을 나열
op_list = ['*', '/', '+', '-', '(', ')', 'C', 'AC']

# num_list와 op_list를 합친 key_list 생성
key_list = num_list + op_list

# key_list에서 =, C, AC 를 제거
key_list.remove('AC')
key_list.remove('C')
key_list.remove('=')

# 키보드 입력시 실행되는 함수
def inputKey(key):
    # display를 입력 가능한 상태로 전환
    display.configure(state=tk.NORMAL)
    
    # 입력된 키가 key_list에 있는 키인 경우
    if key.char in key_list:
        # display_entry에 입력된 키 값을 추가
        display.insert(tk.END, key.char)
    # 입력된 키가 '=' 또는 엔터인 경우
    elif key.char == '=' or key.char == '\r':
        try:
            # 결과 값을 계산
            result = str(round(eval(display.get()), 2))
            # 메인 디스플레이를 지우고
            display.delete(0, tk.END)
            # 결과 값을 추가합니다.
            display.insert(tk.END, result)
        except:
            # 현재 display 수식을 임시로 저장
            result_tmp = display.get()
            # display 에 내용을 지웁니다
            display.delete(0, tk.END)
            # 안내 메시지를 표출
            display.insert(0, "계산할 수 없는 수식입니다")
            display.update()
            # 1초간 정지
            time.sleep(1)
            # display 내용을 지웁니다.
            display.delete(0, tk.END)
            # 임시로 저장해두었던 수식을 다시 보여주기
            display.insert(0, result_tmp)
    # 입력된 키가 'C'인 경우
    elif key.char == 'C' or key.char == 'c':
        # display 내용을 삭제
        display.delete(0, tk.END)
    # 입력된 키가 'A'인 경우
    elif key.char == 'A' or key.char == 'a':
        # display 내용을 삭제
        display.delete(0, tk.END)
        # 클립보드 1,2,3의 내용도 삭제
        clip1_entry.delete(0, tk.END)
        clip2_entry.delete(0, tk.END)
        clip3_entry.delete(0, tk.END)

    # BackSpace 키를 누른 경우
    if key.keysym == "BackSpace":
        # 현재 display_entry 글자 수를 구해서
        display_len = len(display.get())
        # 마지막 글자만 지운다
        display.delete(display_len-1, tk.END)
    
    # I1 키를 누른 경우
    if key.keysym == 'I1':
        # 클립보드1의 내용을 삭제
        clip1_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 1로 복사
        clip1_entry.insert(tk.END, display.get())
    # I2 키를 누른 경우
    elif key.keysym == 'I2':
        # 클립보드2의 내용을 삭제
        clip2_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 2로 복사
        clip2_entry.insert(tk.END, display.get())
    # I3 키를 누른 경우
    elif key.keysym == 'I3':
        # 클립보드3의 내용을 삭제
        clip3_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 3로 복사
        clip3_entry.insert(tk.END, display.get())
    # I4 키를 누른 경우
    elif key.keysym == 'I4':
        # 클립보드3의 내용을 삭제
        clip4_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 3로 복사
        clip4_entry.insert(tk.END, display.get())
    # O1 키를 누른 경우
    elif key.keysym == 'O1':
        # 클립보드1의 내용을 display에 추가
        display.insert(tk.END, clip1_entry.get())
        # 클립보드1의 내용 삭제
        clip1_entry.delete(0, tk.END)
    # O2 키를 누른 경우
    elif key.keysym == 'O2':
        # 클립보드2의 내용을 display에 추가
        display.insert(tk.END, clip2_entry.get())
        # 클립보드2의 내용 삭제
        clip2_entry.delete(0, tk.END)
    # O3 키를 누른 경우
    elif key.keysym == 'O3':
        # 클립보드3의 내용을 display에 추가
        display.insert(tk.END, clip3_entry.get())
        # 클립보드3의 내용 삭제
        clip3_entry.delete(0, tk.END)
    # O4 키를 누른 경우
    elif key.keysym == 'O4':
        # 클립보드3의 내용을 display에 추가
        display.insert(tk.END, clip4_entry.get())
        # 클립보드3의 내용 삭제
        clip4_entry.delete(0, tk.END)

    # display를 입력 불가능한 상태로 전환
    display.configure(state="readonly")

def click(text):
    # display를 입력 가능한 상태로 전환
    display.configure(state=tk.NORMAL)

    # text 값이 =인 경우
    if text == '=':
        try:
            # 결과 값을 계산
            # display.get() : display에 있는 글씨를 가져옴
            # eval(입력값) : 입력값을 수식으로 보고 계산을 한다
            # round(값, 2) : 값을 소수점 2자리로 반올림
            # str(숫자값) : 숫자를 문자로 변환
            result = str(round(eval(display.get()),2))
            # 메인 디스플레이를 지우고 
            display.delete(0, tk.END)
            # 결과 값을 추가합니다.
            # display의 가장 마지막에 result값 추가
            display.insert(tk.END, result)
        except:
            display.insert(tk.END, "=> 오류")
    # text 값이 C인경우
    elif text == 'C':
        # 메인 디스플레이를 지웁니다.
        display.delete(0, tk.END)
    elif text == 'AC':
         # 메인 디스플레이를 지웁니다.
        display.delete(0, tk.END)
         # 클립의 디스플레이도 모두 지움
        clip1_entry.delete(0, tk.END)
        clip2_entry.delete(0, tk.END)
        clip3_entry.delete(0, tk.END)
    else:
        # 그 외의 버튼을 누르면 그 버튼의 text 값을 entry에 출력
        display.insert(tk.END, text)

# F1~F6 키를 눌렀을 때 실행되는 함수
def funcClick(key):
    # display를 입력 가능한 상태로 전환
    display.configure(state=tk.NORMAL)
    
    # I1 키를 누른 경우
    if key == 'I1':
        # 클립보드1의 내용을 삭제
        clip1_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 1로 복사
        clip1_entry.insert(tk.END, display.get())
    elif key == 'I2':
        # 클립보드2의 내용을 삭제
        clip2_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 2로 복사
        clip2_entry.insert(tk.END, display.get())
    elif key == 'I3':
        # 클립보드3의 내용을 삭제
        clip3_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 3로 복사
        clip3_entry.insert(tk.END, display.get())
    elif key == 'I4':
        # 클립보드4의 내용을 삭제
        clip4_entry.delete(0, tk.END)
        # display Entry의 내용을 클립보드 3로 복사
        clip4_entry.insert(tk.END, display.get())
    elif key == 'O1':
        # 클립보드1의 내용을 display에 추가
        display.insert(tk.END, clip1_entry.get())
        # 클립보드1의 내용 삭제
        clip1_entry.delete(0, tk.END)
    elif key == 'O2':
        # 클립보드2의 내용을 display에 추가
        display.insert(tk.END, clip2_entry.get())
        # 클립보드2의 내용 삭제
        clip2_entry.delete(0, tk.END)
    elif key == 'O3':
        # 클립보드3의 내용을 display에 추가
        display.insert(tk.END, clip3_entry.get())
        # 클립보드3의 내용 삭제
        clip3_entry.delete(0, tk.END)
    elif key == 'O4':
        # 클립보드4의 내용을 display에 추가
        display.insert(tk.END, clip4_entry.get())
        # 클립보드4의 내용 삭제
        clip3_entry.delete(0, tk.END)

    # display를 입력 불가능한 상태로 전환
    display.configure(state="readonly")

#윈도우 만들기
calc = tk.Tk()
calc.title('Calculator')

# 메인 윈도우를 항상 위로
calc.attributes("-topmost", True)

# 디스플레이 생성
# Entry : 한 줄 짜리 입력창 // 어디에 만들지, 넓이는 얼마로 할 것인지, 색상은 무엇으로
# pack(), grid() 어떻게 배치할지
display = tk.Entry(calc,width=35, readonlybackground="light gray", bg="light gray")
display.grid(row=0, column=0, columnspan=2)
display.configure(state="readonly")

# 숫자 버튼을 넣을 프레임
num_frame = tk.Frame(calc)
num_frame.grid(row=1, column=0)

# 숫자 버튼을 넣어봅시다.

# num_list = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', '=']
row_num=0
column_num=0
for btn_text in num_list:
    def cmd(x = btn_text):
        click(x)
    tk.Button(num_frame, text=btn_text, width = 5, command = cmd).grid(row = row_num, column = column_num)
    column_num = column_num+1
    if column_num>2:
        column_num=0
        row_num=row_num+1
# tk.Button(num_frame, text="1", width=5).grid(row=0, column=0)
# tk.Button(num_frame, text="2", width=5).grid(row=1, column=0)
# tk.Button(num_frame, text="3", width=5).grid(row=2, column=0)
# tk.Button(num_frame, text="4", width=5).grid(row=0, column=1)
# tk.Button(num_ frame, text="5", width=5).grid(row=1, column=1)
# tk.Button(num_frame, text="6", width=5).grid(row=2, column=1)


# 연산자 버튼을 넣을 프레임
op_frame = tk.Frame(calc)
op_frame.grid(row=1, column=1)

# 연산자 버튼을 넣어봅시다.

# op_list = ['*', '/', '+', '-', '(', ')', 'C', 'AC']
row_num = 0
column_num = 0

for btn_text in op_list: 
    def cmd2(x=btn_text):
        click(x)
    tk.Button(op_frame, text=btn_text, width=5, command = cmd2).grid(row=row_num, column = column_num)
    column_num = column_num + 1
    if column_num > 1:
        column_num = 0
        row_num = row_num+1

# Event handling
# Event : 사용자의 동작에 따라 발생하는 신호

# 클립보드 프레임 생성 및 배치
clip_frame = tk.Frame(calc)
clip_frame.grid(row=2, column=0, columnspan=2, sticky='N')

# I1~I4, O1~O4 를 눌렀을 때 실행되는 함수
def cmd_I1():
    # 단순히 funcClick을 호출
    funcClick('I1')

def cmd_I2():
    # 단순히 funcClick을 호출
    funcClick('I2')

def cmd_I3():
    # 단순히 funcClick을 호출
    funcClick('I3')

def cmd_I4():
    # 단순히 funcClick을 호출
    funcClick('I4')

def cmd_O1():
    # 단순히 funcClick을 호출
    funcClick('O1')

def cmd_O2():
    # 단순히 funcClick을 호출
    funcClick('O2')

def cmd_O3():
    # 단순히 funcClick을 호출
    funcClick('O3')

def cmd_O4():
    # 단순히 funcClick을 호출
    funcClick('O4')

# 클립보드1 입출력 버튼, 엔트리 생성 및 배치
clip1_input_btn = tk.Button(clip_frame, width=2, text="I1", command=cmd_I1)
clip1_input_btn.grid(row=0, column=0)
clip1_entry = tk.Entry(clip_frame, width=20, bg="light green")
clip1_entry.grid(row=0, column=1)
clip1_output_btn = tk.Button(clip_frame, width=2, text="O5", command=cmd_O1)
clip1_output_btn.grid(row=0, column=2)

# 클립보드2 입출력 버튼, 엔트리 생성 및 배치
clip2_input_btn = tk.Button(clip_frame, width=2, text="I2", command=cmd_I2)
clip2_input_btn.grid(row=1, column=0)
clip2_entry = tk.Entry(clip_frame, width=20, bg="light blue")
clip2_entry.grid(row=1, column=1)
clip2_output_btn = tk.Button(clip_frame, width=2, text="O6", command=cmd_O2)
clip2_output_btn.grid(row=1, column=2)

# 클립보드3 입출력 버튼, 엔트리 생성 및 배치
clip3_input_btn = tk.Button(clip_frame, width=2, text="I3", command=cmd_I3)
clip3_input_btn.grid(row=2, column=0)
clip3_entry = tk.Entry(clip_frame, width=20, bg="light gray")
clip3_entry.grid(row=2, column=1)
clip3_output_btn = tk.Button(clip_frame, width=2, text="O7", command=cmd_O3)
clip3_output_btn.grid(row=2, column=2)

# 클립보드3 입출력 버튼, 엔트리 생성 및 배치
clip4_input_btn = tk.Button(clip_frame, width=2, text="I4", command=cmd_I4)
clip4_input_btn.grid(row=3, column=0)
clip4_entry = tk.Entry(clip_frame, width=20, bg="light pink")
clip4_entry.grid(row=3, column=1)
clip4_output_btn = tk.Button(clip_frame, width=2, text="O8", command=cmd_O4)
clip4_output_btn.grid(row=3, column=2)

calc.mainloop()