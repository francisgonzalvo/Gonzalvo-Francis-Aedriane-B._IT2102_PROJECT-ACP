




FINAL PROJECT DOCUMENTATION
CS121: ADVANCED COMPUTER PROGRAMMING







Submitted By:
Gonzalvo, Francis Aedriane B.
IT – 2102


















I.PROJECT OVERVIEW

The School Supplies Management System was created to simplify and organize the distribution of school materials such as notebooks, pens, and other essential items needed for education. Through this system, we can better monitor the supplies students need for their studies. It will also make it easier for teachers, as they can quickly determine what and how many supplies the students require.

The system includes three main features to enhance its functionality. The first is Student Management, where you can input the names and grade levels of students to determine the specific school supplies they need and the quantities required. The second feature is Inventory Management, which allows you to add, update, and view inventory items. This section includes the item names and the quantities of supplies you plan to use. Lastly, there is Distribution Management, which helps track which students will receive the items and in what quantities. This feature also enables you to efficiently manage the distribution of supplies to students. In excluded features  for this system are financial management, as the system does not handle financial transactions or budgeting. It also does not include advanced analytics, as it does not have advanced reporting features such as predictive analytics or budget forecasting.

School Administrator  and Teachers are the main target of this system. In school administrator they can use this system by managing students information, inventory and tracking the distribution of supplies. The teachers use this system by requesting supplies for their students and tracking the distribution process. 

The project will use Tkinter for the graphical interface and SQLite for the database, making it feasible for small-to-medium scale use in educational institutions. The system will be highly relevant to schools and organizations, helping them efficiently allocate and manage limited resources. The development of the system is set to be completed within 2 months, with all features fully implemented, tested, and validated, ensuring it is ready for deployment by the end of the timeframe.















II.PYTHON CONCEPTS AND LIBRARIES


Python Tkinter
	
    Tkinter is used to create the graphical interface for the School Supply Management System. This allows the user, usually a school administrator, to interact with the application through buttons, text fields, and tables instead of using command-line commands. Tkinter makes sure the system is easy to use, with a clear layout for managing students, inventory, and item distribution. The interface is organized into tabs using ttk.Notebook, and different widgets like Entry, Label, and Treeview are used in each tab to show and manage data. Tkinter responds to user actions like clicking buttons (e.g., "Add Student" or "Distribute Item") by triggering the right functions in the program to update the database.

MySQL
SQLite is used to store and manage data for the school supply system. It’s a lightweight, easy-to-use database that doesn’t require a separate server, making it perfect for small applications like this one. In this system, SQLite manages three main tables: students, inventory items, and distribution records.




























III.SUSTAINABLE DEVELOPMENT GOALS

The School Supply Management System created focuses on several aspects of the Sustainable Development Goals (SDGs) to improve the quality of education and reduce inequality. First, by ensuring that every student has sufficient school supplies, the system helps achieve Goal 4: Quality Education, providing equal opportunities for all students, especially those from disadvantaged sectors. It further promotes Goal 10: Reduced Inequality through fair sharing of supplies, helping remove barriers to education, and, thus reducing disparities on socioeconomic status.


IV.PROGRAM/SYSTEM INSTRUCTIONS
V.


When you run the code, it will show a GUI with options for Student Management, Inventory Management, and Distribution Management.

• Student Management: Here, you can input the names and grades of students. You can also add more students by clicking the “Add Student” button.

• Inventory Management: This allows you to add items by entering the item name and the quantity of school supplies needed.

• Distribution Management: In this section, you can assign items to students by providing the Student ID, Item ID, and Quantity. When you click the “Distribute” button, the system will check if the student and item exist.
