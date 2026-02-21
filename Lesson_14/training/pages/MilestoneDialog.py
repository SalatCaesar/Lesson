from controls import *
from pages.MilestoneSelector import MilestoneSelector


@templatename('EDWS3/Utils/NewDueDateChange/dialog:Dialog')
class MilestoneDialog(DialogTemplate):
    """Выбор диалога"""

    milestone_lnk = ControlsButton(By.CSS_SELECTOR, '.edws-NewDueDateChange-addMilestoneButton_margin', 'веха')
    apply_btn = ControlsButton(By.CSS_SELECTOR, '.edws-NewDueDateChange-Dialog__confirmButton', 'Кнопка принять')

    def open_selector(self) -> MilestoneSelector:
        """Открыть выбор вех.
        :return: Каталог с вехами
        """

        self.milestone_lnk.click()
        mil_select = MilestoneSelector(self.driver)
        mil_select.check_open()
        return mil_select

    def apply_selected(self):
        """Подтвердить выбранные вехи"""

        self.check_close(self.apply_btn.click)
