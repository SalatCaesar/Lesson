from controls import *
from atf.ui import *


@templatename("PM/Milestones/dialog:Dialog")
class MilestoneCard(DocumentTemplate):
    """Карточка вех"""

    add_task_btn = Button(By.CSS_SELECTOR, '.icon-RoundPlus', 'добавить задачу')
    search_task_cs = ControlsSearchInput(By.CSS_SELECTOR, '.controls-Render', 'Поиск')
    task_filter_cfv = ControlsFilterView(By.CSS_SELECTOR, '.controls-FilterView', 'Фильтр')
    task_grid_tgv = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-Grid', 'Таблица')
