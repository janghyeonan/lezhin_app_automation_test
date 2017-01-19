import os
import unittest
from appium import webdriver
from time import sleep

 
class lezhin_Tests(unittest.TestCase):    

    
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'        
        desired_caps['appPackage'] = 'com.lezhin.comics.plus'        
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
        
 
    def test_comics_mode(self):    
        #만화 부분
        sleep(5)
        print("\n 0. 만화 부분 시작!")
        sleep(1)
        print("\n 1.사이드 메뉴 클릭")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        print("\n 2.사이드 메뉴 활성화 완료!")        
        sleep(3)
        self.driver.get_screenshot_as_file("c:/result/01_test_comics_mode.png")

        print("\n 3.만화  메뉴 클릭")
        self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='만화']").click()
        print("\n 4.만화  메뉴 클릭 완료!")
        sleep(3)
        self.driver.get_screenshot_as_file("c:/result/02_test_comics_mode.png")
        
        
        print("\n 5.만화 장르 메뉴  클릭")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='장르']").click()
        print("\n 6.만화 장르 메뉴  클릭 완료!")
        sleep(10)
        self.driver.get_screenshot_as_file("c:/result/03_test_comics_mode.png")
        
        print("\n 7.만화 장르 스릴러  클릭")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='스릴러']").click()
        print("\n 8.만화 장르 스릴러  클릭 완료!")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/04_test_comics_mode.png")
        
        print("\n 9.뒤로가기 버튼  클릭")
        self.driver.find_element_by_xpath("//android.widget.ImageButton").click()        
        print("\n 10.뒤로가기 버튼  클릭 완료!")
        sleep(3)
        self.driver.get_screenshot_as_file("c:/result/05_test_comics_mode.png")

        print("\n 11.요일별 카테고리 버튼 클릭")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='요일별']").click()
        print("\n 12.요일별 카테고리 버튼 클릭 완료!")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/06_test_comics_mode.png")

        print("\n 13.일요일 버튼 클릭")
        self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='일']").click()
        print("\n 14.일요일 버튼 클릭 완료!")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/07_test_comics_mode.png")
        
        print("\n 15.만화 원한강천록 보기")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='월한강천록']").click()
        print("\n 16.만화 원한강천록 보기 완료")        
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/08_test_comics_mode.png")

        print("\n 17.뒤로가기 버튼  클릭")
        self.driver.find_element_by_xpath("//android.widget.ImageButton").click()        
        print("\n 18.뒤로가기 버튼  클릭 완료!")
        sleep(3)
        self.driver.get_screenshot_as_file("c:/result/09_test_comics_mode.png")
        print("\n 19.만화 부분  완료!")
        
    def test_novel_mode(self):        
        #소설 부분
        sleep(5)
        print("\n 0.소설 부분 시작!")
        sleep(1)
        print("\n 1.사이드 메뉴 클릭")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        print("\n 2.사이드 메뉴 활성화 완료!")        
        sleep(3)
        self.driver.get_screenshot_as_file("c:/result/01_test_novel_mode.png")
        
        print("\n 3.소설 메뉴 클릭")
        self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='소설']").click()
        print("\n 4.소설 메뉴 클릭 완료")
        sleep(3)
        self.driver.get_screenshot_as_file("c:/result/02_test_novel_mode.png")
        
        print("\n 5.장르 카테고리 클릭 ")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='장르']").click()
        print("\n 6.장르 카테고리 클릭 완료")
        sleep(10)
        self.driver.get_screenshot_as_file("c:/result/03_test_novel_mode.png")

        print("\n 7.개그 카테고리 클릭")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='개그']").click()
        print("\n 8.개그 카테고리 클릭")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/04_test_novel_mode.png")

        print("\n 9.시니콘! 선택 클릭")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='시니콘!']").click()
        print("\n 10.시니콘! 선택 클릭 완료")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/05_test_novel_mode.png")
        
        print("\n 11.뒤로가기 클릭")
        self.driver.find_element_by_xpath("//android.widget.ImageButton").click()        
        print("\n 12.뒤로가기 클릭 완료")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/06_test_novel_mode.png")
        
        print("\n 13.뒤로가기2 클릭")
        self.driver.find_element_by_xpath("//android.widget.ImageButton").click()        
        print("\n 14.뒤로가기2 클릭 완료")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/07_test_novel_mode.png")
        print("\n 15. 소설 부분 완료!")
        
    def test_cs_mode(self):
        #고객지원 ->연재관련공지 -> X
        sleep(5)
        print("\n 0. 고객지원 부분 시작")
        sleep(1)
        print("\n 1.사이드 메뉴 클릭")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        print("\n 2.사이드 메뉴 활성화 완료!")        
        sleep(3)
        self.driver.get_screenshot_as_file("c:/result/01_test_cs_mode.png")
        
        print("\n 3. 고객지원 메뉴 클릭")
        self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='고객 지원']").click()
        print("\n 4..고객지원 메뉴 클릭 완료")
        sleep(10)
        self.driver.get_screenshot_as_file("c:/result/02_test_cs_mode.png")
        
        print("\n 5. 연재 관련 공지  클릭")
        self.driver.find_element_by_xpath("//android.widget.ListView//android.view.View[@content-desc='연재 관련 공지']").click
        print("\n 6. 연재 관련 공지  클릭 완료")
        sleep(3)        
        self.driver.get_screenshot_as_file("c:/result/03_test_cs_mode.png")

        print("\n 7. 뒤로가기 클릭")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        print("\n 8. 뒤로가기 클릭 완료")
        sleep(3)        
        self.driver.get_screenshot_as_file("c:/result/04_test_cs_mode.png")
        print("\n 9. 고객지원 관련 완료!")
        
        
    def test_login_mode(self):
        #로그인 / 로그아웃
        sleep(5)
        print("\n 0. 로그인/로그아웃  부분 시작")
        sleep(1)
        print("\n 1.사이드 메뉴 클릭")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        print("\n 2.사이드 메뉴 활성화 완료!")        
        sleep(3)
        self.driver.get_screenshot_as_file("c:/result/01_test_login_mode.png")
        
        print("\n 3.로그인/회원가입 버튼 클릭")
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='로그인/회원가입']").click()
        print("\n 4.로그인/회원가입 버튼 클릭 완료")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/02_test_login_mode.png")

        print("\n 5. 아이디 텍스트 박스 찾고, 아이디 입력 ")
        self.driver.find_element_by_xpath("//TextInputLayout[@text='이메일']//android.widget.EditText").send_keys("ajh910@naver.com")
        print("\n 6. 아이디 텍스트 박스 찾고, 아이디 입력 완료 ")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/03_test_login_mode.png")

        print("\n 7. 패스워드  텍스트 박스 찾고, 패스워드 입력 ")
        self.driver.find_element_by_xpath("//TextInputLayout[@text='비밀번호']//android.widget.EditText").send_keys("******")
        print("\n 8. 패스워드  텍스트 박스 찾고, 패스워드 입력 완료 ")
        sleep(5)
        self.driver.get_screenshot_as_file("c:/result/04_test_login_mode.png")

        print("\n 9. 로그인 버튼 클릭")
        self.driver.find_element_by_id("com.lezhin.comics.plus:id/lza_btn_activity_sign_in_email").click()
        print("\n 10. 로그인 버튼 클릭 완료")
        sleep(10)        
        self.driver.get_screenshot_as_file("c:/result/05_test_login_mode.png")
        
        print("\n 11. 사이드 메뉴 클릭")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        print("\n 12. 사이드 메뉴 클릭 완료")
        sleep(3)        
        self.driver.get_screenshot_as_file("c:/result/06_test_login_mode.png")
        
        print("\n 13. 로그아웃 버튼 활성화")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        print("\n 14. 로그아웃 버튼 활성화 완료")
        sleep(3)        
        self.driver.get_screenshot_as_file("c:/result/07_test_login_mode.png")
        
        print("\n 15. 로그아웃 버튼 클릭")
        self.driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='로그아웃']").click()
        print("\n 16. 로그아웃 버튼 클릭 완료")
        sleep(3)        
        self.driver.get_screenshot_as_file("c:/result/08_test_login_mode.png")
        
        print("\n 17. 사이드 메뉴 클릭")
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        print("\n 18. 사이드 메뉴 클릭 완료")
        sleep(3)        
        self.driver.get_screenshot_as_file("c:/result/09_test_login_mode.png")
        
        print("\n 19. 로그아웃 된 내용 확인")
        sleep(3)
        print("\n 20. 로그인/로그아웃부분 완료!")       
        
        
        
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(lezhin_Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)

#주소창 
