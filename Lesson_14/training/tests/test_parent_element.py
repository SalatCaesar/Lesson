from atf.ui import *
from pages.MilestoneCard import MilestoneCard
from atf import *


class Test(TestCaseUI):

    def test_1(self):

        log('Показываем, что родительский элемент навешивается')
        MilestoneCard(self.driver).add_task_btn.print_locator()

    def test_2(self):

        log('Показываем, что родительский элемент можно установить методом')
        m_card = MilestoneCard(self.driver)
        m_card.header_line.print_locator()
        m_card.add_task_btn.add_parent(m_card.header_line)
        m_card.add_task_btn.print_locator()

    def test_3(self):

        log('Показываем, что родительский элемент снять')
        m_card = MilestoneCard(self.driver)
        m_card.add_task_btn.add_parent(m_card.header_line)
        m_card.add_task_btn.set_absolute_position()
        m_card.add_task_btn.print_locator()


@parent_element('base_elem')
class BaseDoc(Region):
    panel = Element(By.CSS_SELECTOR, '.panel_class', 'Панель')


@parent_element('test1')
class Doc1(BaseDoc):
    pass


class Test1(TestCaseUI):

    doc1 = None

    @classmethod
    def setUpClass(cls):

        cls.doc1 = Doc1(cls.driver)

    def test_1(self):

        log("Добавляем какой-то новый родительский элемент")
        self.doc1.panel.add_parent(BaseDoc(self.driver).panel)
        self.doc1.panel.print_locator()

    def test_2(self):

        log("Тут изменился локатор у документа из-за первого теста")
        self.doc1.panel.print_locator()
