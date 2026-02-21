from atf import *
from atf.ui import *
from controls import *

from pages.MilestoneDialog import MilestoneDialog
from pages.StaffSelector import StaffSelector


@templatename('EDWS3/Tasks/taskDialog:Dialog')
class TaskCard(DocumentTemplate):
    """Карточка задачи"""

    next_phase_btn = ControlsButton(caption='На выполнение')
    executor = ControlsLookupInput(rus_name='Исполнитель', catalog=StaffSelector)
    description = RichEditorExtendedEditor(rus_name='Описание задачи')
    edit_elm = Element(SabyBy.DATA_QA, 'edo3-ReadOnlyStateTemplate__changeButton', 'Изменить')
    milestone_lnk = ControlsButton(By.CSS_SELECTOR, '.edws-DueDateChange__button-link', 'Срок/Веха')
    _elm = Element(SabyBy.DATA_QA, 'deleteDocument', 'Удалить')
    toolbar = ControlsToolbarsView(SabyBy.DATA_QA, 'edo3-Toolbar__container', 'Описание')

    def fill_task(self, **kwargs):

        self.check_open()
        if 'Исполнитель' in kwargs.keys():
            self.executor.autocomplete_search(kwargs['Исполнитель'])
        if 'Описание' in kwargs.keys():
            self.description.type_in(kwargs['Описание'])

    def run_task(self):

        self.next_phase_btn.click()

    def open_to_edit(self):
        """
        Открыть для редактирования
        """

        if wait(lambda: self.edit_elm.is_displayed, 2):
            info('Открываем документ на редактирование')
            self.edit_elm.click()
        self.edit_elm.should_not_be(Displayed, msg='Документ не открылся для редактирования')

    def select_milestone(self, milestone_name):

        self.milestone_lnk.click()
        mil_dial = MilestoneDialog(self.driver)
        mil_dial.check_open()
        catalog = mil_dial.open_selector()
        catalog.select(milestone_name)
        mil_dial.apply_selected()
        self.milestone_lnk.should_be(ContainsText(milestone_name))

    def delete_open_task(self):
        """Удаляем открытую задачу"""

        self.toolbar.select(data_qa='deleteDocument')
        self.popup_confirmation.confirm()
        self.check_close()
