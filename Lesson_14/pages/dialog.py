from controls import *
from atf.ui import *
from pages.selector import Dialog as SelectorMil


@templatename("EDWS3/Utils/NewDueDateChange/dialog:Dialog")
class Dialog(DialogTemplate):
    """Диалог выбора вехи """

    mil_link = Element(By.CSS_SELECTOR, '.edws-NewDueDateChange-addMilestoneButton_margin', 'веха')
    apply_btn = ControlsButton(By.CSS_SELECTOR, '.edws-NewDueDateChange-Dialog__confirmButton', 'Применить')

    def add_milestone(self, name_milestone):
        """
        выбор вехи
        :param name_milestone: Имя вехи
        """
        self.mil_link.click()
        SelectorMil(self.driver).select(name_milestone)
        self.apply_btn.click()
