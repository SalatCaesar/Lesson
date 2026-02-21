from atf import *
from atf.ui import *
from controls import *


class TaskInWork(Region):
    """Реестр задач В работе"""

    create_dwbtn = ExtControlsDropdownAddButton()

    def open(self):

        log('Переходим в Задачи')
        self.browser.open('https://fix-online.sbis.ru/page/tasks-in-work')
        self.check_page_load_wasaby()

    def create_document(self, regulation='Задача'):
        """:param regulation:"""

        from pages.taskDialog import Dialog

        self.create_dwbtn.select(regulation)
        task_card = Dialog(self.driver)
        task_card.check_open()
        return task_card
