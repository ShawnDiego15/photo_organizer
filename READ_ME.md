# Photo Organizer

The goal of the photo organizer application is to organize a folder of media (`.jpg`, `.jpeg`, `.png` files) by their creation date. In the event a creation date cannot be found, the program is written to organize them by their last modified date.

The end result will be as follows:
- A photo taken on 5/4/2025 is currently in a folder with photos taken from 1/1/2025 to 5/4/2025.
- Upon execution, the photo from 5/4/2025 will now be in a folder with a file name '2025-05-04'

***NOTE:*** By default, this program MOVES files and DOES NOT COPY them. Files that are in an unorganized folder will not exist after execution as they will be moved to an organized folder.

Instructions on Setting up Your Enviornment:
1. Install VSCode (https://code.visualstudio.com/download)
2. Open VSCode.
3. On the left side of the screen, click the 4 squares titled "Extensions".
4. In the searchbar, type "Python". Find the Python extension and click install.
5. Click on "File" in the top left of your VSCode Window and select "Open Folder".
6. Navigate to the folder "photo_organizer" and select it.
7. Once you are in the "photo_organizer" folder within VSCode, click on "New Folder" in the top left of the file browser.
8. Name this folder "unorganized_media".
9. Repeat step 7, naming the second folder "organized_media".

Instructions on Testing Python Installation (Optional):
1. Click on the "Explorer" tab, on the left side of the screen within VSCode.
2. Select the file `python_test.py`.
3. With this file open, the top right of the screen in VSCode should display a play button titled 'Run Python File'. Click this button.
4. A terminal window should open in the bottom half of your screen. It will contain a lot of text that is irrelevant, but if you see the text `Hello World! If you are able to read this, your Python installation should be working correctly.`, then there are no issues.

Instructions on Running the Organization Program:
1. In the top of the screen, click on "Terminal" and "New Terminal".
2. This should open a terminal window (if one is not already open) in the bottom half of your screen.
3. Select the last line of the terminal, you should see a white box appear. You should also be able to type (do not hit enter) if you would like to verify.
4. Within the terminal enter `pip install Pillow` and press enter. Let this run for a few seconds, you should see a confirmation installation was successful.
5. Upload all media you want to sort to the 'unorganized_media' folder. This can be done in batches, or all can be uploaded at once. At first, I would recommend using a small batch of photos to review the output and confirm this organization is accurate.
    1. ALL MEDIA SHOULD BE DIRECTLY LOCATED IN THIS FOLDER, NOT SECTIONED OFF IN OTHER FOLDERS.
    2. Example correct filepath: unorganized_media (folder) -> picture_1, picture_2, picture_3
    3. Example incorrect filepath: unorganized_media (folder) -> jones_family (folder) -> picture_1, picture_2, picture_3
6. Once media is ready, open the "photo_organizer.py" file in the Explorer tab.
7. Click "Run Python File" and wait for the process to finish.

All photos can be organized at once or done in batches. The program should not create duplicate folders, so if a file for 2025-01-01 already exists and a second batch contains a photo created at that date, it will be sorted into the file as well.

In addition, I've added a commented out line of code `dest_path = os.path.join(DEST_FOLDER, "baseball_game", folder_name)`. This can be used for further organization if desired. An example of this is as follows:
1. One drive of photos is only for pictures of baseball games but they were taken across years.
2. If this line is added, replacing the current `dest_path = os.path.join(DEST_FOLDER, folder_name)`, then the organization would follow this format:
    - organized_media
        - baseball_game
            - 2024-05-04
            - 2024-12-01
            - 2025-01-09
            - 2025-05-02
