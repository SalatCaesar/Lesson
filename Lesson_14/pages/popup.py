from controls import *
from atf.ui import *


@templatename("Addressee/popup:Stack")
class Stack(CatalogTemplateList):
    """Выбор сотрудник"""

    list_grid = ControlsListView(By.CSS_SELECTOR, '[data-qa="msg-addressee-selector__plain-list-view"]', 'Лист')