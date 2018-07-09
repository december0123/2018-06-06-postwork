'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).

W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy:

- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop".

Podpowiedź: Użyj wzorca Command (polecenie).

W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.

Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd, sys
import turtle

class Command:
    def __init__(self, turtle, arg):
        self.turtle = turtle
        self.arg = arg
class ForwardCommand(Command):
    def __init__(self, turtle, arg):
        super().__init__(turtle, arg)
    def execute(self):
        self.turtle.forward(int(self.arg))

class RightCommand(Command):
    def __init__(self, turtle, arg):
        super().__init__(turtle, arg)
    def execute(self):
        self.turtle.right(int(self.arg))

class LeftCommand(Command):
    def __init__(self, turtle, arg):
        super().__init__(turtle, arg)
    def execute(self):
        self.turtle.left(int(self.arg))

class HomeCommand(Command):
    def __init__(self, turtle, arg):
        super().__init__(turtle, arg)
    def execute(self):
        self.turtle.home()

class CircleCommand(Command):
    def __init__(self, turtle, arg):
        super().__init__(turtle, arg)
    def execute(self):
        self.turtle.circle(int(arg))

class PositionCommand(Command):
    def __init__(self, turtle, arg):
        super().__init__(turtle, arg)
    def execute(self):
        print('Current position is %d %d\n' % self.turtle.position())

class HeadingCommand(Command):
    def __init__(self, turtle, arg):
        super().__init__(turtle, arg)
    def execute(self):
        print('Current heading is %d\n' % (self.turtle.heading(),))

class ResetCommand(Command):
    def __init__(self, turtle, arg):
        super().__init__(turtle, arg)
    def execute(self):
        self.turtle.reset()

class Invoker:
    def __init__(self):
        self._history = []
        self.recording = False

    def record(self):
        self._history = []
        self.recording = True

    def execute(self, command):
        command.execute()
        if self.recording:
            self._history.append(command)

    def playback(self):
        for command in self._history:
            command.execute()

    def stop(self):
        self.recording = False

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    invoker = Invoker()

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        self.invoker.execute(ForwardCommand(turtle, arg))
    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        self.invoker.execute(RightCommand(turtle, arg))
    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        self.invoker.execute(LeftCommand(turtle, arg))
    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        self.invoker.execute(HomeCommand(turtle, arg))
    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        self.invoker.execute(CircleCommand(turtle, arg))
    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        self.invoker.execute(PositionCommand(turtle, arg))
    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        self.invoker.execute(HeadingCommand(turtle, arg))
    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        self.invoker.execute(ResetCommand(turtle, arg))
    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        turtle.bye()
        return True
    def do_record(self, arg):
        self.invoker.record()
    def do_stop(self, arg):
        self.invoker.stop()
    def do_playback(self, arg):
        self.invoker.playback()

if __name__ == '__main__':
    TurtleShell().cmdloop()
