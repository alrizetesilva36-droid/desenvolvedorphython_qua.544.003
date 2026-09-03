import pyautogui as auto
from datetime import date


def hoje():
    return date.today().strftime("%d/%m/%Y")

def main():
    auto.PAUSE = 1

    auto.press("win")
    auto.write("cmd")
    auto.press("enter")
    auto.write("cd c:/Users/ALUNO/Alrizete/desenvolvedorphython_qua.544.003")
    auto.press("enter")
    auto.write("git add .")
    auto.press("enter")
    auto.write(f'git commit -m "{hoje()}"')
    auto.press("enter")
    auto.write("git push")
    auto.sleep(3)
    auto.press("enter")
    auto.write("exit")
    auto.press("enter")
    


if __name__ == "__main__":
    main()