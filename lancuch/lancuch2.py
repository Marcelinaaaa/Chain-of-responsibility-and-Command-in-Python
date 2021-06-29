class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = f'handle_{event}'
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent is not None:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print(f'MainWindow: {event}')

    def handle_default(self, event):
        print(f'MainWindow Default: {event}')


class SendDialog(Widget):
    def handle_paint(self, event):
        print(f'SendDialog: {event}')


class MsgText(Widget):
    def handle_down(self, event):
        print(f'MsgText: {event}')

    #def handle_down(self, event):
    #    print(f'MsgText MV: {event}')



def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)
    #msgmv = MsgText(mw)

    newwidget = input("If you want create new instance of MsgTextMW, press Y")
    if newwidget in 'Yy':
        msgmv = MsgText(mw)
    else:
        pass
    events = ['down', 'paint', 'unhandled', 'close']
    newevent = input("If you want create new_event, press Y")
    if newevent in 'Yy':
        newevent_name = input("New event name: ")
        events.append(newevent_name)
    for e in events:
        evt = Event(e)
        print(f'Sending event -{evt}- to MainWindow')
        mw.handle(evt)
        print(f'Sending event -{evt}- to SendDialog')
        sd.handle(evt)
        print(f'Sending event -{evt}- to MsgText')
        msg.handle(evt)
        if newwidget in 'Yy':
            print(f'Sending event -{evt}- to MsgTextMV')
            msgmv.handle(evt)
        print('--------------')


if __name__ =='__main__':
    main()

# Dodanie zdarzenia było trudniejsze.