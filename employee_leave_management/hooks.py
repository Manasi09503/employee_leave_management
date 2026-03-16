app_name = "employee_leave_management"
app_title = "Employee Leave Management"
app_publisher = "Manasi More"
app_description = "Employee Leave Management System"
app_email = "moremanasi9503@gmail.com"
app_license = "MIT"
fixtures = [
    {
        "dt": "DocType",
        "filters": [
            ["name", "in", ["Employee1", "Leave Request"]]
        ]
    },
    {
        "dt": "Report",
        "filters": [
            ["name", "in", ["Leave Summary Report"]]
        ]
    }
]
