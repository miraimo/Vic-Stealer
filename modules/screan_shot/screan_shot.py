import os
import mss

# Screenshot and save in folder
def screan_shot(folder_path: str) -> None:
    try:

        with mss.mss() as sct:
            output = os.path.join(folder_path, "screenshot.png")
            sct.shot(output=output)

    except Exception as err:
        print(err)