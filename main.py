import tdl


SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

test_string = 'hello, world'
window_title = '/r/roguelikedev complete tutorial'


def main():
    tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)

    console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title=window_title, fullscreen=False)
    console.draw_str((SCREEN_WIDTH-len(test_string))//2, SCREEN_HEIGHT//2, test_string)

    tdl.flush()

    tdl.event.keyWait()


if __name__ == "__main__":
    main()
