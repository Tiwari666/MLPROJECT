
# src/__init__.py

# Import all necessary files and modules
# Keep only the imports necessary for initialization
from .log_config.logger import logger






"""
The __init__.py file in the src directory serves as an initializer for the package, allowing us to import modules and sub-packages

from the package directly. By importing all necessary files and modules within the __init__.py file, we can make them accessible

from the package's root level, simplifying the import process for users of the package.

In this example, the __init__.py file imports various modules and sub-packages from the src directory, including data_ingestion.

"""

"""
Distinctions between __init__.py and main.py:

1. __init__.py is an initializer file for a package, while main.py is a script that serves as the entry point for an application.

2. __init__.py is typically used to import modules and sub-packages within a package, making them accessible from the package's 
root level.

3. main.py is used to define the main functionality of an application, such as setting up configurations, running the application.

4. __init__.py is executed when a package is imported, while main.py is executed when the application is run directly.

5. __init__.py is not mandatory in Python 3.3 and later versions, while main.py is essential for running the application.

6. __init__.py is used to organize code into modules and sub-packages, while main.py is used to define the primary logic of the 
application.

7. __init__.py is typically an empty file or contains import statements, while main.py contains the main functionality of the
application.

8. __init__.py is located within a package directory, while main.py is typically located at the root level of the application.

9. __init__.py is used to define a package, while main.py is used to define the main execution flow of the application.

10. __init__.py is used to initialize a package and make its contents accessible, while main.py is used to define the primary
functionality of the application.


"""



"""
 In Python projects, it's common to place the __init__.py file inside the src folder to initialize the package, 
 and the main.py file at the root level of the application to serve as the entry point. This structure allows us to organize
our code effectively and maintain a clear separation between the package's internal modules and 
the application's main execution script.

src/ Directory: Contains alll the application's modules and packages. The __init__.py file inside this directory marks it as
 a Python package, allowing us to import its modules elsewhere in our project.

main.py File: Located at the root of the project, this file serves as the entry point to our application. 
It can import modules from the src package to utilize their functionalities.

__init__.py File: Placed inside the src/ directory, this file initializes the package and can be used to import
 modules for easier access.
"""






""" 
The __init__.py file in Python serves as an initializer for a package, allowing us to execute initialization code 
when the package is imported. While it's not mandatory in Python 3.3 and later versions, 
including an empty __init__.py file is considered good practice to clearly define a directory as a package. 


In my src directory, I have created an empty __init__.py file to indicate that the directory should be treated as a package. 
This helps in organizing code into modules and sub-packages, making it more manageable and maintainable.

If we need to execute specific initialization code when the package is imported, 
we can include it within the __init__.py file. 
For example, we might want to set up logging configurations or import frequently used functions. 

Specifically, setting up logging configurations in Python involves configuring the logging system to record messages about 
our application's operation, which is essential for debugging and monitoring. 

By configuring logging in this manner, we can track various events in our application, which aids in debugging 
and understanding the application's behavior.

"""

"""
The __init__.py file is used to initialize the package (in this case, the src folder).

By importing everything in __init__.py, it ensures that all necessary files in the src folder are available 
when src is imported elsewhere in this project.

This is a good practice to manage our project, especially when there are multiple modules.

So, the code for src/__init__.py  will ensure that we can access the necessary modules directly when you use the following script:

'from src import data_ingestion, data_transformation, model, logging, exceptions'

This way, we can access the functions and classes defined in these modules without having to import them individually 
in the main script.
"""

"""
main.py is the entry point for executing the project logic.

__init__.py helps organize and make the project easier to work with by handling module imports."""