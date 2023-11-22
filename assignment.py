import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QCalendarWidget

def open_assignment():
    app = QApplication(sys.argv)
    window = QWidget()
    assignments = {}
    init_ui(window, assignments)
    sys.exit(app.exec_())

def init_ui(window, assignments):
    # Initialize the main UI components
    layout = QVBoxLayout()

    # Course selection
    label_course = QLabel("Select Course:")
    course_combobox = QComboBox()
    course_combobox.addItems(["EPHYL111L", "EMAT101L", "CSET101", "CSET108"])
    layout.addWidget(label_course)
    layout.addWidget(course_combobox)

    # Assignment input
    label_assignment = QLabel("Enter Assignment Name:")
    assignment_entry = QLineEdit()
    layout.addWidget(label_assignment)
    layout.addWidget(assignment_entry)

    # Due date selection
    label_due_date = QLabel("Select Due Date:")
    due_date_calendar = QCalendarWidget()
    due_date_entry = QLineEdit()
    due_date_calendar.clicked.connect(lambda: update_due_date_entry(due_date_calendar, due_date_entry))
    layout.addWidget(label_due_date)
    layout.addWidget(due_date_calendar)
    layout.addWidget(due_date_entry)

    # Add Assignment button
    add_button = QPushButton("Add Assignment")
    add_button.clicked.connect(
        lambda: add_assignment(course_combobox, assignment_entry, due_date_entry, result_display, assignments))

    layout.addWidget(add_button)

    # Course selection for display
    label_display = QLabel("Select Course Name to Display Assignment and Due Date:")
    display_entry = QComboBox()
    display_entry.addItems(["EPHYL111L", "EMAT101L", "CSET101", "CSET108"])
    layout.addWidget(label_display)
    layout.addWidget(display_entry)

    # Submit button to show assignments
    submit_button = QPushButton("Submit")
    submit_button.clicked.connect(lambda: show_due_date(display_entry, assignments, result_display))
    layout.addWidget(submit_button)

    # Display area for assignment information
    result_display = QTextEdit()
    result_display.setReadOnly(True)
    layout.addWidget(result_display)

    # Set up the window layout and properties
    window.setLayout(layout)
    window.setWindowTitle('Assignment Due Dates')
    window.setGeometry(100, 100, 600, 450)
    window.show()

def add_assignment(course_combobox, assignment_entry, due_date_entry, result_display, assignments):
    # Add a new assignment to the assignments dictionary
    course_name = course_combobox.currentText()
    assignment_name = assignment_entry.text().strip()
    due_date = due_date_entry.text().strip()

    if assignment_name and course_name and due_date:
        # Add assignment to the dictionary
        assignments[(assignment_name, course_name)] = due_date
        assignment_entry.clear()
        due_date_entry.clear()
        result_display.clear()
        result_display.append(f"Assignment added: {assignment_name} - {course_name} - Due Date: {due_date}")
    else:
        result_display.clear()
        result_display.append("Please enter Assignment Name, Course Name, and Due Date.")


def show_due_date(display_entry, assignments, result_display):
    # Display assignments for the selected course
    course_name_to_display = display_entry.currentText()
    assignments_for_course = get_assignments_by_course_name(course_name_to_display, assignments)

    result_display.clear()
    if assignments_for_course:
        result_display.append(f"Assignments for {course_name_to_display}:")
        for assignment_name, due_date in assignments_for_course:
            result_display.append(f"{assignment_name} - Due Date: {due_date}")
    else:
        result_display.append("No assignments found for the selected course.")

def get_assignments_by_course_name(course_name, assignments):
    # Retrieve assignments for a specific course
    return [(assignment_name, due_date) for (assignment_name, cn), due_date in assignments.items() if cn == course_name]

def update_due_date_entry(due_date_calendar, due_date_entry):
    # Update the due date entry based on the selected date in the calendar
    selected_date = due_date_calendar.selectedDate()
    due_date_entry.setText(selected_date.toString("yyyy-MM-dd"))

if __name__ == '__main__':
    # Call open_assignment to execute the code
    open_assignment()
