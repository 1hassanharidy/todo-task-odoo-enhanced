# To-Do Management Module

## Overview
This module provides a **To-Do List Management System** for **Odoo 17**, allowing users to create, manage, and track tasks efficiently.

## Features
- Create and manage **To-Do Tasks**.
- Assign tasks to users.
- Track task progress with different **status levels**.
- Set **due dates** for tasks.
- **List, Form, and Search Views** for better task management.
### Enhanced Features

   The following features have been **recently added** to extend the core functionality of the To-Do Management module:

1. **Estimated Time**
    
    * A new field `estimated_time` (float) on `todo.task` allows you to specify the maximum hours (or days) you expect the task to take.
2. **Timesheet Lines**
    
    * Each task can now have **timesheet lines** (e.g., `todo.timesheet.line` model) where users record actual hours spent.
    * The module checks that **the total of all timesheet lines** does **not exceed** the `estimated_time` field.
    * If the total is about to exceed `estimated_time`, you can handle it via a warning or simply block additional entries (implementation depends on your preference).
3. **Archiving Feature**
    
    * You can **archive** tasks in the `todo.task` model when they are no longer needed.
    * Archived tasks are hidden by default but can be viewed if you activate the **Archived** filter.
4. **Server Action: “Close”**
    
    * A **server action** named **Close** is provided to mark tasks as done (or “Closed”) in bulk.
    * You can trigger this action from the tree view or form view, handling **one or multiple** records at once.
5. **Automated Cron Job**
    
    * An **automated scheduled action** (cron job) checks for tasks that are **past their Due Date**.
    * It can notify the assigned user or manager (depending on your configuration) and **highlight late tasks** in the tree view (e.g., by changing their color or status).
6. **Report Action (PDF)**
    
    * A **custom QWeb report** allows you to print each task with its details, timesheet entries, and total time.
    * The layout includes a company logo, address, phone, and pagination, as shown in the sample design.
    * This makes it easy to share or archive a task’s full details (including timesheets) in PDF format.

## Installation
1. Clone this repository into your Odoo `addons` directory:
   ```sh
   git clone https://github.com/1hassanharidy/todo-task-odoo.git
   ```
2. Restart Odoo server:
   ```sh
   odoo-bin -c /etc/odoo.conf -u todo_management
   ```
3. Activate the **developer mode** in Odoo.
4. Navigate to **Apps**, search for "To-Do Management", and install it.

## Usage

### 1. To-Do Model
- **Model Name:** `todo.task`
- **Fields:**
  - **Task Name** – The name of the task.
  - **Assign To** – User responsible for the task.
  - **Description** – Detailed description of the task.
  - **Due Date** – The deadline for the task.
  - **Status** – The current state of the task (`New`, `In Progress`, `Completed`).

### 2. List View
- A menu item **"To-Do" → "All Tasks"** is created.
- Displays all tasks with their key details.

### 3. Form View
- Users can add/edit tasks.
- Includes fields: **Task Name, Assign To, Description, Due Date, Status**.

### 4. Search View
- Allows searching tasks using:
  - **Task Name**
  - **Assigned User**
- Provides filters for:
  - **Status**
  - **Due Date**
  - **Assigned User**

 ### 5. Chatter (Activity Log)

The module includes a **Chatter** feature to log important task updates. The following events are tracked:

- **Task Creation:**  
  - A log entry is added when a new task is created.
  - Displays the creator's name and timestamp.

- **Assignment Changes:**  
  - When the **Assigned To** field is updated, a log entry is created.
  - Displays the previous assignee, the new assignee, and the user who made the change.

- **Due Date Changes:**  
  - When the **Due Date** of a task is modified, a log entry is added.
  - Displays the old due date, the new due date, and the user who made the change.

### 6. Server Action: Close

* From the list or form view, select **Close** to mark tasks as completed.
* Supports **batch operations** on multiple tasks.

### 7. Cron Job for Late Tasks

* Periodically checks for tasks whose **Due Date** is in the past and are not completed.
* Can **notify** users or highlight these tasks in the list view.

### 8. PDF Report

* A **custom QWeb report** prints each task’s details, timesheet lines, total time, and company information (logo, address, phone).
* Can be accessed from the **Print** button on the task form.

## Screenshots
### 1. List View
![List View](https://github.com/user-attachments/assets/f5c32d71-cae7-47f3-a00c-352f0628b025)

### 2. Form View & Task Chatter
![Form View](https://github.com/user-attachments/assets/ba2d1611-808f-4fb6-892d-3d9fe8507cd3)

### 3. Module Hierarchy
![Hierarchy](https://github.com/user-attachments/assets/f2c90a3f-0d3d-4705-8718-1ce7d9437077)

## Contribution
- Fork this repository.
- Create a new branch: `feature-xyz`
- Commit your changes.
- Push and create a Pull Request.

## License
This module is released under the **MIT License**.
