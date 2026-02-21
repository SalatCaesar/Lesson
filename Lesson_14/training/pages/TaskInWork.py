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

        from pages.TaskCard import TaskCard

        self.create_dwbtn.select(regulation)
        card = TaskCard(self.driver)
        card.check_open()
        return card
