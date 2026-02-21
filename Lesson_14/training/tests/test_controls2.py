from datetime import datetime

from atf import *
from atf.ui import *

from pages.AuthPages import AuthPage
from pages.TaskInWork import TaskInWork


class TestControls2(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        cls.browser.open(cls.config.get('SITE'))
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))

    def setUp(self):
        TaskInWork(self.driver).open()

    def test_1(self):
        """В карточке задачи заполнить: Описание, ответственного
           Запустить на выполнение
           Открыть на редактирование и добавить веху"""

        task_data = {'Исполнитель': 'Задач Автотест',
                     'Описание': 'Для вебинара по автотестированию ' + str(datetime.now().strftime('%H%M%S'))}

        task_page = TaskInWork(self.driver)
        task_card = task_page.create_document('Задача')

        task_card.fill_task(**task_data)
        task_card.run_task()
        delay(2)
        task_card.open_to_edit()
        task_card.select_milestone('Смена вехи 3')
        task_card.delete_open_task()

    def test_2(self):
        """В карточке задачи выбрать ответственного через справочник"""

        task_page = TaskInWork(self.driver)
        task_card = task_page.create_document('Задача')
        task_card.check_open()
        task_card.executor.open_data_dictionary().select('Задач Автотест')
        task_card.executor.should_be(ContainsText('Задач Автотест'))
        task_card.delete_open_task()

    def tearDown(self):
        self.browser.close_windows_and_alert()
