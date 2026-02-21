from controls import *


@templatename('PM/Milestones/dialog:Dialog')
class MilestoneCard(DocumentTemplate):
    """Карточка вех"""

    add_task_btn = Button(By.CSS_SELECTOR, '.icon-RoundPlus', 'добавить задачу')
    search_task_cs = ControlsSearchInput()
    task_filter_cfv = ControlsFilterView(By.CSS_SELECTOR, '.controls-FilterView', 'Фильтр')
    task_grid_tgv = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-Grid', 'Таблица')
    header_line = Element(By.CSS_SELECTOR, '.layout-Browser__header', 'Заголовочная линия')
