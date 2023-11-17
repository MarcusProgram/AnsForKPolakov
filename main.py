
#############################################
################ НЕ ВАЖНО ###################
#############################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from colorama import Fore, init
import sys
from selenium.webdriver.common.keys import Keys
import random
import ctypes
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
print(f"{Fore.RED} Данная программа была написанна программистом MARCUS {Fore.RESET}{'\n'*10}")
sleep(2)



#███╗░░░███╗░█████╗░██████╗░░█████╗░██╗░░░██╗░██████╗
#████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝
#██╔████╔██║███████║██████╔╝██║░░╚═╝██║░░░██║╚█████╗░
#██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗██║░░░██║░╚═══██╗
#██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝╚██████╔╝██████╔╝
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░







sys.setrecursionlimit(2147483647)
init()



#############################################
#############################################
#############################################


def getlink(link):
    driver.get(link)


################# ПОДКЛЮЧАЮ ХРОМ И ДЕЛАЮ ЧТО БЫ В КОНСОЛИ НЕ БЫЛО ЛИШНЕГО #################
options = webdriver.ChromeOptions() 

for messages_eror in [0,1,2,3,4]:
    options.add_argument(f"log-level={messages_eror}")
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

###########################################################################################


colvo = int(input("Введите сколько всего заданий: "))
linkk = 'https://kpolyakov.spb.ru/school/ogetest2020/b9.htm?roistat_visit=3443029' # тут ваша ссылка

getlink(linkk)

def main():
    correct_answers = []
    try:
        for answer in range(1, 40):
            for task_index in range(1, colvo + 1):
                input_element_xpath = f'/html/body/div[3]/div/div[2]/form/div[{task_index}]/table/tbody/tr[3]/td/input[2]'
                driver.find_element(By.XPATH, input_element_xpath).send_keys(answer)

            driver.execute_script("checkAnswers(this.form);")

            for task_number in range(1, colvo + 1):
                element = driver.find_element(By.ID, f"q{task_number}")
                if "errans" not in element.get_attribute("class"):
                    correct_answers.append(f"Task number: {task_number} Answer: {answer}")

            getlink(linkk)

        sorted_tasks = sorted(correct_answers, key=lambda x: int(x.split()[2]))

        for task in sorted_tasks:
            print(task)

    except Exception as ex:
        print(ex, '\n\n')
    finally:
        driver.quit()

if __name__ == '__main__':
    main()
