from controls import *
from atf.ui import *
from pages.dialog import Dialog as AddMilestone
from pages.popup import Stack


@templatename("EDWS3/Tasks/taskDialog:Dialog")
class Dialog(DocumentTemplate):

    executor_cl = ControlsLookupInput(By.CSS_SELECTOR, '.edws-StaffChooser__lookup', 'исполнитель', catalog=Stack)
    desc_re = RichEditorExtendedEditor(By.CSS_SELECTOR, '.richEditor_Base_textContainer', 'описание')
    milestone_btn = Button(By.CSS_SELECTOR, '.edws-DueDateChange__button-link', 'Веха / Срок')
    phase_elm = ControlsButton(caption='На выполнение')
    new_phase = Element(By.CSS_SELECTOR, '.extControls-doubleButton__captionContent-start-m', 'Выполнение')
    change_lnk = ControlsButton(By.CSS_SELECTOR, '[data-qa="edo3-ReadOnlyStateTemplate__changeButton"]', 'Изменить')

    def fill_task(self, **kwargs):
        """Заполнять задачу"""

        if 'Исполнитель' in kwargs.keys():
            self.executor_cl.autocomplete_search(kwargs['Исполнитель'])
        if 'Описание' in kwargs.keys():
            self.desc_re.type_in(kwargs['Описание'])

    def run_task(self):
        """Оправить на выполнение"""

        self.phase_elm.click()
        self.phase_elm.should_not_be(Displayed)
        self.new_phase.should_be(Displayed)

    def select_milestone(self, name_milestone):
        """Выбираем веху
        :param name_milestone: Имя вехи
        """

        self.milestone_btn.click()
        AddMilestone(self.driver).add_milestone(name_milestone)
        self.milestone_btn.should_be(ContainsText(name_milestone))

    def open_to_redaction(self):
        """Открыть на редактирования"""

        if self.change_lnk.is_displayed:
            self.change_lnk.click()
        self.change_lnk.should_not_be(Displayed)
