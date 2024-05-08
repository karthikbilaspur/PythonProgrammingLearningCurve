from notifypy import Notify

# Create a notification object
notification = Notify()

# Set the title and message for the notification
notification.title = "Task Reminder"
notification.message = "You have an important task due soon."

# Set the urgency level
notification.urgency = "critical"

# Set the path to the notification icon
notification.icon = "/path/to/icon.png"

# Set the timeout for the notification
notification.timeout = 10000  # 10 seconds

# Display the notification
notification.send()