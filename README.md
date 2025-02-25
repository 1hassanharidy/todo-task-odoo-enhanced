# To-Do Management Module

## Overview
This module provides a **To-Do List Management System** for **Odoo 17**, allowing users to create, manage, and track tasks efficiently.

## Features
- Create and manage **To-Do Tasks**.
- Assign tasks to users.
- Track task progress with different **status levels**.
- Set **due dates** for tasks.
- **List, Form, and Search Views** for better task management.

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

 ### Chatter (Activity Log)

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

## Screenshots
### 1. List View
![List View](https://github.com/user-attachments/assets/ba2d1611-808f-4fb6-892d-3d9fe8507cd3)

### 2. Form View & Task Chatter
![Form View](https://github.com/user-attachments/assets/f5c32d71-cae7-47f3-a00c-352f0628b025)

### 3. Module Hierarchy
![Hierarchy](https://github.com/user-attachments/assets/f2c90a3f-0d3d-4705-8718-1ce7d9437077)

## Contribution
- Fork this repository.
- Create a new branch: `feature-xyz`
- Commit your changes.
- Push and create a Pull Request.

## License
This module is released under the **MIT License**.
