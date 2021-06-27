from selenium import webdriver
import time


def sending_msg_to_multi_contacts(contact,message,count):

    for indivi in contact:

        user = driver.find_element_by_xpath(f'//span[@title = "{indivi}"]')
        user.click()

        messagebox = driver.find_element_by_xpath('//div[@class = "_2A8P4"]')

        for i in range(count):
            messagebox.send_keys(message)
            sendbtn = driver.find_element_by_xpath('//button[@class = "_1E0Oz"]')
            sendbtn.click()

def replying_msg(contact,message):

    user = driver.find_element_by_xpath(f'//span[@title = "{contact}"]')
    user.click()

    #while True:

    for opposite_msg in driver.find_elements_by_xpath('//div[@class = "_2hqOq message-in focusable-list-item"]'):

        try:
            a = opposite_msg.find_element_by_xpath('.//div[@class = "_2et95 _3c94e _1dvTE"]')
            b = a.find_element_by_xpath('.//div[@class = "eRacY"]')

            if b.text:
                messagebox = driver.find_element_by_xpath('//div[@class = "_2A8P4"]')
                messagebox.send_keys(f"You sent : {b.text}")
                sendbtn = driver.find_element_by_xpath('//button[@class = "_1E0Oz"]')
                sendbtn.click()

        except Exception as e:
            print(e)
            continue

def main():

    try:
        choice = int(input("Press 1 to send message\nPresss 2 to reply to a incoming message\nEnter your choice = "))
        choice = 1
        if choice == 1:
            contact = input("Enter the contacts as comma-separated : ").rstrip().split(",") 
            message = input("Enter the message : ")
            count = int(input("Enter the count : "))
            sending_msg_to_multi_contacts(contact,message,count)

        elif choice == 2:

            contact = input("Enter the contact : ")
            message = input("Enter the message : ")

            replying_msg(contact,message=None)

        if input("Press 'r' to repeat this function : ") == "r":
            main()

        else:
            driver.quit()

    except Exception as e:
        print(e)
        driver.quit()



if __name__ == "__main__":

    options = webdriver.FirefoxOptions() 
    # options.add_argument('PATH FOR DEFAULT')
    # options.add_argument('--profile-directory=Default')

    # The executable path of geckodriver should be absolute path like /home/user/downloads/wh../geckodriver
    driver = webdriver.Firefox(executable_path= EXECUTABLE_PATH)

    driver.get("https://web.whatsapp.com")

    time.sleep(10)

    main()
