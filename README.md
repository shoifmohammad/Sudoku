# Sudoku

> **About :**
  - Sudoku is a very popular puzzle game. Every row and column should have digits 1 to 9. Even the small 3x3 grids should have 1 to 9 digits. So, no duplicates will be there. This Sudoku is a GUI based sudoku which have some other features too.
  <p align="center">
  <img width="600" height="450" src="https://github.com/shoifmohammad/Sudoku/blob/master/screenshots/basic.png">
  </p>
  
> **Features :**
  
  - **Error**
  <br></br>
  &nbsp;&nbsp;&nbsp;&nbsp; Error will be raised if you put some wrong digit. This will mark the wrong digits.
  <p align="center">
  <img width="600" height="450" src="https://github.com/shoifmohammad/Sudoku/blob/master/screenshots/error.png">
  </p>
  
  - **Pause/play**
  <br></br>
  &nbsp;&nbsp;&nbsp;&nbsp; You can pause the game in between by clicking the button or hitting space key. You can again resume the game in same ways. If your game is paused, your timer will start to work again automatically if you start to solve the puzzle.
  
  - **Solver**
  <br></br>
  &nbsp;&nbsp;&nbsp;&nbsp; Every mode has a solver in it. You have to just click the solve button and you'll get the final solution. If you have put some values wrong as the grid is not solvable anymore and you are trying to get solution, it will raise an error.
  <p align="center">
  <img width="600" height="450" src="https://github.com/shoifmohammad/Sudoku/blob/master/screenshots/solver.png">
  </p>
  <p align="center">
    Solved by the solver
  </p>
  
  - **Custom Mode**
  <br></br>
  &nbsp;&nbsp;&nbsp;&nbsp; This mode will help you to create your own puzzle. If you get stuck while solving another grids (e.g. in newspapers or magazines) somehow then you can use it to get solution.
  <p align="center">
  <img width="600" height="450" src="https://github.com/shoifmohammad/Sudoku/blob/master/screenshots/custom.png">
  </p>
  
  - **Image Detection**
  <br></br>
  &nbsp;&nbsp;&nbsp;&nbsp; There is a mode named 'Image' that provides you option to choose an image of sudoku grid in '.jpg', '.jpeg' or '.png' format. Then the grid will be detected from the image and you can proceed further. For example you can use the sample images of sudoku grid from 'samle' folder.
  <br></br>
  The method for grid detection has to be improved. *Feel free to give a pull request.*
  
  <p align="center">
  <img width="400" height="300" src="https://github.com/shoifmohammad/Sudoku/blob/master/screenshots/image1.png">
  </p>
  <p align="center">
    Choosing image
  </p>
  
  <p align="center">
  <img width="400" height="400" src="https://github.com/shoifmohammad/Sudoku/blob/master/sample/Sudoku_1.jpg">
  </p>
  <p align="center">
    Original image
  </p>
  
  <p align="center">
  <img width="400" height="300" src="https://github.com/shoifmohammad/Sudoku/blob/master/screenshots/image2.png">
  </p>
  <p align="center">
    Detected Grid
  </p>
  
> **Technology used :**  
  - Python
  - pygame
  - tesseract-ocr
  - pillow
  
> **Required python packages :**
  - pygame, tkinter, PIL, pytesseract
  
  ```
        Installation: pip install pygame, tkinter, PIL, tesseract-ocr
  ```
  
> **How to run :**
  - Run the 'game.py' in python3

> **References :**
  - [Pygame Documentation](https://www.pygame.org/docs/)
  - [Hough Lines transformation](https://www.youtube.com/watch?v=gbL3XKOiBvw)
