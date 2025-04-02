from user_interface import Ui_EditTask
from PySide6.QtCore import QDate

class EditTaskUI:
    def __init__(self,ui,task,parent_form):
        self.super_ui = ui
        self.parent_form = parent_form
        self.task = task

        self.ui_form = Ui_EditTask(self.parent_form.ui_form)
        self.ui_form.ui.setModal(True)

        self.button_binding()
        self.install_settings()

    def button_binding(self):
        self.ui_form.ui.button_add_task.clicked.connect(self.edit_task_save_clicked)
        self.parent_form.ui_form.ui.listWidget.itemDoubleClicked.connect(self.doubleclick_in_task)


    def install_settings(self):
        self.ui_form.ui.input_date_task_box.setCalendarPopup(True)
        self.ui_form.setFixedSize(270, 205)


    def edit_task_save_clicked(self):

        input_name_task, input_text, type_task, date = self.get_data_from_form()
        type_task = self.task.type_task_names[type_task]
        select_task = self.super_ui.ui_selected_task_index
        task_id = self.super_ui.task_ids_from_the_database['ItemTaskId'][select_task]['id']

        self.task.update(task_id=task_id,
                         name=input_name_task,
                         text=input_text,
                         date=date,
                         type_task=type_task)

        self.parent_form.update_list()
        self.ui_form.hide()


    def doubleclick_in_task(self, item):
        selected = self.parent_form.ui_form.ui.listWidget.row(item)
        self.super_ui.ui_selected_task_index = selected

        id_in_database = self.super_ui.task_ids_from_the_database['ItemTaskId'][selected]['id']
        task_data = self.task.get(where=id_in_database)

        self.ui_form.ui.input_taskname_line.setText(task_data['name'])
        self.ui_form.ui.input_addinfo_textline.setText(task_data['text'])

        index_type = self.task.type_task_names_reverse[task_data['type']]
        self.ui_form.ui.input_type_task_box.setCurrentIndex(index_type)

        date = QDate.fromString(str(task_data['date']), "yyyy-MM-dd")
        self.ui_form.ui.input_date_task_box.setDate(date)
        self.super_ui.show_form(form='edit_task')


    def get_data_from_form(self) :
        input_name_task = self.ui_form.ui.input_taskname_line.text()
        input_text = self.ui_form.ui.input_addinfo_textline.toPlainText()

        type_task = self.ui_form.ui.input_type_task_box.currentIndex()
        date_str = self.ui_form.ui.input_date_task_box.date()
        date_str = date_str.toString("yyyy-MM-dd")

        return input_name_task, input_text, type_task, date_str