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
   git clone https://github.com/YOUR_GITHUB_USERNAME/todo_management.git
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

## Screenshots
*(Attach relevant screenshots of the module views.)*

## Contribution
- Fork this repository.
- Create a new branch: `feature-xyz`
- Commit your changes.
- Push and create a Pull Request.

## License
This module is released under the **MIT License**.
